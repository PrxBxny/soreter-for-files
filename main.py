import os

def split_of_type(folder:list):
    text = ['txt', 'doc', 'docx', 'rtf', 'odt']
    pictures = ['jpg', 'png', 'gif', 'tiff']
    audio = ['wav', 'mp3', 'aif', 'aiff', 'flac', 'mid']
    spreadsheets = ['xls', 'xlsx', 'ods', 'dbf']
    programming = ['py', 'cpp', 'js', 'java', 'c', 'cs', 'go']

    text_paths = []
    pictures_paths = []
    audio_paths = []
    spreadsheets_paths = []
    programming_paths = []

    for file in folder:
        print(file)
        if file.split('.')[-1] in text:
            text_paths.append(file)
        elif file.split('.')[-1] in pictures:
            pictures_paths.append(file)
        elif file.split('.')[-1] in audio:
            audio_paths.append(file)
        elif file.split('.')[-1] in spreadsheets:
            spreadsheets_paths.append(file)
        elif file.split('.')[-1] in programming:
            programming_paths.append(file)

    return[text_paths, pictures_paths, audio_paths, spreadsheets_paths, programming_paths]


def sort(path:str):
    if os.path.isdir(path):
        files = split_of_type(os.listdir(path))
        for i in range(len(files)):
            print(files[i])
    else:
        print('файлов не обнаружено')
