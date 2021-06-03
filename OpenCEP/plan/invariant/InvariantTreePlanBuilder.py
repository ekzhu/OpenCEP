from abc import ABC
from typing import Dict

from OpenCEP.base.Pattern import Pattern
from OpenCEP.plan.TreePlan import TreePlan, TreePlanLeafNode
from OpenCEP.plan.TreePlanBuilder import TreePlanBuilder


class InvariantTreePlanBuilder(TreePlanBuilder, ABC):
    """
    Base class for an invariant tree plan builders
    """
    def build_tree_plan(self, pattern: Pattern, statistics: Dict):
        """
        Creates a tree-based evaluation plan for the given pattern.
        """
        # as of now, the invariant-based method can only work on composite non-nested patterns
        leaves = [TreePlanLeafNode(i) for i in range(len(pattern.full_structure.args))]
        tree_topology, invariants = self._create_tree_topology(pattern, statistics, leaves)
        return TreePlan(tree_topology), invariants
