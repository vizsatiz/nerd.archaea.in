from api.common_helpers.common_constants import Algorithms
from api.services.linear_reg_service import LinearRegressionService


class ComputeEngineMapper:

    def __init__(self):
        pass

    @staticmethod
    def get_compute_engie(algorithm=None):
        if algorithm == Algorithms.LINEAR_REGRESSION:
            return LinearRegressionService.compute_linear_regression
        else:
            raise Exception('The algorithm has not yet been implemented')
