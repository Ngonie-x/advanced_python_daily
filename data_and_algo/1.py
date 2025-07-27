import time


def oddGen(n, m):
    while n < m:
        yield n

        n += 2


def oddLst(n, m):
    lst = []
    while n < m:
        lst.append(n)
        n += 2
    return lst


t1 = time.time()
sum(oddGen(1, 1000000))
print("Time to sum an iterator: %f" % (time.time() - t1))

t2 = time.time()
sum(oddLst(1, 1000000))
print("Time to sum an iterator: %f" % (time.time() - t2))
