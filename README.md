# OpenAI Predict Verticals

## Project Overview

OpenAI Predict Verticals is a project designed to send API requests using OpenAI GPT models and compare the correctness of the responses. The primary use case involves analyzing video titles from over 50 YouTube channels, each with 10 video titles, to identify the best prompt and system message for generating accurate responses. This project is also adaptable to various other use cases, working with multiple datasets or datasets from different topics.

## Execution Steps

### Step 1: Choose Your Datasets
1. Locate the `channel_list_1000.csv` file in the `data` folder. This serves as the example dataset for the project.
2. If you have a different use case, upload your dataset to the `data` folder.

### Step 2: Split Your Datasets
1. If your dataset is large, consider parsing it due to the single request limit.
2. For datasets with more than 1000 rows, the most convenient method is to split it into four parts.
3. Run the `split.py` file to create four different datasets with equal category distributions. These will be sent as four separate requests.

### Step 3: Find Your System and Prompt Messages
1. Identify the system and prompt messages you want to test.
2. Add the prompt messages as variables inside the `Prompt` object in the `prompt_messages.py` file.
3. Add the system messages to the `SystemMessages` object in the `system_messages.py` file.

### Step 4: Run the Script to Get Compared Results
1. Execute the `classification_per_method.py` file, modifying the prompt and system messages as specified.
2. You can change the gpt models as you want.
3. The script will send requests to OpenAI four times using the same prompt and system message for the four different datasets.
4. It will then combine the responses, compare the actual values with the GPT responses, create a new dataset, and generate a 'match' column indicating 'true' or 'false' based on the correctness of the results.
5. View all files (including unmerged) in the specified file directory, e.g., `output\data_scientist\simple\data_sc_simple_final_comparison.csv`.

### Step 5: Final Analysis
1. Open the `virtulaize_final_result` Jupyter notebook file.
2. Review the detailed analysis of the results.

## File Structure

- `data/`
  - `channel_list_1000.csv`
- `split.py`
- `prompt_messages.py`
- `system_messages.py`
- `classification_per_method.py`
- `output/`
  - `data_scientist/`
    - `simple/`
      - `data_sc_simple_final_comparison.csv`
- `virtulaize_final_result.ipynb`

## Conclusion

This project facilitates the evaluation of OpenAI GPT model responses by comparing them with actual values, helping you to determine the most effective prompt and system message for various datasets. Use the detailed analysis to refine your approach and improve the accuracy of the results.
