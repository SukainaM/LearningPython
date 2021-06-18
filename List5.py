a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

listt = []

for num in a:
    if num <5:
        listt.append(num)

print(listt)



# one liner
print([aa for aa in a if aa < 5])