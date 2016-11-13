from api.common_helpers.common_constants import Algorithms
from api.services.linear_reg_service import LinearRegressionService


class TrainingEngineMapper:

    def __init__(self):
        pass

    @staticmethod
    def get_training_engine(algorithm=None):
        if algorithm == Algorithms.LINEAR_REGRESSION:
            return LinearRegressionService.train_linear_regression
        else:
            raise Exception('The algorithm has not yet been implemented')
