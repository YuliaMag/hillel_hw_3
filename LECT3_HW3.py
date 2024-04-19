
# a = "*"
# b = " "
# i = int(input("Enter the size of the triangle: "))
# j = 1
#
# for k in range(i, 0, -1):
#     print((b * k) + (a * j))
#     j += 1

a = "*"
b = " "
i = int(input("Enter the size of the triangle: "))
j = 1

for k in range(i, 0, -1):
    k -= 1
    print((b * k) + (a * j))
    j += 1


