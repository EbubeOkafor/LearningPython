#simple list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles) #This would print all elements of the list including the square brackets

#Accessing elements in a list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0]) #Allows us pick the first element in the list. Note that counting starts from 0.
print(bicycles[1])
print(bicycles[2])
print(bicycles[3])
print(bicycles[1].upper()) #prints the second element of the list in uppercase.

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

#Accessing elements from behind in a list
cars = ['bentley', 'toyota', 'benz', 'volvo']
print(cars[-1]) #prints the last element in a list
print(cars[-2]) #prints second to the last element in a list

##Modifying the elemnets of a list##

#Changing values of elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati' #Changes the value of the first element of the list
print(motorcycles)

#Adding a new element to the end of a list using .append() method
cars.append('jeep')
print(cars)

#Inserting a new element at any position of the list
cars.insert(1, 'innoson') #adds a new element innoson at index[1] i.e position 2 of the list
print(cars)

#Removing an element of known index from a list
del motorcycles[1] #Removes the element 'yamaha' at index 1 of the list
print(motorcycles)

#Removing an element from a list using .pop() method
#pop() method allows us to remove the last item in a list but still have access to the removed item.
last_owned = motorcycles.pop() #the pooped element of motorcycle list is stoored in last_owned variable.
print("The last motorcycle I owned was a " + last_owned.title() + ".")

#Using pop() method to remove from any positon of the list
first_owned = cars.pop(0) #Pops the elemt at index[0] and stores it in first_owned variable.
print('The first car I owned was a ' + first_owned.title() + '.')
print(cars) #Bentley, which was the first element is no longer in the cars list.

#using remove() method to remove an element from a list by its value
cars.remove('volvo') #Removes volvo from the cars list
print(cars)

##Organising a list##
#Arranging list in alpabetical order using sort()#
cars.sort(reverse=True) #Arranges the list in normal alphabetical order permanently
print(cars)
cars.sort(reverse=False) #Arranges the list in reverse alphabetcal order permanently
print(cars)

#Arranging list in alpabetical order using sorted()#
alphabets = ['j', 'n', 'c','a' , 'e', 'f', 'g', 'h', 'i', 'b', 'k', 'l', 'm', 'd', 'o', 'p', 'q', 'r']
print(sorted(alphabets)) #sorted arranges the list temporarily that means it does not affect the original value of list,

#Reversing the content of a list
alphabets.reverse() #This reverse the list without arranging it alphabeticlly
print(alphabets)

#Checking the number of item in a list that is the length by len()
print(len(alphabets))