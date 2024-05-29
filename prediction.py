from openai import OpenAI
import pandas as pd


def guess_language(df):
    df_text = df[['Text']].to_csv()
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
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that detect the language in the text from a dataframe. In this dataframe, tell me what language they are in. Colums are: index, text"},
            {"role": "user", "content": prompt},
        ]
    )
    guess = completion.choices
    return guess

def create_df_from_gpt(data):
    # takes a list, returns a DF
    language_list = []
    
    for entry in data:
        parts = entry.split(': ') # split the response for create df
        if len(parts) > 1:
            language_list.append([int(parts[0]), parts[1]])
            
    # df_gpt = pd.DataFrame({'gpt language': language_list})
    df_gpt = pd.DataFrame(language_list, columns=['index', 'lang'])
    df_gpt = df_gpt.set_index('index')
    return df_gpt
    
if __name__ == '__main__':
    # Set your OpenAI API key
    # client 
    df = pd.read_excel("ob.xlsx", sheet_name="TikTok")
    df.index.name = 'index'
    df.index = df.index + 2
    gpt_guess = guess_language(df)
    gpt_guess = gpt_guess[0].message.content.strip().split("\n") #gpt response

    df_gpt = create_df_from_gpt(gpt_guess) #create df from gpt response

    merged_df = df[['Language']].join(df_gpt) #merge the gpt response with the original df
    merged_df['match'] = merged_df['Language'] == merged_df['lang']

    merged_df.to_csv("compare.csv", index=True)
    print(merged_df["match"].value_counts()[False])


