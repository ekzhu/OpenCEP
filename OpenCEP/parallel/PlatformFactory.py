"""
This file contains the class responsible for parallel execution platform initialization.
"""
from OpenCEP.parallel.ParallelExecutionParameters import ParallelExecutionParameters
from OpenCEP.parallel.ParallelExecutionPlatforms import ParallelExecutionPlatforms
from OpenCEP.parallel.platform.ThreadingParallelExecutionPlatform import \
    ThreadingParallelExecutionPlatform


class PlatformFactory:
    """
    Creates a parallel execution platform given its specification.
    """
    @staticmethod
    def create_parallel_execution_platform(parallel_execution_params: ParallelExecutionParameters):
        if parallel_execution_params is None:
            parallel_execution_params = ParallelExecutionParameters()
        if parallel_execution_params.platform == ParallelExecutionPlatforms.THREADING:
            return ThreadingParallelExecutionPlatform()
        raise Exception("Unknown parallel execution platform: %s" % (parallel_execution_params.platform,))
