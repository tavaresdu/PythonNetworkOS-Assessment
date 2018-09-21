try:
    with open('4.txt', 'r') as f:
        print(f.read()[::-1])
except FileNotFoundError:
    print('Arquivo não encontrado!')