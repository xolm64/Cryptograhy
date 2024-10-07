import json

with open("./text.txt", "r") as file:
    data = file.read()


print(data)
new_data = []
words = data.split()

for elem in words:
    if  'з'  in elem or "З" in elem:
        new_data.append("***")
    else:
        new_data.append(elem)

new_data = " ".join(new_data)
print(new_data)
file = open("./output1.txt", "w")
file.write(new_data)

with open("./output1.txt", "w") as file:
    file.write(new_data)
