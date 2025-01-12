# # for i in range(1, 10):
# #     str = "*"              ##star pyramid in simple
# #     print(str * i)

def pyramid(rows):                  ##starpyramid but more accurate
    for i in range(1, rows+1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print("* ", end="")
        print()
pyramid(10)
print("Merry Christmas")