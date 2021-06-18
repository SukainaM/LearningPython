num = int(input("any num: " ))

numbers = list(range(1, num+1))

new_list = []

# for i in numbers:
#     if num % i == 0:

print([i for i in numbers if num % i ==0])
        # new_list.append(i)
