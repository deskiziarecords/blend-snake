import os
from openai import AzureOpenAI

endpoint = "<your-endpoint>"
model_name = "o4-mini"
deployment = "o4-mini"

subscription_key = os.getenv("AZURE_OPENAI_API_KEY")
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a senior DevOps engineer helping beginners.",
        },
        {
            "role": "user",
            "content": "How do I set up CI/CD using GitHub Actions for a Node.js app?",
        }
    ],
    max_completion_tokens=100000,
    model=deployment
)

print(response.choices[0].message.content)