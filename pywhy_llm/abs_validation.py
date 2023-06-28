from typing import List, Dict, Set, Tuple, Protocol

class Validation_Protocol(Protocol):

    def validate_variable_descriptions(self, variable_descriptions: Dict[str, str]) -> Dict[str, str]:
        """
        Validate the descriptions for each variable.

        Args:
            variable_descriptions Dict[str, str]: A dictionary mapping variable names to their descriptions.

        Returns:
            variable_descriptions Dict[str, str]: validated dictionary mapping variable names to their descriptions.
        """
        pass

    def validate_relationships(self, variable_descriptions: Dict[str, str], variable_relationships: Dict[Tuple[str, str], str]) -> Set[Tuple[str, str]]:
        """
        Validate the suggested relationships

        Args:
            variable_descriptions Dict[str, str]: A dictionary mapping variable names to their descriptions.

            variable_relationships Dict[Tuple[str, str], str]: A set of edges with an explanation for how their relationship occurs, where it's assumed that parent is first, child is second, and explanation is third

        Returns:
            variable_relationships Set[Tuple[str, str, str]]: validated relationships
        """
        pass

    def validate_confounders(self, variable_descriptions: Dict[str, str], variable_relationships: Dict[Tuple[str, str], str], confounders: Set[Tuple[str, str]]) -> Set[Tuple[str, str]]:
        """
        Validate set of confounders

        Args:
            variable_descriptions Dict[str, str]: A dictionary mapping variable names to their descriptions.

            variable_relationships Dict[Tuple[str, str], str]: A set of edges with an explanation for how their relationship occurs, where it's assumed that parent is first, child is second, and explanation is third

            confounders Set[Tuple[str, str]]: Set of confounders along with a reasoning or explanation for how the confounding occurs

        Returns:
            confounders Set[Tuple[str, str]]: validated set of confounders
        """
        pass

    def validate_backdoor(self,  variable_descriptions: Dict[str, str], variable_relationships: Dict[Tuple[str, str], str], confounders: Set[Tuple[str, str]], backdoor_set: Set[str]) -> Set[str]:
        """
        Validate backdoor path

        Args:
            variable_descriptions Dict[str, str]: A dictionary mapping variable names to their descriptions.

            variable_relationships Dict[Tuple[str, str], str]: A set of edges with an explanation for how their relationship occurs, where it's assumed that parent is first, child is second, and explanation is third

            confounders Set[Tuple[str, str]]: Set of confounders along with a reasoning or explanation for how the confounding occurs
        
            backdoor_set Set[str]: set of varaibles in backdoor set

        Returns:
            backdoor_set Set[str]: validated backdoor set
        """
        pass

    def validate_frontdoor(self,  variable_descriptions: Dict[str, str], variable_relationships: Dict[Tuple[str, str], str], confounders: Set[Tuple[str, str]], frontdoor_set: Set[str]) -> Set[str]:
        """
        Validate frontdoor set

        Args:
            variable_descriptions Dict[str, str]: A dictionary mapping variable names to their descriptions.

            variable_relationships Dict[Tuple[str, str], str]: A set of edges with an explanation for how their relationship occurs, where it's assumed that parent is first, child is second, and explanation is third

            confounders Set[Tuple[str, str]]: Set of confounders along with a reasoning or explanation for how the confounding occurs

            frontdoor_set Set[str]: set of varaibles in frontdoor set

        Returns:
            frontdoor_set Set[str]: validated frontdoor set
        """
        pass

    def validate_iv(self,  variable_descriptions: Dict[str, str], variable_relationships: Dict[Tuple[str, str], str], confounders: Set[Tuple[str, str]], instrumental_variables: Set[str]) -> Set[str]:
        """
        Suggest instrumental variables

        Args:
            variable_descriptions Dict[str, str]: A dictionary mapping variable names to their descriptions.

            variable_relationships Dict[Tuple[str, str], str]: A set of edges with an explanation for how their relationship occurs, where it's assumed that parent is first, child is second, and explanation is third

            confounders Set[Tuple[str, str]]: Set of confounders along with a reasoning or explanation for how the confounding occurs
        
            set of instrumental variables Set[str]: set of varaibles in backdoor set

        Returns:
            set of instrumental variables Set[str]: set of varaibles in backdoor set
        """
        pass

    def suggest_validation_code(self) -> str:
        """
        Suggest code to run validation analysis

        Returns:
            code str: code to run validation

        """
        pass