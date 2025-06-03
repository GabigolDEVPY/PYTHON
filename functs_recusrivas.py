def retornar(fatorial):
    if fatorial == 0 or fatorial == 1:
        return 1

    return fatorial * retornar(fatorial - 1)

print(retornar(5))