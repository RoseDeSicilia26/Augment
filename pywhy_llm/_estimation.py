from typing import List, Dict, Set, Tuple, Protocol

class Estimation_Protocol(Protocol):

    def suggest_estimation_code(self) -> str:
        """
        Suggest code to run the causal effect analysis

        Returns:
            code str: suggested code for running estimation
        """
        pass