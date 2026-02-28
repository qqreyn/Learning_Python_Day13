open("task1.txt", "x")

with open("task1.txt", "a") as f:
    f.write("First file")
    f.write("\nSecond line")
    f.write("\nApple")
    f.write("\nI like cars")
    f.write("\nPython is fantastic!")

with open("task1.txt") as f:
    print(f.read())

