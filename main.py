
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


# value = 'User Dosent Exists'
# key =['name','age','status']

# dict = {}

# c= dict.fromkeys(key,value)

# print(c)


# # update

# mydict = dict (name='mohamed',age=28)

# # second ={'name':'greet'}
# second = second.update(mydict)

# print(second)
# print(mydict)


# a_dict = dict(k=4, z=2)
# a_dict.update(dict(l=1))
# print (a_dict)


# #  make dict
# key = ['A','c']
# value  = [1,2,3]

# x= {key[i]:value[i] for i in range(0,len(key))}
# print(x)


# #  make dict

# key  = [1,2]
# value = ['amir','ali']

# x= {key[i]:value[i].upper() for i in range(0,len(key))}
# print(x)


# # make search engine
# import sys
# mylist_names = ['ali', 'mohamed']
# mydict = {'name': mylist_names, "phone": '010636996868'}

# user_input = input('Enter search Name:')


# while user_input:

#     if user_input in mydict['name']:
#         # result = mydict['name'][user_input]
#         print('user exist')
#         user_input = input('Enter search Name:')

#     else:
#         print("No user have this Name")
#         print('Search Again (Y or N):')
#         user = (input('Search Again (Y or N):')).upper()
#         if user == 'Y':
#             user_input = input('Enter search Name:')
#         else:
#             sys.exit()

# set

# s= set('amir')

# q = {'z','m','cv'}
# print(type(q)) # set
# print(s)
# print('a'in s)

# myset ={'amir','mohamed'}
# myotherset = {'new', 'mohamed'}

# newset = myotherset | myset
# newset2 = myotherset & myset
# print(newset2)
# print(newset)

# def myfunc():
#     x = 10

#     return x
#     # print(x)  it wont run cause it after return


# print(myfunc())

# def addnum(user_name):
#     return (f'welcome back {user_name} !')

# print(addnum('mohamed'))


# def check_even(numbers):
#     total = 0
#     for num in numbers:
#         if num % 2 == 0:
#             total += num
#     return total


# print(check_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 2+ 4 + 6 +8  = 20


# def my_func_name ():
#     x = 10

# print(my_func_name.__name__ + ' my add')

# # map

# mylist = [1, 2, 3, 4, 5, 6]

# my_map = map(lambda x: x * 2 , mylist)

# new_list = list(my_map)
# print(new_list)


# filter for any iterable
# mylist = [1, 2, 3, 4, 5, 6]
# my_filter = filter(lambda x: x % 2 == 0, mylist)

# print(list(my_filter))
# import sys

# print(sys.getsizeof( name *10 for name in range(100)))

# mydict = [{'name': ['amir']}, {'name': ['aamohamedli']}]

# new_soreted = sorted(mydict, key=lambda x:x['name'] )

# print(new_soreted)

# mylist=  ['red','blue']

# def pick_color(color):
#     if color not in mylist:
#         raise ValueError ('pleas add vali color ')
#     print(f'u are right u chose \"   {color}   \" color')


# pick_color('red')

# except Error

# def divide_num(a, b):

#     try:
#         result = a/b
#         return result
#     except ZeroDivisionError as err:

#         print('there is some thing wrong ')

#         print(err)

# print(divide_num(1, 00))


#  request from website
# import requests


# user_serach = input('what do u want to search :')
# number = int(input('whats ur no for jokes u want :'))

# url = 'https://icanhazdadjoke.com/search'
# res = requests.get(
#     url, headers={'accept': 'application/json'},
#     params={'term': user_serach,
#             'limit': number})


# # print (res.ok)
# # print (res.headers)


# data = res.json()
# joke = data['results']
# no_of_result = data['total_jokes']
# print(f' i found {no_of_result} joke for { user_serach}')
# if no_of_result == 0:
#     print(f" ther is no joke for {user_serach}")
# else:
#     print(f' her is  {number} u want for now ')

# print("--------------------------------------")

# count = 0
# for jo in joke:
#     print(joke[count]['joke'])
#     print("--------------------------------------")
#     count += 1


# # print(data )
# # {'id': 'YvkV8xXnjyd', 'joke': 'Why did the cowboy have a weiner dog? Somebody told him to get a long little doggy.'}

#  classes

# print(help(list))

# # programme to cout words u want to count

