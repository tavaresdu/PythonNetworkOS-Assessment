import threading
a = list(enumerate([183677, 186720, 176916, 186554, 113034,
                    193701, 131768, 142185, 131518, 105202]))
b = [0 for i in range(len(a))]


def fatorial(n):
    fat = n
    for i in range(n-1, 1, -1):
        fat = fat * i
    return fat


def main(thread):
    while a:
        entry = a.pop()
        print('thread '+str(thread)+' input '+str(entry))
        b[entry[0]] = fatorial(entry[1])
        print('terminado thread '+str(thread)+' input '+str(entry))


threads = []
for i in range(4):
    t = threading.Thread(target=main, args=(i,))
    t.start()
    threads.append(t)
for t in threads:
    t.join()
