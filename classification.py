from openai import OpenAI
import pandas as pd
import numpy as np
import json
import os
from prompt_messages import Prompts

# COMPLETIONS_MODEL = "gpt-3.5-turbo-1106"
COMPLETIONS_MODEL = 'gpt-4-1106-preview'

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

system_message = """You are a helpful assistant that classifies multiple video titles into one category.
    The video title will be separated by a new line character.
    The categories are: 'Auto & Vehicles', 'Sports Editorial Content', 'Entertainment', 'Kids Content', 'Family', 'News, Politics, & Information', 'Gaming', 
    'Tech', 'Education & Science', 'Food & Drinks', 'Corporate Channels', 'Lifestyle & Hobbies', 'Health & Fitness'
"""

def classify_channel(channel_id, prompt):
    videos_df = channel_list[channel_list['channel_id']==channel_id]
    video_titles = videos_df[['video_title']].to_csv(index=False)
    final_prompt = prompt(video_titles)

    completion_response = request_completion(system_message, final_prompt)
    completion_response = completion_response[0].message.content

    return completion_response

if __name__ == '__main__':    
    channel_list = pd.read_csv('data/channel_list_1000.csv')

    channel_df = channel_list[['channel_id', 'vertical']].drop_duplicates()

    channel_df['predicted_vertical'] = channel_df['channel_id'].apply(lambda channel_id: classify_channel(channel_id, Prompts.certainty_one_shot_prompt))

    channel_df.to_csv('output/certainty_one_shot_prompt_output.csv')
    