#challenge 029

import math

num=int(input("Please enter a number that is over 500"))
if num >500:
    answer=math.sqrt(num)
    print(round(answer,2))
else:
    print("Error, number too low.")
