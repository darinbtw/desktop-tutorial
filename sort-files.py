from pathlib import Path
import shutil

path_home = Path('C:\Users\VladOS\Test_downloadss') #The main path, you wish to clear (C:\Users\uesrname\Test_downloads)

# Path.home() / 'downloads'

#categories of suffixes in dictonary
folders = {
    # Images
    '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images', '.gif': 'Images',
    '.bmp': 'Images', '.webp': 'Images', '.svg': 'Images', '.heic': 'Images',

    # Documents
    '.txt': 'Documents', '.pdf': 'Documents', '.doc': 'Documents', '.docx': 'Documents',
    '.rtf': 'Documents', '.odt': 'Documents', '.pptx': 'Documents', '.ppt': 'Documents',

    # Tables and datas
    '.xlsx': 'Spreadsheets', '.xls': 'Spreadsheets', '.csv': 'Spreadsheets', '.json': 'Spreadsheets',

    # Archive
    '.zip': 'Archives', '.rar': 'Archives', '.7z': 'Archives', '.tar': 'Archives', '.gz': 'Archives',

    # Musics and videos
    '.mp3': 'Audio', '.wav': 'Audio', '.flac': 'Audio',
    '.mp4': 'Video', '.mkv': 'Video', '.avi': 'Video', '.mov': 'Video',

    # Programs and installers
    '.exe': 'Programs', '.msi': 'Programs',

    # Codes
    '.py': 'Code', '.js': 'Code', '.html': 'Code', '.css': 'Code',
}

for name in path_home.iterdir():
    if name.is_file():
        lower_name = name.suffix.lower() #your name suffix from a file
        folder = folders.get(lower_name, 'Others')
        print(f'{folder} -> {name.name}') #for debugging
        (path_home/folder).mkdir(exist_ok=True) #creating new folder if does not exist
        shutil.move(name, path_home/folder/name.name) #move from/to