from zipfile import ZipFile


with ZipFile('input.zip') as myzip:
    for info in myzip.infolist():
        if info.filename[-1] == '/':
            dirs = info.filename[:-1].split('/')
            print('  ' * (len(dirs) - 1) + dirs[-1])
        else:
            print('  ' * len(dirs) + info.filename.split('/')[-1])



