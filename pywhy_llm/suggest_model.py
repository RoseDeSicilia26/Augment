from typing import List, Dict, Set, Tuple, Protocol
from _model import Model_Protocol
import guidance
import re

class Suggest_Model(Model_Protocol):
    
    def suggest_descriptions(self, variable_names: List[str], llm: guidance.llms) -> Dict[str, str]:
        
        return self.generate_descriptions(variable_names, llm)


    def generate_descriptions(self, variable_names: List[str], llm: guidance.llms) -> Dict[str, str]:

        generate_description = guidance(    
            '''
            {{#system~}}
            You are a helpful assistant with expertise in causal inference. You are helping me better understand a dataset by providing me with a description of the variables. I will provide you with the name of a column variable within the dataset and you will provide a description for that column variable. Let's take it step by step to make sure the description is relevant, succinct, and clear. 
            Here is an example:
            ------------------------------------------
            variable_name
            description
            ------------------------------------------
            age
            The age of the patient in years. 
            {{~/system}}

            {{#user~}}
            {{variable}}
            {{~/user}}
                        
            {{#assistant~}}
            {{gen 'description' temperature=0.7}}
            {{~/assistant}}
            ''')

        variables_and_descriptions : Dict[str, str] = {}

        for variable_name in variable_names:

            output = generate_description(variable_name=variable_name, llm=llm)

            variables_and_descriptions[variable_name] = output['description']
    
        return variables_and_descriptions


    def suggest_confounders(self, variables_and_descriptions: Dict[str, str], llm: guidance.llms, treatment: str, outcome: str) -> Set[Tuple[str, str]]:

        return self.generate_confounders(variables_and_descriptions, llm, treatment, outcome)

    
    def generate_confounders(self, variables_and_descriptions: Dict[str, str], llm: guidance.llms, treatment: str, outcome: str) -> Dict[str, str]:

        all_vars_but_t_o = ', '.join(f'{key}: {value}' for key, value in variables_and_descriptions.items() if key not in [treatment, outcome])

        generate_confounders = guidance(
                
            '''
            {{#system~}}
            You are a helpful assistant with expertise in causal inference. I will provide you with context about the dataset by showing you all the columns and their associated descriptions. You will then go varaible by variable and explain whether the variable is confounding the relationship between the treatment and the outcome and categorize it appropriately. Where a confounder is a common cause of both the treatment and the outcome. In essence, a confounder directly causes both the treatment and the outcome. 
            ------------------------------------------
            Input:
                treatment
                    treatment_variable_name
                    description of treatment_variable

                outcome
                    outcome_variable_name
                    description of outcome_variable

                Dataset schema with descriptions
                    name_of_first_variable: Description of first variable.
                    name_of_second_variable: Description of second variable.
                    ...
                    name_of_nth_confounder: Description of nth variable.          

            Output: 
                <confounder>name_of_first_variable</confounder>: <explanation>Description of first variable.</explanation>
                <category>True or false</category>

                <confounder>name_of_second_variable</confounder>: <explanation>Description of second variable.</explanation>
                <category>True or false</category>

                ...

                <confounder>name_of_nth_confounder</confounder>: <explanation>Description of nth variable. 
                Explanation for why and how the selected variable is or is not a confounder.</explanation>
                <category>True or false</category>
            {{~/system}}

            {{#user~}}
            Treatment: {{treatment}}
            Outcome: {{outcome}}

            Dataset schema with descriptions
            {{variables_and_descriptions}}

            What variables directly influence both the treatment and the outcome?
            {{~/user}}

            {{#assistant~}}
            {{gen 'confounder_explanation' temperature=1 max_tokens=2000}}
            {{~/assistant}} 
            ''')
        
        output = generate_confounders(
        treatment=treatment, 
        outcome=outcome, 
        variables_and_descriptions=all_vars_but_t_o,
        llm=llm)

        # Find all occurrences of confounders, explanations, and categories
        confounders = re.findall(r'<confounder>(.*?)</confounder>', output['confounder_explanation'])
        explanations = re.findall(r'<explanation>(.*?)</explanation>', output['confounder_explanation'])
        categories = re.findall(r'<category>(.*?)</category>', output['confounder_explanation'])

        # Combine confounders, explanations, and categories into a dictionary
        suggested_confounders = {confounder: explanation
               for confounder, explanation, category in zip(confounders, explanations, categories)
               if category == 'True'}

        return suggested_confounders
    
    
    def suggest_variable_relationships(self, variables_and_descriptions: Dict[str, str], treatment: str, outcome: str, llm: guidance.llms, confounders_and_reasoning: Dict[str, str] = None) -> Dict[Tuple[str, str], str]:

        return self.generate_variable_relationships(variables_and_descriptions, confounders_and_reasoning, treatment, outcome, llm)


    def generate_variable_relationships(self, variables_and_descriptions: Dict[str, str], treatment: str, outcome: str, llm: guidance.llms, confounders_and_reasoning: Dict[str, str] = None) -> Dict[Tuple[str, str], str]:

        relevant_variables_and_descriptions = {key: value for key, value in variables_and_descriptions.items() if key == treatment or key == outcome or key in confounders_and_reasoning.keys()}


        generate_relationships = guidance('''
        {{#system~}}
        You are a helpful assistant with expertise in causal inference. You will assist me in discovering the causal graph representing my dataset. 
        I will provide you with context about the dataset by showing you the the columns along with their associated descriptions.  
        I will then go variable by variable and ask you to identify its children (should it have any), where a child is another variable that is directly caused by the specified variable. Show your work and take it step by step to make sure that the variables you identify are indeed children of the specified variable.
        ------------------------------------------
        Input:

            Dataset schema with descriptions
                name_of_first_variable: Description of first variable.
                name_of_second_variable: Description of second variable.
                ...
                name_of_nth_confounder: Description of nth variable.     

            Selected variable     
            Does selected_variable have any children present in the dataset?

        Output (if the selected variable has (a) child(dren) present in the dataset):
            <child>child_1</child><explanation>Explanation for why and how this varaible is child of the selected variable.</explanation>
            ...
            <child>child_n</child><explanation>Explanation for why and how this varaible is child of the selected variable.</explanation>

        Output (if the selected variable does not have a child present in the dataset): 
            <null>  
        {{~/system}}

        {{#user~}}
        Dataset schema with descriptions
        {{variables_and_descriptions}}

        Does {{variable}} have any children present in the dataset?  
        {{~/user}}

        {{#assistant~}}
        {{gen 'children' temperature=0.7}}
        {{~/assistant}} 
        
        ''')

        relationships_and_descriptions : Dict[Tuple[str, str], str] = []

        for var, desc in relevant_variables_and_descriptions.items():
            output = generate_relationships(variables_and_descriptions=relevant_variables_and_descriptions, variable=var, llm=llm)

            children = re.findall(r'<child>(.*?)</child>', output['children'])
            explanations = re.findall(r'<explanation>(.*?)</explanation>', output['children'])

            for i in range(len(children)):
                relationships_and_descriptions[(var, children[i])] = explanations[i]


        return relationships_and_descriptions

    
