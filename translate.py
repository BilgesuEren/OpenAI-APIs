from openai import OpenAI

# Set your OpenAI API key
# client

def translate_to_german(sentence):
    # Define the prompt for translation

    prompt = f"Translate the following English sentence to German: '{sentence}'"

    chat_completion = client.chat.completions.create(
    messages=[
            {"role": "system", "content": "You are a helpful assistant that translates English to German."},
            {"role": "user", "content": prompt}
        ],
        # model="gpt-3.5-turbo",
        # model = 'gpt-4-1106-preview',
        model = 'gpt-3.5-turbo-1106',
        max_tokens=100
    )

    # Extract and return the translated text
    translation = chat_completion.choices[0].message.content.strip()
    return translation

# Example usage
english_sentence = "Hello, how are you?"
german_translation = translate_to_german(english_sentence)
print(f"English: {english_sentence}")
print(f"German: {german_translation}")
