from abc import ABC, abstractmethod
from typing import List, Dict, Optional, Set
from context import context, context_builder

class ABS_Identification(ABC):
    @staticmethod
    @abstractmethod
    def suggest_backdoor(self):
        """
        Suggest backdoor path

        Args:
            context (Context): Context object about the data
        """
        pass

    @staticmethod
    @abstractmethod
    def suggest_frontdoor(self):
        """
        Suggest frontdoor path

        Args:
            context (Context): Context object about the data
        """
        pass

    @staticmethod
    @abstractmethod
    def suggest_iv(self):
        """
        Suggest instrumental variables

        Args:
            context (Context): Context object about the data
        """
        pass

    @staticmethod
    @abstractmethod
    def suggest_analysis_code(self):
        """
        Suggest code to run identification analysis

        Args:

        """
        pass