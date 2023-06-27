from abc import ABC, abstractmethod
from typing import List, Dict, Optional
from context import context, context_builder

class ABS_Model(ABC):
    @abstractmethod
    def __init__(self):
        """
        Create a new instance of ContextBuilder.

        Returns:
            ContextBuilder: The new instance of ContextBuilder.
        """
        pass

    @abstractmethod
    def variable_names(self) -> None:
        """
        Set the names of the variables.

        Args:
            variable_names (List[str]): The list of variable names.
        """
        pass

    @abstractmethod
    def variable_descriptions(self) -> None:
        """
        Set the descriptions for each variable.

        Args:
            variable_descriptions (Optional[Dict[str, str]]): A dictionary mapping variable names to their descriptions.
        """
        pass

    @abstractmethod
    def variable_relationships(self) -> None:
        """
        Set the relationships between variables.

        Args:
            variable_relationships (Optional[Dict[str, List[str]]]): A dictionary mapping each variable to a list of its related variables.
        """
        pass

    @abstractmethod
    def build(self) -> Context:
        """
        Build and return the Context object.

        Returns:
            Context: The populated Context object.
        """
        pass
