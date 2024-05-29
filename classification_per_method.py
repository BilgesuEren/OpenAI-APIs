from openai import OpenAI
import pandas as pd
from prompt_messages import Prompts
from system_messages import SystemMessages

# COMPLETIONS_MODEL = "gpt-3.5-turbo-1106"
# Initialize the OpenAI client
COMPLETIONS_MODEL = 'gpt-4-0125-preview'
# client


def request_completion(system_message, prompt):
    completion_response = client.chat.completions.create(
        model=COMPLETIONS_MODEL,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt},
        ]
    )
    classification = completion_response.choices
    return classification

def classify_channel(channel_list, channel_id, system_message, prompt_func):
    videos_df = channel_list[channel_list['channel_id'] == channel_id]
    video_titles = ", ".join(videos_df['video_title'].tolist())
    final_prompt = prompt_func(video_titles)
    completion_response = request_completion(system_message, final_prompt)
    completion_response = completion_response[0].message.content
    return completion_response

def run_classification(channel_list, system_message, prompt_func, output_file):
    channel_df = channel_list[['channel_id', 'vertical']].drop_duplicates()
    channel_df['predicted_vertical'] = channel_df['channel_id'].apply(lambda channel_id: classify_channel(channel_list, channel_id, system_message, prompt_func))
    channel_df.to_csv(output_file, index=False)

def process_all_datasets(system_message, prompt_func, output_prefix, system_message_path):
    datasets = ['dataset_1.csv', 'dataset_2.csv', 'dataset_3.csv', 'dataset_4.csv']
    output_files = []

    for i, dataset in enumerate(datasets):
        channel_list = pd.read_csv(f'datasets/{dataset}')
        output_file = f'output/{system_message_path}/{output_prefix}/{output_prefix}_output_{i + 1}.csv'
        run_classification(channel_list, system_message, prompt_func, output_file)
        output_files.append(output_file)
    
    # Combine all output files
    combined_df = pd.concat([pd.read_csv(file) for file in output_files])
    combined_df.to_csv(f'output/{system_message_path}/{output_prefix}/{output_prefix}_combined_results.csv', index=False)

def compare_results(output_prefix, system_message_path):
    combined_df = pd.read_csv(f'output/{system_message_path}/{output_prefix}/{output_prefix}_combined_results.csv')
    combined_df['match'] = combined_df.apply(lambda row: row['vertical'] == row['predicted_vertical'], axis=1)
    accuracy = combined_df['match'].mean()
    combined_df.to_csv(f'output/{system_message_path}/{output_prefix}/{output_prefix}_final_comparison.csv', index=False)
    print(f"Accuracy: {accuracy * 100:.2f}%")

if __name__ == '__main__':
    system_message = SystemMessages.data_scientist
    prompt_func = Prompts.simple_zero_shot_prompt

    process_all_datasets(system_message, prompt_func, 'one_shot', 'data_scientist')
    compare_results('one_shot', 'data_scientist')