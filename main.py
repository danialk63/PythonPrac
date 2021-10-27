print("HELLO WORLD!!")
#Different Print Statements:
print("Escape Sequence, escapeSequence2", end=" ")
print("Escape Sequence3")

#Comments
"""For
Multi
line
comments"""

#Escape Sequence
print("HELLO \n This is AHMAD KHALID")

#Variables

var1 = "Ahmad"
var2 = 34
var3 = 6
print (var2 + var3)

#Type Casting

var1 = "Ahmad "
var2 = 34
var3 = 6
var4 = "44"
var5 = "55"
print (int (var4) + int (var5))
print(10 * "AHMAD \n" )
print (10 * str(int (var4) + int (var5)))
#input
"""print("Enter number")
inpnum = input()
print("You entered ", int(inpnum) + 10)
#Practice
print("Enter first number")
inp = input()
print("Enter second number")
inp2 = input()
print("The sum is", int(inp) + int(inp2))
"""

# Slicing

str = "my name is AHMAD"
print(str)
print(len(str))
print(str[0:16:1])
print((str[ ::-1])) #Reverse the string

#different Functions

print(str.endswith("D"))
print(str.capitalize())
print(str.find("is"))
print(str.lower())
print(str.upper())
print(str.replace("AHMAD", "AHMAD KHALID"))

#List slicing
numbers = [2,4,6,8,10]
#print(numbers[0:5:1])
#numbers.sort()
#numbers.reverse()
#numbers.append(15)
#numbers.append(16) #Append is for add number in the last
#numbers.insert(1,55) # Insert is for add number in any index
#numbers.remove(8)
#numbers.pop() # pop is for remove number in the last
#print(numbers)

#print(max(numbers))
#print(min(numbers))


#Tuple -> Tuple cannot be change its immutable
tp = (1,2,3)
#tp[1] = 8
print(tp)

