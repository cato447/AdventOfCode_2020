f = open("Ressources/NumsDay1.txt", 'r')

nums = f.readlines()
nums = [int(i) for i in nums]

for i in nums:
    for j in nums:
        for k in nums:
            if i + j + k == 2020:
                print(i*j*k)
                break