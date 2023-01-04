from zipfile import ZipFile


def human_read_format(size):
    if size < 1024:
        return f'{size}Б'
    if round(size / 1024) < 1024:
        return f'{round(size / 1024)}КБ'
    if round(size / 1024 / 1024) < 1024:
        return f'{round(size / 1024 / 1024)}МБ'
    if round(size / 1024 / 1024 / 1024) < 1024:
        return f'{round(size / 1024 / 1024 / 1024)}ГБ'


with ZipFile('input.zip') as myzip:
    for info in myzip.infolist():
        if info.filename[-1] == '/':
            dirs = info.filename[:-1].split('/')
            print('  ' * (len(dirs) - 1) + dirs[-1])
        else:
            print('  ' * len(dirs) + info.filename.split('/')[-1], human_read_format(info.file_size))



