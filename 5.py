num_list = list()
size = 0
try:
    for filename in ['5a.txt', '5b.txt']:
        with open(filename, 'r') as f:
            splited = f.read().split()
            size = len(splited) if len(splited) > size else size
            num_list.append(splited)
    for num in range(size):
        num_sum = 0
        for index in [0, 1]:
            if num < len(num_list[index]):
                num_sum += int(num_list[index][num])
        print(sum)
except FileNotFoundError:
    print('Um dos arquivos não foi encontrado!')
