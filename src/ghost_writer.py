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
        model="grok-3",
        messages=[
            {"role": "system", "content": "You are Grok 3. Write unit tests for the following code. Return ONLY the raw code. No markdown formatting or explanations."},
            {"role": "user", "content": code}
        ]
    )
    
    test_code = response.choices[0].message.content

    test_dir = "tests"
    os.makedirs(test_dir, exist_ok=True)

    basename = os.path.basename(file_path)
    name, ext = os.path.splitext(basename)
    test_file_path = os.path.join(test_dir, f"{name}.test{ext}")

    with open(test_file_path, 'w') as f:
        f.write(test_code)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        generate_test(sys.argv[1])