# user_input = input('Enter letter u want to count : ')
# user_letter = input('What letter u want to count : ')
# def func(user_input):
#     return len(user_input)


# def count_letter(user_input):
#     repeat = 0
#     for letter in user_input:
#         if letter == user_letter:
#             repeat += 1
#     return repeat


# print(func(user_input))
# print( count_letter(user_input))


# class Person():
#     def __init__(self, anyname):
#         self.name = anyname


# mohamed = Person(50)   # we now made new obj ogf person
# print(mohamed.name)
# print ()


# class Person():
#     def __init__(self, anyname):
#         self.__name = anyname


# mohamed = Person(20)   # we now made new obj ogf person
# print(mohamed._Person__name)
# print ()

# class Person():
#     def __init__(self, name):
#         self.name = name

#     def func(self, thing, name):
#         # her self.name is from class not from func parameter that given
#         print(thing, self.name)
#         return name  # this param from func


# mohamed = Person(20)   # we now made new obj of person

# print(mohamed.func('hello mohamed', 'am another name'))

# class Person():
#     """its comment about explain this class

#     Returns:
#         [type] -- [description]
#     """
#     active_users = 0

#     def __init__(self, age):
#         self.age = age
#         # trace stat of attribute we add class attribute here
#         Person.active_users += 1  # we add 1 to active_user when we make new obj from class

#     def func(self, thing, name):
#         # her self.name is from class not from func parameter that given
#         print(thing, f'my age is {self.age}')
#         # import pdb; pdb.set_trace()
#         return (f'active user is now : {Person.active_users}')


# mohamed = Person(28)   # we now made new obj of person
# ali = Person(31)   # we now made new obj of person
# # Person.active_users is now 2 after we make 2 obj of class Person
# print(mohamed.func('hello mohamed', 'am another name'))

#  both var have same id cause they have same vale
# x = 10
# y = 9+1
# print(id(x))
# print(id(y))

# #  not the same id in the same list
# x = [0]
# y = [0]
# print(id(x))
# print(id(y))


# class method concerned with this class
# class Person():
#     @classmethod
#     def Set_obj(cls, data):
#         # we change the data passes and we can make change on it before we make new instance
#         name, last_name, age = data[0] = 'hello', data[1], data[2]
#         return cls(name, last_name, age)

#     def __init__(self, name, last_name, age):
#         self.name = name
#         self.last_name = last_name
#         self.age = age

#     def first_name():
#         return self.last_name


# # newuser = Person('mohamed', 'amir', 28)

# # print(newuser.name)
# # print(newuser.last_name)
# # print(newuser.age)

# user1 = Person.Set_obj(['mohamed', 'amir', 28])
# print(user1.name)
# print(user1.last_name)
# print(user1.age)

# class Name:
#     def __init__(self, name):
#         self.name = name


# class Person(Name):
#     def __init__(self, name):
#         self.name = name


# print(issubclass(Person, Name))


#  iterator and iterable
# name = 'mohamed'
# nextchar = iter(name)

# for char in nextchar:
#     """
#     it will iterate untill Raise  StopIteration erro
#     """
#     print(next(nextchar))


# print(next(nextchar))
# print(next(nextchar))
# print(next(nextchar))
# print(next(nextchar))
# print(next(nextchar))
# print(next(nextchar))
# print(next(nextchar))

# def iteron():
#     """[it return ' m' on first call ]

#     Returns:
#         [string] -- [first letter]
#     """
#     return next(nextchar)


# for char in range(0, len(name)):
#     print(iteron())
# #  use while with iterator instead of for loop


# name = input("please Enter any thing : ")
# nextchar = iter(name)


# def iteron():
#     """[it return ' m' on first call ]

#     Returns:
#         [string] -- [first letter]
#     """
#     return next(nextchar)


# char = 0
# while True:
#     print(iteron())
#     char += 1
#     if char == len(name):
#         print('End of text ')
#         break

# #  use while with iterator instead of for loop

def func1(func_as_var):
    def func2():
        func_as_var()
        print('its func 2')
    return func2


@func1
def func3():  # instead of write my_var = func1(func3)   i write  @func1
    print("its func 3")


@func1  # its decorator sugre
def func4():  # instead of write my_var = func1(func3)   i write  @func1
    print("its func 4")


func3()
print("------------------------------------")
func4()
# my_var = func1(func3)
# my_var()
