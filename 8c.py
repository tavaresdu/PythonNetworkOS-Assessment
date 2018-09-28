import multiprocessing
a = list(enumerate([183677, 186720, 176916, 186554, 113034,
                    193701, 131768, 142185, 131518, 105202]))
b = [0 for i in range(len(a))]


def fatorial(n):
    fat = n
    for i in range(n-1, 1, -1):
        fat = fat * i
    return fat


def main(inq, outq, process):
    while not inq.empty():
        entry = inq.get()
        print('iniciando processo '+str(process)+' input '+str(entry))
        outq.put((entry[0], fatorial(entry[1])))
        print('terminado processo '+str(process)+' input '+str(entry))


if __name__ == '__main__':
    processes = []
    in_queue = multiprocessing.Queue()
    out_queue = multiprocessing.Queue()
    for entry in a:
        in_queue.put(entry)
    for i in range(4):
        p = multiprocessing.Process(target=main, args=(in_queue, out_queue, i))
        p.start()
        processes.append(p)
    for i in range(len(a)):
        q = out_queue.get()
        b[q[0]] = q[1]
    for p in processes:
        p.join()
    print(b)
