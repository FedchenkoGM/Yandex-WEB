import os


def human_read_format(size):
    if size < 1024:
        return f'{size}Б'
    if round(size / 1024) < 1024:
        return f'{round(size / 1024)}КБ'
    if round(size / 1024 / 1024) < 1024:
        return f'{round(size / 1024 / 1024)}МБ'
    if round(size / 1024 / 1024 / 1024) < 1024:
        return f'{round(size / 1024 / 1024 / 1024)}ГБ'


def get_files_sizes():
    sp = []
    for f in os.listdir():
        if os.path.isfile(f):
            sp.append(f'{f} {human_read_format(os.path.getsize(f))}')
    return '\n'.join(sp)


print(get_files_sizes())