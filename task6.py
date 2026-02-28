with open("task6.txt", "r") as f:
    data = f.read()
    
words = data.split()
print("Total Words:", len(words))