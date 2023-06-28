from typing import List, Dict, Set, Tuple, Protocol

class Model_Protocol(Protocol):
    def suggest_variable_descriptions(self,  variable_names: List[str]) -> Dict[str, str]:
        """
        Suggest the descriptions for each variable.

        Args:
            variable_names List[str]: List of variable names

        Returns:
            variable_descriptions Dict[str, str]: A dictionary mapping variable names to their descriptions.
        """
        pass

    def suggest_variable_relationships(self, variable_descriptions: Dict[str, str]) -> Set[Tuple[str, str, str]]:
        """
        Suggest the relationships between variables.

        Args:
            variable_descriptions Dict[str, str]: A dictionary mapping variable names to their descriptions.
        
        Returns:
            variable_relationships Set[Tuple[str, str, str]]: A set of edges with an explanation for how their relationship occurs, where it's assumed that parent is first, child is second, and explanation is third

        
        """
        pass

    def suggest_confounders(self, variable_descriptions: Dict[str, str], variable_relationships: Set[Tuple[str, str]]) -> Set[Tuple[str, str]]:
        """
        Suggest confounders

        Args:
            variable_descriptions Dict[str, str]: A dictionary mapping variable names to their descriptions.

            variable_relationships Set[Tuple[str, str]]: A set of edges in the form of tuples, where it's assumed that parent is first, child is second

        Returns:
            confounders Set[Tuple[str, str]]: Set of confounders along with a reasoning or explanation for how the confounding occurs
        """
        pass