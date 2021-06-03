"""
 Data parallel HyperCube algorithms
"""
from abc import ABC
from OpenCEP.parallel.data_parallel.DataParallelExecutionAlgorithm import DataParallelExecutionAlgorithm
import math
from OpenCEP.base.Pattern import Pattern
from OpenCEP.evaluation.EvaluationMechanismFactory import \
    EvaluationMechanismParameters
from OpenCEP.base.DataFormatter import DataFormatter
from OpenCEP.base.PatternMatch import *
from OpenCEP.stream.Stream import *


class HyperCubeParallelExecutionAlgorithm(DataParallelExecutionAlgorithm, ABC):
    """
    Implements the HyperCube algorithm.
    """
    def __init__(self, units_number, patterns: Pattern or List[Pattern],
                 eval_mechanism_params: EvaluationMechanismParameters, platform, attributes_dict: dict):
        super().__init__(units_number - 1, patterns, eval_mechanism_params, platform)
        self.__attributes_dict = attributes_dict

    def eval(self, events: InputStream, matches: OutputStream, data_formatter: DataFormatter):
        raise NotImplementedError()
