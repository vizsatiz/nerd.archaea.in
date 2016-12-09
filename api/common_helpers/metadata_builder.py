from pickle import dumps
from nerd_log_helper import logger
from api.common_helpers.common_constants import Algorithms
from machine_learning.model_persistance.sci_learn_model import SciLearnModelPersistenceHelper
from machine_learning.linear_regression.lin_reg_builder import LinearRegressionBuilder


class MetadataBuilder:

    def __init__(self):
        pass

    @staticmethod
    def build_metadata(algorithm=None, parameters=None):
        if algorithm == Algorithms.LINEAR_REGRESSION:
            try:
                parameters = {
                    'fit_intercept': parameters['fit_intercept'],
                    'normalize': parameters['normalize'],
                    'copy_X': parameters['copy_X'],
                    'n_jobs': parameters['n_jobs']
                }
            except Exception as e:
                logger.error('The parameters that are passed for creating LR is incorrect : ' + e.message)
                raise Exception('The parameters are not right.')
            linear_reg = LinearRegressionBuilder(parameters).build()
            model_object = SciLearnModelPersistenceHelper.get_model_state(linear_reg)
            weights = dumps(model_object)
        else:
            raise Exception('Unimplemented algorithm')
        return {
            'weights': weights,
            'parameters': parameters
        }