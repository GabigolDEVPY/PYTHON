import numpy


n, m, p = map(int, input().split())


array_1 = numpy.array([input().split() for _ in range(n)], int)


array_2 = numpy.array([input().split() for _ in range(m)], int)


result = numpy.concatenate((array_1, array_2), axis=0)


print(result)