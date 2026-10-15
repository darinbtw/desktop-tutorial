from pathlib import Path
import shutil

path_home = Path.home() / 'Test_downloads' #The main path, you wish to clear (C:\Users\uesrname\Test_downloads)

#categories of suffixes in dictonary
folders = {'.jpg': 'Images', '.png': 'Images', '.txt': 'Documents', '.pdf': 'Documents'}

for name in path_home.iterdir():
    if name.is_file():
        lower_name = name.suffix.lower() #your name suffix from a file
        folder = folders.get(lower_name, 'Others')
        print(f'{folder} -> {name.name}') #for debugging
        (path_home/folder).mkdir(exist_ok=True) #creating new folder if does not exist
        shutil.move(path_home/name.name, path_home/folder/name.name) #move from/to