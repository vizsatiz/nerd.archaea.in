from api.services.compute_service import ComputeEngineMapper

class LinearRegressionService:

    def __init__(self):
        pass

    @staticmethod
    def compute_linear_regression(application=None, data=None):
        if application is None:
            raise Exception('Unknown application')
        if data is None:
            raise Exception('No data found to do the computation')

    @staticmethod
    def train_linear_regression(application=None, training_data=None):
        pass





