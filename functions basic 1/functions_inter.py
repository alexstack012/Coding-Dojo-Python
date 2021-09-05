# # Note: Avoid using class keywords like int, str, list, and dict as variable/parameter names.

# # Update Values in Dictionaries and Lists

# x = [[5, 2, 3], [10, 8, 9]]
# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'}
# ]
# sports_directory = {
#     'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer': ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [{'x': 10, 'y': 20}]


# # Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# def num_swap():
#     x[1] = 15
#     print(x)


# num_swap()
# # Change the last_name of the first student from 'Jordan' to 'Bryant'
# def name_swap():
#     students[0] = {'first_name':  'Michael', 'last_name': 'Bryant'},
#     print(students)


# name_swap()

# # In the sports_directory, change 'Messi' to 'Andres'
# def name_swap2():
#     sports_directory = ['Andres', 'Ronaldo', 'Rooney']
#     print(sports_directory)


# name_swap2()


# # Change the value 20 in z to 30
# def num_swap2():
#     z = [{'x': 10, 'y': 30}]
#     print(z)


# num_swap2()


########### problem #2 ##################


# # Iterate Through a List of Dictionaries
# # Create a function iterateDictionary(some_list) that, given a list of dictionaries, the
# # function loops through each dictionary in the list and prints each key and the associated
# # value. For example, given the following list:

# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'},
#     {'first_name': 'Mark', 'last_name': 'Guillen'},
#     {'first_name': 'KB', 'last_name': 'Tonel'}
# ]


# def iterateDictionary(students):
#     print(students[0])
#     print(students[1])
#     print(students[2])
#     print(students[3])


# iterateDictionary(students)


# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


# problem #3 ############################3
# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'},
#     {'first_name': 'Mark', 'last_name': 'Guillen'},
#     {'first_name': 'KB', 'last_name': 'Tonel'}
# ]


# def iterateFirst():
#     print(students[0]['first_name'])
#     print(students[1]['first_name'])
#     print(students[2]['first_name'])
#     print(students[3]['first_name'])


# def interateLast():
#     print(students[0]['last_name'])
#     print(students[1]['last_name'])
#     print(students[2]['last_name'])
#     print(students[3]['last_name'])


# iterateFirst()
# interateLast()

# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries
# and a key name, the function prints the value stored in that key for each dictionary.
# For example, iterateDictionary2('first_name', students) should output:

# Michael
# John
# Mark
# KB

# # And iterateDictionary2('last_name', students) should output:

# Jordan
# Rosales
# Guillen
# Tonel


######### problem #4 ######################

# # Iterate Through a Dictionary with List Values
# # Create a function printInfo(some_dict) that given a dictionary whose values are
# # all lists, prints the name of each key along with the size of its list, and then
# # prints the associated values within each key's list. For example:


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


# def printInfo(dojo):
#     print(len(dojo['locations']))
#     print(dojo['locations'])
#     print(len(dojo['instructors']))
#     print(dojo['instructors'])


# printInfo(dojo)

def printInfo(dojo):  # function declaration, takes a dictionary as argument
    i = dojo.keys()  # i takes the return of the dictionary keys() function
    i = list(i)  # convert i to a proper list
    for x in range(0, len(i)):  # for loop to iterate through the keys list i
        # Prints the number of items in the list of the key, then the key in uppercase plus a colon as per assignment
        print(len(dojo[i[x]]), i[x].upper()+":")
        # for loop to iterate through the values of parent loop's key's list
        for value in dojo[i[x]]:
            print(value)  # print the value


printInfo(dojo)

# printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
