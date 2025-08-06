# Standard Library Imports
import os
import sys


def resource_path(relative_path):
    """
    Function to get the absolute path to the images/sounds for PyInstaller to use
    :param relative_path: the relative path of the resource
    :return: the absolute path of the resource
    """
    try:
        # PyInstaller temporary folder (when using onefile, every resource file, such as an image or sound file, is moved there)
        base_path = sys._MEIPASS  # Points to the temporary folder
    # In cases where the .py file is run instead of the app (_MEIPASS doesn't exist)
    except AttributeError:
        # Use the current working directory
        base_path = os.path.abspath(".")
    # The absolute path of the resource passed in is returned
    # Combine the base path with the relative path
    return os.path.join(base_path, relative_path)