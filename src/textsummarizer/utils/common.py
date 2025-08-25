import os
from box.exceptions import BoxValueError
import yaml
from textsummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

#This file basically contains the common functions which might be used in various parts of this project. So kept under this file


#Reading the yaml file and return its content
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:   # ConfigBox is part of the python-box library, a tool that allows dictionary-like objects to be
    # accessed using dot notation (e.g., config.key instead of config['key']). 
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

#create directories
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):   #Verbose is a general programming term for produce lots of logging output. 
    # You can think of it as asking the program to "tell me everything about what you are doing all the time"
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")



@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

    