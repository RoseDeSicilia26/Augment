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

    def suggest_variable_relationships(self, variable_descriptions: Dict[str, str]) -> Dict[Tuple[str, str], str]:
        """
        Suggest the relationships between variables.

        Args:
            variable_descriptions Dict[str, str]: A dictionary mapping variable names to their descriptions.
        
        Returns:
            variable_relationships Dict[Tuple[str, str], str]: A dictionary where the keys are edges, where it's assumed that parent is first, child is second, and the values are an explanation for how their relationship occurs        
        """
        pass

    def suggest_confounders(self, variable_descriptions: Dict[str, str], variable_relationships: Dict[Tuple[str, str], str]) -> Set[Tuple[str, str]]:
        """
        Suggest confounders

        Args:
            variable_descriptions Dict[str, str]: A dictionary mapping variable names to their descriptions.

            variable_relationships Dict[Tuple[str, str], str]: A dictionary where the keys are edges, where it's assumed that parent is first, child is second, and the values are an explanation for how their relationship occurs     

        Returns:
            confounders Set[Tuple[str, str]]: Set of confounders along with a reasoning or explanation for how the confounding occurs
        """
        pass