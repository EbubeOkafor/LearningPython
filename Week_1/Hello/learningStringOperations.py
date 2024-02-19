#Changing textcase with methods
name = "ada lovelace"
print(name)
print(name.title()) #prints name in title case
print(name.upper()) #prints name in upper case
print(name.lower()) #prints name in lower case

#String concatenation
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name #The empty quotation mark is just used to create a space between the first and last name.
print(full_name)

#adding whitespace to strings
print("Languages:\n\tPython\n\tC\n\tJavaScript") #\n signifies new line while \t signifies tab

#removing whitespace from strings
favorite_language = ' python ' 
print(favorite_language)  
print(favorite_language.rstrip()) #rstrip() removes whitespace from the right of string
print(favorite_language.lstrip()) #lstrip() removes whitespace from the left of string

#Changing integers to string to prevent type error
age = 23
wish = "Happy " + str(age) + "rd Birthday!" #str() converts the integer 23 to string 23
print(wish)