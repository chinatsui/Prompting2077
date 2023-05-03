import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

# import samples.use_delimiter
# response = get_completion(use_delimiter.prompt)
# print(response)

# import samples.structured_output
# response = get_completion(structured_output.prompt)
# print(response)

# import samples.interpret_instructions as interpret_instructions
# response = get_completion(interpret_instructions.prompt2)
# print(response)

import samples.few_shot as few_shot
response = get_completion(few_shot.prompt)
print(response)
