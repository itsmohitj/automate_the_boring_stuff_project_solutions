#The Collatz Sequence
def collatz(number):
    if(number % 2 == 0):
        result = number // 2
    else:
        result = 3 * number + 1
    print(result)
    return result

num = int(input("Enter a number: "))
while(num != 1):
    num = collatz(num)
print("The Collatz Sequence is complete.")