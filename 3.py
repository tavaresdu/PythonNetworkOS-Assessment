import os
from operator import itemgetter
directory = input('Digite um diretório: ')
files = os.listdir(directory)
for i in reversed(range(len(files))):
    file_fullpath = os.path.join(directory, files[i])
    if os.path.isfile(file_fullpath):
        file_info = dict()
        file_info['name'] = files[i]
        file_info['size'] = os.stat(file_fullpath).st_size
        files[i] = file_info
    else:
        del files[i]
files = sorted(files, key=itemgetter('size'), reverse=True)
with open('3.txt', 'w') as f:
    for file_info in files:
        f.write(f'{file_info["name"]} = {file_info["size"]} bytes\n')
print('Arquivo gerado com sucesso!')
