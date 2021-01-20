"""Module contains code for current building context, including dags built-up"""
from typing import Dict

from airflow import DAG


class DagBuildContext:
    """
    Used to store current build up dags, currently only for subdag reference
    """

    def __init__(self):
        self._context_built_dags: Dict[str, DAG] = {}

    def add_dag(self, dag: DAG) -> None:
        """
        add built dag to context
        """
        self._context_built_dags[dag.dag_id] = dag

    def get_all_dags(self):
        """
        return all build dags, list of DAG
        """
        return self._context_built_dags.values()

    def get_all_dag_ids(self):
        """
        return all built dag ids, list of str
        """
        return self._context_built_dags.keys()

    def find_dag(self, dag_id: str):
        """
        Find a built-up dag for specific dag_id, if not found, return None
        """
        return self._context_built_dags.get(dag_id)
