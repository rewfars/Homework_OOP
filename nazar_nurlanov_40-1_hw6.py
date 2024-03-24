def bubble_sort(bubble):
    n = len(bubble)
    while n > 0:
        n -= 1
        for i in range (0, n):
            if bubble[i] > bubble[i+1]:
                bubble[i] , bubble[i + 1]= bubble[i+1], bubble[i]
numbers = [24, 53, 4, 35, 18, 32, 2, 74, 28]
bubble_sort(numbers)
print(numbers)



import random

def binary_search(val):
    n = 5000
    resultOK = False
    first = 0
    last = n - 1
    pos = 0

    while first < last:
        middle = (first + last)//2
        if val==middle:
            first = middle
            last = first
            resultOK = True
            pos = middle
        else:
            if val > middle:
                first = middle+1
            else :
                last = middle-1


    if resultOK:
        print('элемент найден')
        print(pos)
    else:
        print('элемент не найден')

val = random.randint(0, 5000)
print(val)
binary_search(val)