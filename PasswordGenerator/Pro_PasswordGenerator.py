import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'v', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '_', '|', '<', '>', '?', '/']

print("Welcome to Password Generators!")

l_txt = int(input("How many letters you want in your password: "))

s_txt = int(input("How many symbols you want in your password: "))

n_txt = int(input("How many numbers you want in your password: "))

pass_list = []

for i in range(1, l_txt + 1):
    x = random.choice(letters)
    pass_list.append(x)
for i in range(1, s_txt + 1):
    y = random.choice(symbols)
    pass_list.append(y)
for i in range(1, n_txt + 1):
    z = random.choice(numbers)
    pass_list.append(z)
# print(pass_list)
random.shuffle(pass_list)
password = ""
for j in pass_list:
    password = password + j
print("Password: {}".format(password))