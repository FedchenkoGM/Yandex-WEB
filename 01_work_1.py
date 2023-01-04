def human_read_format(size):
    if size < 1024:
        return f'{size}Б'
    if round(size / 1024) < 1024:
        return f'{round(size / 1024)}КБ'
    if round(size / 1024 / 1024) < 1024:
        return f'{round(size / 1024 / 1024)}МБ'
    if round(size / 1024 / 1024 / 1024) < 1024:
        return f'{round(size / 1024 / 1024 / 1024)}ГБ'


print(human_read_format(1023))
print(human_read_format(15000))
print(human_read_format(26843545711))