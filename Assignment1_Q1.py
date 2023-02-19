# Write a code to print Fibonacci series

number = int(input('Enter the number till which you would like to print Fibonacci series : '))
print(f'Fibonacci series till {number} is : ')

n1 = 0
n2 = 1

while n2<number:
    print(n2)
    n1, n2 = n2, n1 + n2