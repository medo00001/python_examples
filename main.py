
# List = []
# List.append("1111")
# print(List)
# def funcx(y): return y**2
# print(funcx(5))


# numbers = list(range(3, 8))
# print(numbers)

# numbers = list(range(5, 20, 2))
# print(numbers)

# words = ["hello", "world", "spam", "eggs"]
# counter = 0
# max_index = len(words) - 1

# while counter <= max_index:
#    word = words[counter]
#    print(word + "!")
#    counter = counter + 1


# words = ["hello", "world", "spam", "eggs"]
# for word in words:
#   print(word + "!")

# for i in range(5):
#   print("hello!")

""" calculator"""
# while True:
#    print("Options:")
#    print("Enter 'add' to add two numbers")
#    print("Enter 'subtract' to subtract two numbers")
#    print("Enter 'multiply' to multiply two numbers")
#    print("Enter 'divide' to divide two numbers")
#    print("Enter 'quit' to end the program")
#    user_input = input(": ")

#    if user_input == "quit":
#       break
#    if user_input == "add":

#         num1 = float(input("Enter a number: "))
#         num2 = float(input("Enter another number: "))
#         result = str(num1 + num2)
#         print("The answer is " + result)

#    elif user_input == "subtract":
#       ...
#    elif user_input == "multiply":
#       ...
#    elif user_input == "divide":
#       ...
#    else:
#       print("Unknown input")


# def multiply(x, y):
#    return (x * y)

# a = 4
# b = 7
# operation = multiply
# print(operation(a, b))


# import emoji

# user_input = int(input("Enter number"))
# # print('  '* (user_input) + emoji.emojize(' :heart_eyes:', use_aliases=True))
# for i in range(0,user_input+1):
#     print('  '* (user_input-i+1) + emoji.emojize(' :heart_eyes:', use_aliases=True)*(i+i))

# import random
# import sys

# random_no = random.randint(1, 10)

# # user_input = int(input('Enter valid number 1 -10 : '))
# user_input = None


# while True:
#     user_input = int(input('Enter valid number 1 -10 : '))

#     if user_input > random_no:
#         print(' high ')
#     elif user_input < random_no:
#         print('low ')
#     else:
#         print('right')
#         play_again = input('u want play again : (Y or N):')
#         play_again = play_again.lower()

#         if play_again == 'y':
#             random_no = random.randint(1, 10)

#             user_input = int(input('Enter valid number 1 -10 : '))

#         else:
#             sys.exit()


# print(random_no)

# # lists
# my_list = ['red', 'blue', 'grey', 'text ', 'another' ]
# # get_color = my_list[len(my_list)-1]

# # cause len count 0 + till end
# # print(get_color)

# # check if item in list
# # we can make choic using if

# # if 'red' in my_list:
# #     print('its here : its ok ')
# # else:
# #     print('sry its not her')

# # # using loop in list
# my_list.append( ['new',50, True, 1 , 3 , 6])
# index = 0

# # for element in my_list:
# #     print (element)

# while index < len(my_list):# len of my list = 6
#     print(my_list[index][index])
#     index +=1 # index will be  0 +1  = 1

# """ 0+ 1 , 1+1 , 2+1 , 3+1 , 4+1 , 5+1   """

# # append item

# lists
# my_list = ['red', 'blue', 'grey', 'text ', 'another']
# get_color = my_list[len(my_list)-1]

# cause len count 0 + till end
# print(get_color)

# check if item in list
# we can make choic using if

# if 'red' in my_list:
#     print('its here : its ok ')
# else:
#     print('sry its not her')

# # using loop in list
# extend vs append       extend in the same list and append to the end of my list in another list
# my_list.extend(['new', 50, True, 1, 3, 6])
# index = 0
# print(my_list)
# for element in my_list:
#     print (element)

# while index < len(my_list):  # len of my list = 6
#     print(my_list[index])
#     index += 1  # index will be  0 +1  = 1

# """ 0+ 1 , 1+1 , 2+1 , 3+1 , 4+1 , 5+1   """

# append item
# my_list = ['red', 'blue', 'grey', 'text ', 'another']
# my_list.extend(['new', 50, True, 1, 3, 6])
# my_list.insert(1, [1, 333, 55, 99])

# my_list.pop(0)
# print(my_list)


# my_list = ['red', 'blue', 'grey', 'text ', "1"]

# user_word = input('please give me ur value to remove :').lower()


# if user_word in my_list:
#     my_list.remove(user_word)
#     print(my_list)

# my_list = ['red', 'blue', 'grey', 'text ', 1]

# # print('.'.join(my_list))
# string = 'hello'

# y = [x*5 for x in string]
# new_list = list(string)
# print(new_list)


# import asyncio

# async def main():
#     print('Hello ...')
#     await asyncio.sleep(1)
#     print('... World!')

# # Python 3.7+
# asyncio.run(main())

# #TODO: add more func

# nested list

# new_list = ['ali', 'amir', 'medo']
# new_list2 = ['*', '*', '*']
# new_list3 = ['4', '5', '6']

# mylist = [[new_list, new_list2, new_list3], [
#     new_list, new_list2, new_list3], [new_list, new_list2, new_list3]]

# [[[[print(newval)for newval in val]for val in item] for item in mylist]]

# value = ['mohamed',28,True] 
# key =['name','age','status']
# newdict = dict(key=value)
# print(newdict)


# mydict = {'name':"mohamed",'age':25,'status':True}

# for key ,value in mydict.items():
#     print(f"key is :{key}, value is {value}")


# # items = mydict.items()

# print(items)





