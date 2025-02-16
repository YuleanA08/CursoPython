#El break es para parar una iteracion hasta cierto punto
for i in range(1,11):
    print(i)
    if i == 5:
        break

#El continue es una manera de decir que omita ese dato y siga
for i in range(1,11):
    if i == 6:
        continue
    print(i)