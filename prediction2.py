from openai import OpenAI
import pandas as pd


def gpt_prediction(df):
    df_text = df[['video_title']].to_csv()
    df
    prompt = f"""
        According to the CSV identify which language the text is in one by one, for each index. 
        I want you to guess the language based on the Text.
        Do it this entire dataframe and give me response according to this examples below.
        I want to see all the results
        Example 1: 1: en
        Example 2: 5: de
        CSV: {df_text}
    """
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that detect the language in the text from a dataframe. In this dataframe, tell me what language they are in. Colums are: index, text"},
            {"role": "user", "content": prompt},
        ]
    )
    prediction = completion.choices
    return prediction

if __name__ == '__main__':
    # Set your OpenAI API key
    # client
    df = pd.read_csv('analitcs_videos.csv')
    print(df)
    