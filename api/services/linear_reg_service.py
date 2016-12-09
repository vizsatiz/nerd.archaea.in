import pickle
import json
import threading
from nerd_log_helper import logger
from api.services.application_service import ApplicationService
from machine_learning.linear_regression.lin_reg_trainer import LinearRegressionTrainer
from machine_learning.model_persistance.sci_learn_model import SciLearnModelPersistenceHelper


class LinearRegressionService:

    def __init__(self):
        pass

    @staticmethod
    def compute_linear_regression(application=None, data=None):
        if application is None:
            raise Exception('Unknown application')
        if data is None:
            raise Exception('No data found to do the computation')
        app_metadata = json.loads(application.app_metadata)
        weights = app_metadata['weights']
        lr_object = pickle.loads(weights)
        lr = SciLearnModelPersistenceHelper.initialize_model_with_state(lr_object)
        lr_trainer = LinearRegressionTrainer(lr)
        prediction = lr_trainer.predict(data)
        return prediction.tolist()

    @staticmethod
    def train_linear_regression(application=None, training_data=None):
        if application is None:
            raise Exception('Unknown application')
        if training_data is None:
            raise Exception('No data found for training')
        app_metadata = json.loads(application.app_metadata)
        weights = app_metadata['weights']
        lr_object = pickle.loads(weights)
        lr = SciLearnModelPersistenceHelper.initialize_model_with_state(lr_object)
        lr_trainer_thread = LinearRegressionTrainWorkerThread(lr=lr,
                                                              data_points=training_data['data_points'],
                                                              expectations=training_data['expectations'],
                                                              application=application)
        training_status = json.loads(application.training_status)
        training_status['status'] = 'started'
        ApplicationService.update_application(query={
            'application_id': application.application_id
        }, update_value={
            'training_status': json.dumps(training_status)
        })
        lr_trainer_thread.start()
        return training_status


class LinearRegressionTrainWorkerThread(threading.Thread):

    def __init__(self, lr, data_points, expectations, application):
        super(LinearRegressionTrainWorkerThread, self).__init__()
        self.lr = lr
        self.data_points = data_points
        self.expectations = expectations
        self.application = application

    def run(self):
        try:
            lr_trainer = LinearRegressionTrainer(self.lr)
            lr_trainer.train(self.data_points, self.expectations)
            model_object = SciLearnModelPersistenceHelper.get_model_state(self.lr)
            weights = pickle.dumps(model_object)
            training_status = json.loads(self.application.training_status)
            training_status['status'] = 'done'
            training_status['reference'] = 'trained'
            app_metadata = json.loads(self.application.app_metadata)
            app_metadata['weights'] = weights
            ApplicationService.update_application(query={
                'application_id': self.application.application_id
            }, update_value={
                'app_metadata': json.dumps(app_metadata),
                'training_status': json.dumps(training_status)
            })
        except Exception as e:
            logger.error('Failure while traing linear regression : ' + e.message)
