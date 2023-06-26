import abc
import networkx as nx
import pandas as pd


class ABSModel(abc.ABC):

    strategy: dict ={
        'one_shot':1,
        'cot':2,
        'tot':3
    }
        
    '''
    strategy - ToT, CoT, One Shot, multiple outputs (for user validation)
    select llm prompt strategy

    causal_discovery - 

    validation - auto, human  
    human validation procedure, human in the loop
    '''
    @abc.abstractmethod
    def __init__(
        self, 
        strategy: int = strategy['one_shot'], auto_validation: bool = True):
        pass

    '''
    load in the data from the user (pandas dataframe)

    calls suggest_descriptions for missing descriptions
    '''
    @abc.abstractmethod
    def init_schema(
        self,   
        schema: pd.DataFrame) -> pd.DataFrame:
        pass

    '''
    generates suggestion(s) with llm
    '''
    @abc.abstractmethod
    def suggest_descriptions(
        self,
        schema: pd.DataFrame) -> pd.DataFrame:
        pass

    '''
    load in graph from the user

    calls suggest_graph() to perform causal discovery

    calls 
    '''
    @abc.abstractmethod
    def init_graph(
        self, 
        graph: nx.classes.digraph.DiGraph):
        pass

    '''
    called if user would like to do causal discovery

    different ways of prompting for relationships
    (1) pairwise relationship (two elements passed)
    (2) parent relationships (one element)
    (3) child relationships (one element)
    '''
    @abc.abstractmethod
    def suggest_graph(self):
        pass

    '''
    llm performs pairwise analysis of relationships and suggest pairwise causal relationships
    '''
    @abc.abstractmethod
    def suggest_relationships(self):
        pass

    '''
    llm performs causal analysis on treatment and outcome and suggests causal parents
    '''
    @abc.abstractmethod
    def suggest_confounders(self):
        pass


    '''
    requests the user to validate the description(s) suggested by the llm
    '''
    @abc.abstractmethod
    def validate_descriptions(self):
        pass

    '''
    requests the user to validate the relationship(s) suggested by the llm

    calls validate_pairwise_relationships
    '''
    @abc.abstractmethod
    def validate_graph(self):
        pass

    '''
    requests the user to validate the pair wise 
    '''
    @abc.abstractmethod
    def validate_pairwise_relationship(self):
        pass

    @abc.abstractmethod
    def validate_confounders(self):
        pass

    '''
    display graph 
    full (discovered) graph or just confounders
    '''
    @abc.abstractmethod
    def validate_confounders(self):
        pass

