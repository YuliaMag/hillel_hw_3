min_w = int(input("Enter minimal width: "))
max_w = int(input("Enter maximal width: "))

# If the entered minimum width is greater than the maximum width, print a warning and terminate the program.
# If the difference between the maximum and minimum widths is not a multiple of 2,
# print a warning and terminate the program.

if min_w > max_w or (max_w - min_w) % 2 != 0:
    print("Inappropriate input!")
else:
    print("Correct input: ")

# Print a "diamond" with given dimensions composed of '*' symbols.

    w = (max_w - min_w)

    for i in range(w):
        print(" " * (w - i - 1) + "* " * (i + min_w))

    for i in range(w - 2, -1, -1):
        print(" " * (w - i - 1) + "* " * (i + min_w))





