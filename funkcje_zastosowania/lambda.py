# list_numbers = [1, 2 , 3, 4, 11, 14, 15, 20, 21]

# parzyste = list(filter( lambda x: x % 2 == 0, list_numbers))

# print(parzyste)


# def generate_multiplier(n):
#     return lambda x: x * n

# mul_2 = generate_multiplier(2)
# mul_3 = generate_multiplier(3)

# print(mul_2(5)) # 10
# print(mul_3(5)) # 15

# LAB

text_list = ['x','xxx','xxxxx','xxxxxxx','']

len_list = list(map(lambda x: len(x), text_list))

print(len_list) 