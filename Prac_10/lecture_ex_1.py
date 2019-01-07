def rec_fun(n):
    if n > 0:
        return rec_fun(n - 1) + n * 2
    return 0


print(rec_fun(4))

print(" ".join([str(i * 2) for i in range(1, 16, 3) if i % 2 == 0]))


values = (2, 4, 6)
for x, y in enumerate(values):
    print("{0}:{1:.0f}".format(x, y), end=" ")

