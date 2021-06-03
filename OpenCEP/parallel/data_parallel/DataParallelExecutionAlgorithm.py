from abc import ABC
from OpenCEP.base.Pattern import Pattern
from OpenCEP.evaluation.EvaluationMechanismFactory import \
    EvaluationMechanismParameters, EvaluationMechanismFactory
from OpenCEP.base.DataFormatter import DataFormatter
from OpenCEP.base.PatternMatch import *
from OpenCEP.parallel.platform.ParallelExecutionPlatform import ParallelExecutionPlatform
from OpenCEP.stream.Stream import *


class DataParallelExecutionAlgorithm(ABC):
    """
    An abstract base class for all data parallel evaluation algorithms.
    """
    def __init__(self, units_number, patterns: Pattern or List[Pattern],
                 eval_mechanism_params: EvaluationMechanismParameters, platform: ParallelExecutionPlatform):
        raise NotImplementedError()

    def eval(self, events: InputStream, matches: OutputStream, data_formatter: DataFormatter):
        """
        Activates the actual parallel algorithm.
        """
        raise NotImplementedError()

    def get_structure_summary(self):
        raise NotImplementedError()
