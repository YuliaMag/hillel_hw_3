min_w = int(input("Enter minimal width: "))
max_w = int(input("Enter maximal width: "))
mid_w = (max_w - min_w) / 2

if min_w > max_w or (max_w - min_w) % 2 != 0:
    print("Inappropriate input!")
else:
    print("Correct input: ")

y = mid_w
a = -1

while y <= mid_w:
    for x in range(0, max_w):
        if y <= x < (mid_w + min_w) and y == mid_w:
            print("*", end="")
            continue

        if (x == y or x == max_w - y - 1) and y != mid_w:
            print("*", end="")
            continue
        print(" ", end="")

    if y == 0:
        a = 1
    y = y + a
    # print(y+1, end="")
    print("")

