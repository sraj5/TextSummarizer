import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s')

project_name='textsummarizer'
#making a list of folders and files required for the project which will be automatically created
list_of_files=[
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath=Path(filepath)  #Path is a functon which changes the filepath to the operting system's way of writing path. Windows, linux have
    #different way of writing the paths
    filedir,filename=os.path.split(filepath)
    
    if filedir!="":   
        os.makedirs(filedir,exist_ok=True)  #If the directory already exists, the function does nothing and no error is raised. If the directory
        # does not exist, it creates the directory along with any necessary parent directories.
        logging.info(f'Creating directory:{filedir} for the file {filename}')
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):   #now if the filepath doesnt exist already, (practically the file
        # doesn't exist) then the file has to be created or if the file path exists and the size of the file is zero then it has to opened only
        with open(filepath,'w') as f:
            pass
            logging.info(f'Creating empty file:{filepath}')
    else:   #file exists at the given path and it has size greater than zero
        logging.info(f'{filepath} already exists')
    