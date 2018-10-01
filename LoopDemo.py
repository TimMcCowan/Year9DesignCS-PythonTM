#A loop structure is a structure that allows us to run a sectiub if code a number of times.
# It is also great when we need to run a pattern

# There are 2 broad catagories of loops
#Conditional loop: This loops as long as something is true
#Counted loop: This loops a set number of times

#The general structure of a counted loop is 
#Count: This is the variable to count how many times a loop has run
#Check: This is a boolean statement we evaluate to decide to keep goung or not
#Change This is the count that happens after each loop

# we use a for i inrange loop

for i in range(0,6,1):
	print(i)

#how would the above loop run
# we would reach line 27
# i = 0,0<6 true, run
# i = 1, 1<6 true, run


print("************************")
print("Write a loop that will print out 7 to 104 inclusive")
for i in range(7,105,1):
	print(i)
print("************************")
print("Write a loop that will write the even numbers from -22 to 135 inclusive")
for i in range(-22, 135,2):
	print(i)

print("************************")
print("We can count backwards as well. Python3 will assume the check based on")
print("the relative value of the count and check")

for i in range(3,0,-1):
	print(i)

print("************************")
print("Print out all numbers from 101 to 0 inclusive")
for i in range(101,-1,-1):
	print("I COULD WRITE THIS!")
	print(i)

print("************************")

s = "Fish_food"

for i in range(0,9,1):
	print(s[i])

#Practice never type in length of string as a number always have computer find it
print("************************")

for i in range(8,-1,-1):
	print(s[i])

for i in range(0,len(s),2):
	print(s[i])