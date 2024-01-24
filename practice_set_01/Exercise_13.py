"""     Print a downward Half-Pyramid Pattern of Star (asterisk)
"""
n = 6
b = 0

for i in range(n, b, -1):
    b += 1
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
