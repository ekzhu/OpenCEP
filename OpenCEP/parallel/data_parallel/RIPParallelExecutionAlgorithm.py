from abc import ABC
from OpenCEP.parallel.data_parallel.DataParallelExecutionAlgorithm import DataParallelExecutionAlgorithm
import math
from OpenCEP.base.Pattern import Pattern
from OpenCEP.evaluation.EvaluationMechanismFactory import \
    EvaluationMechanismParameters, EvaluationMechanismFactory
from OpenCEP.base.DataFormatter import DataFormatter
from OpenCEP.base.PatternMatch import *
from OpenCEP.stream.Stream import *


class RIPParallelExecutionAlgorithm(DataParallelExecutionAlgorithm, ABC):
    """
    Implements the RIP algorithm.
    """
    def __init__(self, units_number, patterns: Pattern or List[Pattern],
                 eval_mechanism_params: EvaluationMechanismParameters,
                 platform, multiple):
        super().__init__(units_number - 1, patterns, eval_mechanism_params, platform)
        self.__eval_mechanism_params = eval_mechanism_params

    def eval(self, events: InputStream, matches: OutputStream, data_formatter: DataFormatter):
        raise NotImplementedError()
