data = []
with open('user_data.txt') as file:
    for line in file:
        data.append(line.rstrip())
