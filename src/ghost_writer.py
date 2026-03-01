import os
import sys
from openai import OpenAI

def generate_test(file_path):
    if not os.path.exists(file_path):
        return

    with open(file_path, 'r') as f:
        code = f.read()

    client = OpenAI(
        base_url="https://models.inference.ai.azure.com",
        api_key=os.getenv("GH_MODELS_TOKEN")
    )
    
    response = client.chat.completions.create(
        model="Grok-3", # or "Grok-4.1-fast-reasoning"
        messages=[
            {"role": "system", "content": "You are Grok. Write unit tests for the following code. Return ONLY the code. No markdown blocks."},
            {"role": "user", "content": code}
        ]
    )
    
    test_code = response.choices[0].message.content
    test_file_path = f"{os.path.splitext(file_path)[0]}.test.js"
    
    with open(test_file_path, 'w') as f:
        f.write(test_code)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        generate_test(sys.argv[1])