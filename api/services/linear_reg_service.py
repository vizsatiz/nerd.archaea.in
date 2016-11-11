import pickle
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
        app_metadata = application.app_metadata
        weights = app_metadata['weights']
        lr_object = pickle.loads(weights)
        lr = SciLearnModelPersistenceHelper.initialize_model_with_state(lr_object)
        lr_trainer = LinearRegressionTrainer(lr)
        prediction = lr_trainer.predict(data)
        return prediction

    @staticmethod
    def train_linear_regression(application=None, training_data=None):
        if application is None:
            raise Exception('Unknown application')
        if training_data is None:
            raise Exception('No data found for training')
        app_metadata = application.app_metadata
        weights = app_metadata['weights']
        lr_object = pickle.loads(weights)
        lr = SciLearnModelPersistenceHelper.initialize_model_with_state(lr_object)
        lr_trainer = LinearRegressionTrainer(lr)
