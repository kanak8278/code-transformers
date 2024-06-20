from sys import api_version
from openai import AzureOpenAI, OpenAI
from tenacity import retry, wait_random_exponential, stop_after_attempt
import os

GPT_MODEL = "gpt-4-turbo"
api_key = os.getenv("AZURE_OPENAI_API_KEY")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")

client = AzureOpenAI(api_key=api_key, api_version=api_version, azure_endpoint=endpoint)


@retry(wait=wait_random_exponential(multiplier=1, max=40), stop=stop_after_attempt(10))
def chat_completion_request(
    messages, tools=None, tool_choice=None, model=GPT_MODEL, response_format=None
):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tools,
        tool_choice=tool_choice,
        response_format=response_format,
    )
    return response


if __name__ == "__main__":
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"},
    ]
    response = chat_completion_request(messages)
    print(response.choices[0].message.content)
