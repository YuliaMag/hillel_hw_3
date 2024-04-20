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

    for i in range(min_w):
        print(" " * (min_w - i), "*" * (i * 2 + min_w))

    for i in range(min_w - 2, -1, -1):
        print(" " * (min_w - i), "*" * (i * 2 + min_w))
