from openai import OpenAI
import pandas as pd
import time
import matplotlib.patheffects as path_effects
import matplotlib.pyplot as plt

start = time.time()

# Set your OpenAI API key
# client 

def describe_dataset(df):
    df_string = df[['month', 'views']].to_csv(index=False, lineterminator=' ', sep=' ')

    # Define the prompt for describing
    first_month = df['month'].min()
    last_month = df['month'].max()
    prompt = f"""
    Explain the dataframe in two short sentences. Have views increased or decreased between {first_month} and {last_month}?

    Example 1: The channel performance has been increasing. The views are higher in August 2023 compared to January 2023.

    Example 2: The channel performance is decreasing. The best month was June 2023, and the views decreased from January to September.
    
    Dataframe: {df_string}
    """

    chat_completion = client.chat.completions.create(
    messages=[
            {"role": "system", "content": "You are a helpful assistant that explains a youtube channels performance from a dataframe. The columns are month and views."},
            {"role": "user", "content": prompt}
        ],
        # model="gpt-3.5-turbo",
        # model = 'gpt-4-1106-preview',
        model = 'gpt-3.5-turbo-1106',
        max_tokens=50
    )

    # Extract and return the translated text
    description = chat_completion.choices[0].message.content.strip()
    return description

# Example usage
# load dataset
# dataset = pd.read_csv('data.csv')
# dataset = dataset[dataset['month']>='2023-01-01']
# dataset = dataset[dataset['channel_name']=='Freshtorge']
description = describe_dataset(dataset)
description = description.replace('.', '.\n')
description = description.replace(',', ',\n')
# channel_perf = describe_dataset()
# print(f"Channel: Freshtorge")
# print(f"{description}")
# print(time.time() - start)


fig = plt.figure(figsize=(10, 3))
text = fig.text(0.5, 0.5, description,
                ha='center', va='center', size=12)
text.set_path_effects([path_effects.Normal()])
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.show()