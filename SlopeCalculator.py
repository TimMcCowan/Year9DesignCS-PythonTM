import os

print("Slope Calculator:")

#Input
x1 = input("Input x1: ")
x1 = int(x1)

y1 = input("Input y1: ")
y1 = int(y1)

x2 = input("Input x2: ")
x2 = int(x2)

y2 = input("Input y2: ")
y2 = int(y2)

#Process
rise = x2 - x1
run = y2 - y1

fSlope = rise/run

# Three types to consider
# Strings - store collections of characters
# Result = str(<value>)
# Integers - store integer values
# result int(<value>)
# Floats - store real numbers
# Result = float(<value>)

#output
print("Your slope is m ="+str(rise)+"/"+str(run))
print("Your slope as a decimal is "+str(fSlope))
print(rise)
print(run)

os.system("say Your slope is m ="+str(rise)+" over "+str(run))
