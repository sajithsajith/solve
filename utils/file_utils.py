import io
import base64
import os
import shutil
import random
import string

from PIL import Image


def move_file(old_directory, new_directory):
    """
    Moves all PNG files from the specified old_directory to the new_directory, renaming each file to a random 10-character lowercase string.
    Args:
        old_directory (str): The path to the directory containing the PNG files to move.
        new_directory (str): The path to the directory where the PNG files will be moved.
    Notes:
        - Only files with a '.png' extension are moved.
        - Each moved file is renamed to a random 10-character lowercase string followed by '.png'.
        - Prints the path of each file moved.
    """

    for file_name in os.listdir(old_directory):
        file_path = os.path.join(old_directory, file_name)
        if os.path.isfile(file_path) and file_path.endswith(
            ".png"
        ):  # Check if it's a file
            shutil.move(
                file_path,
                f"{new_directory}/{''.join(random.choices(string.ascii_lowercase, k=10))}.png",
            )
            print(f"moved: {file_path}")


def get_file(directory):
    """
    Retrieves a list of file paths for all PNG files in the specified directory.
    Args:
        directory (str): The path to the directory to search for PNG files.
    Returns:
        list: A list of full file paths to PNG files found in the directory.
    """

    paths = []
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path) and file_path.endswith(".png"):
            paths.append(file_path)
    return paths


def img_to_bytes(path):
    """
    Converts an image file at the given path to both raw bytes and a base64-encoded string.
    Args:
        path (str): The file path to the image.
    Returns:
        dict: A dictionary containing:
            - "raw_bytes": The raw bytes of the image in PNG format.
            - "bytes_base64": The base64-encoded string of the image bytes.
    Raises:
        FileNotFoundError: If the specified image file does not exist.
        OSError: If the image file cannot be opened or read.
    """

    pill_image_resized = Image.open(path)
    pill_image_bytes = io.BytesIO()
    pill_image_resized.save(pill_image_bytes, format="PNG", quality=95)
    pill_image_bytes_value = pill_image_bytes.getvalue()
    pill_image_base64 = base64.b64encode(pill_image_bytes_value).decode("utf-8")
    pill_image_bytes.close()
    return {"raw_bytes": pill_image_bytes_value, "bytes_base64": pill_image_base64}
