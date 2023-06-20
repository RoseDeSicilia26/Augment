# Augment

The Augment class is designed to assist in processing and augmenting schema descriptions of a dataset and identifying potential confounding variables in a causal relationship. It makes use of the GPT-4 language model from OpenAI for generating descriptions and identifying relationships.

## Getting Started
First, you need to have the following Python libraries installed in your environment and an api key to OpenAI API:

pandas

openai

os

re

ipywidgets

You also need to set your OpenAI API key in the script

```
openai.api_key = 'api_key'
```

## Features
The main features of the Augment class include:

Loading data from a text file or pandas DataFrame

Text file or DataFrame containing your dataset can be loaded into the Augment class using the load_text_file() or load_data() methods.

Augmenting descriptions

The augment_descriptions() method is used to generate descriptions for each column in your dataset. You can choose whether to automatically select the first generated description, or manually select from a list of generated descriptions.

Identifying confounding variables

The augment_relationships() method identifies potential confounding variables in a specified causal relationship within your dataset. You can choose whether to automatically accept all identified confounders, or manually validate each one.

## Basic Usage
```
from augment import Augment

# Create an instance of the Augment class
augmenter = Augment()

# Load a text file into the Augment class
augmenter.load_text_file('your_file.txt')

# Generate and validate new descriptions
augmenter.augment_descriptions(auto=True)

# Generate and validate confounding relationships
augmenter.augment_relationships('treatment', 'outcome', auto=True)
```
