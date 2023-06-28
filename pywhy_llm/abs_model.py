from abc import ABC, abstractmethod
from typing import List, Dict, Optional
from context import context, context_builder

class ABS_Model(ABC):
    @staticmethod
    @abstractmethod
    def suggest_variable_descriptions(self) -> None:
        """
        Suggest the descriptions for each variable.

        Args:
            variable_descriptions (Optional[Dict[str, str]]): A dictionary mapping variable names to their descriptions.
        """
        pass

    @staticmethod
    @abstractmethod
    def suggest_variable_relationships(self) -> None:
        """
        Suggest the relationships between variables.

        Args:
            variable_relationships (Optional[Dict[str, List[str]]]): A dictionary mapping each variable to a list of its related variables.
        """
        pass

    @staticmethod   
    @abstractmethod
    def suggest_confounders(self):
        """
        Suggest confounders

        Args:
            context (Context): Context object about the data
        """
        pass
