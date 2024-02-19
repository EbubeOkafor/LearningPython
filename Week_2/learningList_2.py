#Looping through a list using for loop
magicians = ['alice', 'david', 'carolina'] 
for m in magicians: #m represents each element of the list. For the 1st loop 'm' is alice, 2nd loop, m is david and so on.
    print(m) #“For every magician in the list of magicians, print the magician’s name.” 
    print(m.title() + ", that was a great trick!") 
    print("I can't wait to see your next trick, " + m.title() + ".\n")

#Using range()
for i in range(1,5): #range here would give numbers 1 to 5-1. That is 1 to 4.
    print(i)

#Using list() and range() to form a list of numbers.
numbers = list(range(1,6)) #List simply converts the range of values to a list.
print(numbers)

even_numbers = list(range(2,11,2)) #This time around range() has a step parameter. That is count from 2 to 11-1 by 2's
print(even_numbers)

#To put the first 10 square numbers into a list(That is the square of nos 1 to 10):
squares = [] #An empty list is created
for value in range(1,11): #We loop through values 1 to 10
    square = value**2 #The square of each value is stored in variable 'square'.
    squares.append(square) #The value of variable 'square' is then apended to the empty list, 'squares'. And the loop restarts.
print(squares)
print(min(squares)) #prints minimum value in list 'squares'
print(max(squares)) #Prints maximum value in list 'squares'
print(sum(squares)) #Prints sum of values in list 'squares'

