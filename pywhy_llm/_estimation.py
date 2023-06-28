from typing import Protocol
import guidance

class Estimation_Protocol(Protocol):
    def suggest_estimation_code(self, llm: guidance.llms) -> str:
        """
        Suggest code to run the causal effect analysis

        Returns:
            code str: suggested code for running estimation
        """
        pass