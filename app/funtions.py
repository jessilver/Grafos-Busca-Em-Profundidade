import sys
from colorama import init, Fore, Style
import imports
import os

def read_all_files_in_imports(imports_path=None):
    files_content = {}

    if imports_path is None:
        imports_path = os.path.join(os.path.dirname(__file__), 'imports')

    try:
        if not os.path.exists(imports_path):
            raise FileNotFoundError(f"The directory {imports_path} does not exist.")
        
        dighraphs = {}
        block = {}

        dighraphs_count = 1

        list_files = os.listdir(imports_path)

        for filename in list_files:
            file_path = os.path.join(imports_path, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf-8') as file:
                    files_content[filename] = file.read()
                    # print(filename)
                    # print(files_content[filename])
        for archive in files_content:
            # print(archive)
            for line in files_content[archive].split('\n'):
                if line == '':
                    dighraphs_count += 1
                    continue
            
                if 'digraph_'+str(dighraphs_count) not in dighraphs:
                    dighraphs['digraph_'+str(dighraphs_count)] = []

                dighraphs['digraph_'+str(dighraphs_count)].append(line)
        # print(files_content)
                    
        return os.listdir(imports_path), dighraphs

    except FileNotFoundError as e:
        return [], {}

def get_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def is_imports_directory_empty(imports_path=None):
    if imports_path is None:
        imports_path = os.path.join(os.path.dirname(__file__), 'imports')

    if not os.path.exists(imports_path):
        raise FileNotFoundError(f"The directory {imports_path} does not exist.")

    return len(os.listdir(imports_path)) == 0

def create_imports_directory(imports_path=None):
    if imports_path is None:
        imports_path = os.path.join(os.path.dirname(__file__), 'imports')

    if not os.path.exists(imports_path):
        os.makedirs(imports_path)