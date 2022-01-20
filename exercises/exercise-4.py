# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a:
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

print("Enter the lengths of three side of a triangle:")
a_input = input("a: ")
b_input = input("b: ")
c_input = input("c: ")

a = int(a_input)
b = int(b_input)
c = int(c_input)


print("A triangle with sides of " + a_input + ", " +
      b_input + " & " + c_input + " is ", end="")
if(a == b and b == c):
    print("an equilateral")
elif(a != b and (a != c and b != c)):
    print("a scalene")
else:
    print("an isosceles")
print(" triangle")
