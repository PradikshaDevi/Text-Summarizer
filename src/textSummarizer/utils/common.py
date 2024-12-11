import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns
    
    Args:
        path_to_yaml (str): Path like input

    Raises:
        ValueError: If yaml file is empty
        e: empty yaml file

    Returns:
        ConfigBox: Returns ConfigBox type from yaml file
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"The yaml file at {path_to_yaml} is empty.")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates directories in the specified list

    Args:
        path_to_directories (list): List of paths to directories
        verbose (bool, optional): Ignore if multiple directories is to be created. Defaults to False.
    """
    for path in path_to_directories:
        directory_path = Path(path)
        if not directory_path.is_dir():
            os.makedirs(directory_path, exist_ok=True)
            if verbose:
                logger.info(f"Directory '{path}' created.")
        else:
            if verbose:
                logger.info(f"Directory '{path}' already exists.")



@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB
    
    Args:
        path (Path): Path of the file)

    Returns:
        str: size in KB
    """

    size_in_kb = round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"