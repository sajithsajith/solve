from openai import AzureOpenAI
import os

def chat_gpt(image, system_prompt):
    """Function to interact with Azure OpenAI's chat completion API using an image and a system prompt.

    Args:
        image (str): Base64 encoded image string.
        system_prompt (str): System prompt to guide the chat model.

    Returns:
        str: The output from the chat model.
    """
    try:
        client = AzureOpenAI(
            api_key=os.getenv("AZURE_API_KEY"),
            api_version=os.getenv("AZURE_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_ENDPOINT"),
        )
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": system_prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{image}",
                            },
                        },
                    ],
                }
            ],
            max_tokens=4096,
        )
        output = completion.choices[0].message.content
        print(f"\n\033[94mChat-gpt output:\n{output}\n{50*'-'}\033[0m\n")
        return output
    except Exception as e:
        print("error occured in chatgpt, error: ", str(e))
        return None