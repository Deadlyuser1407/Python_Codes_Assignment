d=int(input("Enter the number whose digit are to be added: "))
def getSum(d):
    
    sum = 0
    for digit in str(d): 
      sum += int(digit)      
    return sum
print(getSum(d))
