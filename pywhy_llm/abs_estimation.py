from abc import ABC, abstractmethod
from typing import List, Dict, Optional
from context import context, context_builder

class ABS_Estimation(ABC):

    @abstractmethod
    def suggest_estimation_code(self):
        """
        Suggest code to run the causal effect analysis

        Args:
            
        """
        pass