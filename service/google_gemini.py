import os

from google import genai
from google.genai import types


def gemini(image, prompt, model):
    """
    Generates content using the Gemini API based on a given image and prompt.
    Args:
        image (bytes): The image data in bytes, expected to be in PNG format.
        prompt (str): The textual prompt to guide the content generation.
        model (str): The name or identifier of the Gemini model to use.
    Returns:
        str or None: The generated text output from the Gemini model, or None if an error occurs.
    Raises:
        Exception: Any exception raised during the API call is caught and printed; function returns None in such cases.
    """

    try:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        response = client.models.generate_content(
            model=model,
            contents=[
                prompt,
                types.Part.from_bytes(data=image, mime_type="image/png"),
            ],
        )
        output = response.text
        print(f"\n\033[91m{model} output:\n{output}\n{50*'-'}\n\033[0m")
        return output
    except Exception as e:
        print("error occured in ", model, " , error: ", str(e))
        return None
