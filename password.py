import random
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%&*.?,:;][}{"
user_password = upper_case + lower_case + numbers + symbols 
user_length = 8
password = "".join(random.sample(user_password, user_length))
print("Your Password is", password)
