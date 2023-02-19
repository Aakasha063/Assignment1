# Write a code to print Fibonacci series

number = int(input('Enter the number till which you would like to print Fibonacci series : '))
print(f'Fibonacci series till {number} is : ')

num1 = 0
num2 = 1

while num2<number:
    print(num2)
    num1, num2 = num2, num1 + num2
