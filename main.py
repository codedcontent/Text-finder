# This scripts searches for a keyword through out the entire folder you specify

import pathlib
import os

keyword_search = input('Enter the word to search for: ')

# List containing folders that should not be searched
folders_not_to_search = ['node_modules']

# List containing files that should not be searched
files_not_to_search = ['package-lock.json', 'package.json']


def main():
    folder_to_search = None or input('Enter the folder to search: ')
    print('Searching.. Searching...')
    traverse_folder(folder_to_search)


def traverse_folder(folder):
    # Set the path of the folder to the new path
    new_path = folder

    # Using the pathLib module to work with folder directories
    directory = pathlib.Path(new_path)

    # Iterate through the folder in the directory
    for file in directory.iterdir():
        # If it's a file that should be searched, search it
        if os.path.isfile(file) and file.name:
            checkable_file_name = str(file).replace(
                str(new_path), '').replace('\\', '').replace('/', '').lower()

            if checkable_file_name not in files_not_to_search:
                search_file(file)
        elif os.path.isdir(file) and file.name:
            # if it's a folder check if it should be searched
            checkable_folder_name = str(file).replace(
                str(new_path), '').replace('\\', '').replace('/', '').lower()
            if checkable_folder_name not in folders_not_to_search:
                # Call the traverse_folder function to continue traversing folders of folders
                traverse_folder(file)


def search_file(file):
    try:
        with open(file, 'r') as f:
            # read the files content and count each line
            file_lines = f.readlines()
            file_number = 0
            for line in file_lines:
                file_number += 1
                clean_line = line.strip()
                if keyword_search in clean_line:
                    print(
                        f'Found {keyword_search} in the file ---- {file.name} ----  {file_number} ---- {clean_line}')
    except:
        print('Unable to read this file')
        pass


if __name__ == '__main__':
    main()
