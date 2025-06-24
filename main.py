import os

def split_of_type(folder:list):
    extensions = {'text': ['txt', 'doc', 'docx', 'rtf', 'odt'],
                  'pictures': ['jpg', 'png', 'gif', 'tiff'],
                  'audio': ['wav', 'mp3', 'aif', 'aiff', 'flac', 'mid'],
                  'spreadsheets': ['xls', 'xlsx', 'ods', 'dbf', 'csv'],
                  'programming': ['py', 'cpp', 'c', 'cs', 'js', 'java', 'go']
    }
    files = {'text_files': [], 'pictures_files': [], 'audio_files': [],
             'spreadsheets_files': [], 'programming_files': []
    }

    for file in folder:
        if file.split('.')[-1] in extensions['text']:
            files['text_files'].append(file)
        elif file.split('.')[-1] in extensions['pictures']:
            files['pictures_files'].append(file)
        elif file.split('.')[-1] in extensions['audio']:
            files['audio_files'].append(file)
        elif file.split('.')[-1] in extensions['spreadsheets']:
            files['spreadsheets_files'].append(file)
        elif file.split('.')[-1] in extensions['programming']:
            files['programming_files'].append(file)
        else: return None

    return files


def sort(path:str):
    if os.path.isdir(path):
        files = split_of_type(os.listdir(path))
        if files:
            for keys in files:
                if files[keys]:
                    os.mkdir(f'{path}/{keys}')
                    for file in files.get(keys):
                        os.replace(f'{path}/{file}', f'{path}/{keys}/{file}')
            print('Done!')
        else:
            print('Apparently there is nothing to sort')
    else:
        print('ERROR. sorter need a dir path')

def main():
    path = input('Input path to your folder. I will sorted it: ')
    sort(path)

while True:
    main()
