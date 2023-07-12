import func_kwargs
from func_args import 함수
from func_kwargs import *
import numpy as np
from func_kwargs import name_hello_함수 as nh

func_kwargs.name_hello_함수(a="kim", b="lee", c="park")
data = 함수(1,5,6,4,3,100)
print(data)
name_hello_함수(a= "kim", b="lee", c="park")
nh(a= "kim", b="lee", c="park" )

#상위경로 import
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# file_path = "C:\apps\python_lecture\basic"
# sys.path.append(file_path)
# import hello


list_1 = [1, 2, 3, 4, 5]
list_2 = [2, 5, 4, 2, 10]
a = np.array(list_1)
b = np.array(list_2)
print(list_1 + list_2)
print(a+b)