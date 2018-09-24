import threading
a = list(enumerate([61863, 85751, 61008, 91486, 98320, 82460, 61334, 52075, 69939, 92354]))
b = [0 for i in range(len(a))]


def fatorial(n):
    fat = n
    for i in range(n-1, 1, -1):
        fat = fat * i
    return fat


def main():
    while a:
        entry = a.pop()
        print(entry)
        b[entry[0]] = fatorial(entry[1])


threads = []
for i in range(4):
    t = threading.Thread(target=main)
    t.start()
    threads.append(t)
for i in range(len(threads)):
    threads[i].join()
print(b)

