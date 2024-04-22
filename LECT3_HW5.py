
n = int(input("Enter n: "))

for i in range(2, n + 2):
    for j in range(n - i + 1):
        print(end="  ")
    for j in range(1, i - 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end="")
        for k in range(j - 1, 0, -j):
            print(end=" ")

    print()


