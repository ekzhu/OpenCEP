from abc import ABC

from OpenCEP.parallel.ParallelExecutionParameters import ParallelExecutionParameters
from OpenCEP.parallel.PlatformFactory import PlatformFactory
from OpenCEP.parallel.manager.EvaluationManager import EvaluationManager


class ParallelEvaluationManager(EvaluationManager, ABC):
    """
    An abstract base class for all parallel evaluation managers.
    """
    def __init__(self, parallel_execution_params: ParallelExecutionParameters):
        self._platform = PlatformFactory.create_parallel_execution_platform(parallel_execution_params)
