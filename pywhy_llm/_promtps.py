from typing import Dict, List

class Promtps():

    _suggest_descriptions_promtp: List[str] = [] # technique : prompt[]
    _suggest_relationships_promtp: List[str] = [] # technique : prompt[]
    _suggest_confounders_promtp: List[str] = [] # technique : prompt[]    

    """
    {{#system~}}
    System 
    You are an interdisciplinary researcher with expertise in {field} and causal inference. You are helping a colleague who is new to the field better understand a dataset by adding descriptions to all the variables in a dataset. Your descriptions should be short and concise, but still provide enough context and relevant information. Your colleague will provide you with some information about the dataset and ask that you provide a description for each variable.
    {{~/system}}

    {{#user~}}
    I am working with a dataset that contains information about {field}. {dataset_description}. Here are all the variables in the dataset. Please provide a description for variable {{variable}}. 
    {{~/user}}
             
    {{#assistant~}}
    {{gen 'variable_description' temperature=1 max_tokens=300}}
    {{~/assistant}}
    """

    def suggest_descriptions_promtp(self) -> str:
        


        pass

    def suggest_relationships_promtp(self):

        pass

    def suggest_confounders_promtp(self):

        pass

