from zipfile import ZipFile
import json


count = 0
with ZipFile('input.zip') as myzip:
    for info in myzip.filelist:
        if info.filename[-4:] == 'json':
            with myzip.open(info.filename) as f:
                data = json.load(f)
            if data['city'] == 'Москва':
                count += 1
print(count)




