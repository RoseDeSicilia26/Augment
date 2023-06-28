from typing import List, Dict, Set, Tuple, Protocol

class Identification_Protocol(Protocol):

    def suggest_backdoor(self,  variable_descriptions: Dict[str, str], variable_relationships: Dict[Tuple[str, str], str], confounders: Set[Tuple[str, str]]) -> Set[str]:
        """
        Suggest backdoor path

        Args:
            variable_descriptions Dict[str, str]: A dictionary mapping variable names to their descriptions.

            variable_relationships Dict[Tuple[str, str], str]: A dictionary where the keys are edges, where it's assumed that parent is first, child is second, and the values are an explanation for how their relationship occurs

            confounders Set[Tuple[str, str]]: Set of confounders along with a reasoning or explanation for how the confounding occurs

        Returns:
            backdoor_set Set[str]: set of varaibles in backdoor set
        """
        pass

    def suggest_frontdoor(self,  variable_descriptions: Dict[str, str], variable_relationships: Dict[Tuple[str, str], str], confounders: Set[Tuple[str, str]]) -> Set[str]:
        """
        Suggest frontdoor path

        Args:
            variable_descriptions Dict[str, str]: A dictionary mapping variable names to their descriptions.

            variable_relationships Dict[Tuple[str, str], str]: A dictionary where the keys are edges, where it's assumed that parent is first, child is second, and the values are an explanation for how their relationship occurs

            confounders Set[Tuple[str, str]]: Set of confounders along with a reasoning or explanation for how the confounding occurs

        Returns:
            frontdoor_set Set[str]: set of varaibles in frontdoor set
        """
        pass

    def suggest_iv(self,  variable_descriptions: Dict[str, str], variable_relationships: Dict[Tuple[str, str], str], confounders: Set[Tuple[str, str]]) -> Set[str]:
        """
        Suggest instrumental variables

        Args:
            variable_descriptions Dict[str, str]: A dictionary mapping variable names to their descriptions.

            variable_relationships Dict[Tuple[str, str], str]: A dictionary where the keys are edges, where it's assumed that parent is first, child is second, and the values are an explanation for how their relationship occurs

            confounders Set[Tuple[str, str]]: Set of confounders along with a reasoning or explanation for how the confounding occurs

        Returns:
            instrumental_variables Set[str]: set of varaibles in backdoor set
        """
        pass

    def suggest_analysis_code(self,  variable_descriptions: Dict[str, str], variable_relationships: Set[Tuple[str, str]], confounders: Set[Tuple[str, str]]) -> str:
        """
        Suggest code to run identification analysis

        Args:
            backdoor_set Set[str]: set of varaibles in backdoor set

            frontdoor_set Set[str]: set of varaibles in frontdoor set

            set of instrumental variables Set[str]: set of varaibles in backdoor set

        Returns:
            code str: code to run analysis
        """
        pass