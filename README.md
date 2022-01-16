# Text Finder

## Description

This is a python script that helps you find a particular variable, text or a group of letters that matches the search pattern anywhere within a code base.

### Use Case

Say your code base had 5000+ lines of code and you were looking for where you used a certain function or declared a certain variable. You obviously can't go through the whole code base line by line. This script is the solution.

# Usage

- Clone the code to you local machine
- Run the script in your python enabled terminal
- You are prompted for the keyword to search for.
  #### Example
  `Enter the word to search for:`
- Enter the keyword to search for
- Next you are prompted for the folder path to search in.
  #### Example
  `Enter the folder to search: `
- Enter the folder to search in
- The program searches folders and return whether a match was found or not
- If the search succeeds, the result is the status of the search, the name of the file the match was made, the line the match was made, and the code on that line

  #### Sample Result

  `Enter the word to search for:`

  `Enter the folder to search: `

  `Found elif in the file ---- main.py ---- 24 ---- elif os.path.isdir(file) and file.name:`

- If the search did not find a match, the program will terminate with no result

## Alternatively

If you wanted to automate the whole process so that you don't have to enter a folder path every single time you edit the code as so'

```python
    folder_to_search = None
    # Put the folder path you want the script to search in
    folder_to_search = '<<path-to-folder>>'
```

## Extra

You might not want to search every folder or every file in the folders directories the fix for this is to pass in the name of the folder or file you don't want to search in the code as follows

```python
    # List containing folders that should not be searched
    folders_not_to_search = ['node_modules']

    # List containing files that should not be searched
    files_not_to_search = ['package-lock.json', 'package.json']
```
