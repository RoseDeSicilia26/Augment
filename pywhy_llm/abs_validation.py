from abc import ABC, abstractmethod
from typing import List, Dict, Optional
from context import context, context_builder

class ABS_Validation(ABC):
    @abstractmethod
    def __init__(self):
        """
        Create class attributes to hold
        
        context object
        confounders list
        backdoor set
        frontdoor set
        instrumental variables

        Args:
            context (Context): Context object about the data
        """
        pass

    @abstractmethod
    def validated_variable_descriptions(self):
        """
        Validate the provided or suggested descriptions

        Args:
            context (Context): Context object about the data
        """
        pass

    @abstractmethod
    def validated_relationships(self):
        """
        Validate the suggested relationships

        Args:
            context (Context): Context object about the data
        """
        pass

    @abstractmethod
    def validated_confounders(self):
        """
        Validate the suggested confounders

        Args:
            context (Context): Context object about the data
        """
        pass

    @abstractmethod
    def validated_backdoor(self):
        """
        Validate the suggested backdoor set

        Args:
            context (Context): Context object about the data
        """
        pass

    @abstractmethod
    def validated_frontdoor(self):
        """
        Validate the suggested frontdoor set

        Args:
            context (Context): Context object about the data
        """
        pass

    @abstractmethod
    def validated_iv(self):
        """
        Validate the suggested instrumental variables

        Args:
            context (Context): Context object about the data
        """
        pass

    @abstractmethod
    def suggest_validation_code(self):
        """
        Suggest code to run validation analysis

        Args:

        """
        pass