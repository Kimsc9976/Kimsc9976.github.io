data = input()

num_dict = {"1":0, "0":0}

num_dict[data[0]] += 1

temp = data[0]
for num in data:
    
    if temp!=num:
        num_dict[num] = num_dict[num] + 1
        temp = num

print(min(num_dict["1"],num_dict["0"]))