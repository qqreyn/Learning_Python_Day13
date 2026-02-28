with open("task4.txt", "a") as f:
    f.write("\nJapan")
    f.write("\nMalta")
    f.write("\nSlovenia")
    f.write("\nPoland")
    f.write("\nGermany")

with open("task4.txt", "r") as f:
    for x in f:
        print(x)