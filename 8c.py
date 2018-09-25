import multiprocessing
a = list(enumerate([61863, 85751, 61008, 91486, 98320, 82460, 61334, 52075, 69939, 92354]))
b = [0 for i in range(len(a))]


def fatorial(n):
    fat = n
    for i in range(n-1, 1, -1):
        fat = fat * i
    return fat


def main(entry, queue):
    print(entry)
    queue.put((entry[0], fatorial(entry[1])))


if __name__ == '__main__':
    processes = []
    queue = multiprocessing.Queue()
    for i in range(4):
        p = multiprocessing.Process(target=main, args=(a.pop(), queue))
        p.start()
        processes.append(p)
    for i in range(len(processes)):
        processes[i].join()
    print(queue)

