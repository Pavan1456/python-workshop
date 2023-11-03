# def greet_name(name):
#     return f"Hello,{name}!"
# # print(greet_name("paban"))
# def maths_name(a):
#     return f"{a**0.5}"
 #mathsoperation
# def add(a,b):
#     return a+b
# def subtract(a,b):
#     return a-b
# def multiply(a,b):
#     return a*b
# def divide(a,b):
#     return a/b
import random
random_number = random.randint(1, 10)
random_choice = random.choice(['apple'		,'banana','cherry'])
print (random_choice)

import math
square_root = math.sqrt(25)
sine_value = math.sin(math.pi / 2)
print(sine_value)



import string
ascii_letters = string.ascii_letters
digits = string.digits
from datetime import datetime
current_date = datetime.now()
formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
print (formatted_date)



import os
current_directory = os.getcwd()
list_of_files = os.listdir(current_directory)
print (list_of_files)


import sys
command_line_arguments = sys.argv 
python_version = sys.version
print (command_line_arguments)




