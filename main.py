import sys
import math
import os

from modulos.funciones import func1 as fun, func2, func3
from modulos.user import User

import requests

print(math.sqrt(9))
print(os.getcwd())
print(sys.argv)
# fun()
# func2()
# func3()

u = User(sys.argv[1])
print(u.get_name())
response = requests.get("https://google.com")
print(response.text)
