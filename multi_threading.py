import time
import threading

def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        print('square:',n*n)

def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        print('cube:',n*n*n)

arr = [2,3,8,9]

t = time.time()

calc_square(arr)
calc_cube(arr)
print("done in : ",time.time()-t)
print("Hah... I am done with all my work now!")
