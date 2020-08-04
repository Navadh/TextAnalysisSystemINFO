# import pymysql
#
# # tasdb=pymysql.connect('118.24.85.183', 'root', 'aichou123@AICHOU123','tasdb')
# #
# # cursor=tasdb.cursor()
# # sql="select ttasname, count(*) as total from ttasys group by ttasname having total>0 order by total asc"
# # # sql="select ttasname, count(*) as total from ttasys group by ttasname having total>0"
# #
# # # sql="select ttasname, count(*) from ttasys group by ttasname"
# # # sql="select * from ttasys where ttasname='xyz'"
# # command=cursor.execute(sql)
# # results=cursor.fetchall()
# # # cursor.execute('select version()')
# # # data=cursor.fetchone()
# #
# # #print('Database version:%s'%data)
# # # print('ttasid \t ttasname  \t\t\t ttasmemo \t\t ttasdate  \t\t\t\t ttasnum')
# # print("ttasname \t\t total")
# # # print("ttasname \t\t count")
# # print('-----------------------------------------------------------------------------')
# #
# # for row in results:
# #     print(str(row[0])+"\t\t\t" + str(row[1]))
# # cursor.close()
# # results=""
# # tasdb.close()
#
#
#
# # tasdb=pymysql.connect('localhost', 'root', 'NavINFO5717TX','tasdb')
# #
# # cursor=tasdb.cursor()
# # sql="select * from ttasys where ttasname like %s"
# # values="%n%"
# # command=cursor.execute(sql, values)
# # results=cursor.fetchall()
# # # cursor.execute('select version()')
# # #data=cursor.fetchone()
# #
# # #print('Database version:%s'%data)
# # print('ttasid \t ttasname  \t\t\t ttasmemo \t\t ttasdate  \t\t\t\t ttasnum')
# # print('-----------------------------------------------------------------------------')
# #
# # for row in results:
# #     print(str(row[0])+"\t\t"+row[1]+"\t\t\t"+row[2]+"\t\t"+str(row[3])+"\t\t"+str(row[4]))
# # cursor.close()
# # results=""
# # # tasdb.commit()
# # tasdb.close()
#
# tasdb=pymysql.connect('118.24.85.183', 'root', 'aichou123@AICHOU123','tasdb')
#
# cursor=tasdb.cursor()
# # sql="delete from ttasys where ttasid=%s"
# # values=int(input("Please input an id you wnat to delete: "))
#
# # sql="update ttasys set ttasname=%s where ttasid=%s"
# # values=("BIG", 8)
#
# # sql="insert into ttasys(ttasname, ttasmemo, ttasdate, ttasnum) values(%s, %s, %s, %s)"
# # values=("ABC", "Visitor", "2020-06-23", 5717)
# # command=cursor.execute(sql, values)
# # results=cursor.fetchall()
# cursor.execute('select version()')
# data=cursor.fetchone()
#
# print('Database version:%s'%data)
# # print('ttasid \t ttasname  \t\t\t ttasmemo \t\t ttasdate  \t\t\t\t ttasnum')
# # print('-----------------------------------------------------------------------------')
#
# #for row in results:
# #    print(str(row[0])+"\t\t"+row[1]+"\t\t\t"+row[2]+"\t\t"+str(row[3])+"\t\t"+str(row[4]))
#
# # results=""
#
# cursor.close()
# # tasdb.commit()
#
# tasdb.close()

# import turtle
# def draw_multicolor_square(animal, size):
#     for i in ["red", "green", "blue", "black"]:
#         animal.color(i)
#         animal.forward(size)
#         animal.left(90)
#
# window = turtle.Screen()
# window.bgcolor("lightgreen")
# window.title("Multicolor Squares")
#
# Artist=turtle.Turtle()
# Artist.pensize(4)
#
# size=150
# for i in range(15):
#     draw_multicolor_square(Artist,size)
#     size-=10
#     Artist.forward(10)
#     Artist.right(18)
#
# window.mainloop()

# import turtle
# def draw_polygon(x,y):
#     for i in range(100):
#         x.forward(y)
#         x.left(10)
# window=turtle.Screen()
# window.bgcolor("lightblue")
# window.title("Polygon!")
#
# Polygon=turtle.Turtle()
# draw_polygon(Polygon,100)
# window.mainloop()

# import math
# def circle_stats(r):
#     circumference=2*math.pi*r
#     area=math.pi*r*r
#     return (circumference,area)
# print(circle_stats(2))

# horsemen=["war","famine", "pestilence", "death"]
# print(len(horsemen))
# for i in range(len(horsemen)):
#     print(horsemen[i])

# friends=["Joe", "Zoe", "Brad", "Angelina", "Paris"]
# for (i, friend) in enumerate(friends):
#     print(i, friend)

# mylist=[]
# mylist.append(5)
# mylist.append(9)
# mylist.append(5)
# mylist.insert(1,8)
# print(mylist)
# mylist.count(5)

# english_spanish={}
# english_spanish["one"]="uno"
# english_spanish["two"]="dos"
#
# for key, value in english_spanish.items():
#     print("Got a key", key, "which maps to a value", value)

# value=300
# message="It costs %s dollars"
# print(message % value)
# spaces=' '*15
# print('%s Prince Charming' % spaces)
# def hello():
#     print("Hello there!")

# from future.moves import tkinter as tk
# window=tk.Tk()
# window.mainloop()

# btn=Button(tk, text="Click Me!", command=hello)
# btn.pack()

# canvas=Canvas(tk, width=500, height=500)
# canvas.pack()
# canvas.create_line(0,0,500,500)
# try:
#     x = input("Give me a number: ")
#     x = int(x)
#
#     y = input("Give me another number: ")
#     y = int(y)
#
# except ValueError:
#     print("Sorry, I really needed a number.")
#
# else:
#     sum = x + y
#     print("The sum of " + str(x) + " and " + str(y) + " is " + str(sum) + ".")
# first_name = "ada"
# last_name = "lovelace"
# full_name = first_name + " " + last_name
#
# message = "Hello, " + full_name.title() + "!"
# print(message)
# name = "\tEric Matthes\n"
#
# print("\nUsing strip():")
# print(name.strip())
# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# message = "My first bicycle was a " + bicycles[0].title() + "."
#
# print(message)
# cars = ['bmw', 'audi', 'toyota', 'subaru']
#
# print("Here is the original list:")
# print(cars)
#
# print("\nHere is the sorted list:")
# print(sorted(cars))
#
# print("\nHere is the reverse alphabetical list:")
# print(sorted(cars, reverse=True))
#
# print("\nHere is the original list again:")
# print(cars)
# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)
#
# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print("\nA " + too_expensive.title() + " is too expensive for me.")
# Invite some people to dinner.
# guests = ['guido van rossum', 'jack turner', 'lynn hill']
#
# name = guests[0].title()
# print(name + ", please come to dinner.")
#
# name = guests[1].title()
# print(name + ", please come to dinner.")
#
# name = guests[2].title()
# print(name + ", please come to dinner.")
#
# name = guests[1].title()
# print("\nSorry, " + name + " can't make it to dinner.")
#
# # Jack can't make it! Let's invite Gary instead.
# del(guests[1])
# guests.insert(1, 'gary snyder')
#
# # Print the invitations again.
# name = guests[0].title()
# print("\n" + name + ", please come to dinner.")
#
# name = guests[1].title()
# print(name + ", please come to dinner.")
#
# name = guests[2].title()
# print(name + ", please come to dinner.")
#
# # We got a bigger table, so let's add some more people to the list.
# print("\nWe got a bigger table!")
# guests.insert(0, 'frida kahlo')
# guests.insert(2, 'reinhold messner')
# guests.append('elizabeth peratrovich')
#
# name = guests[0].title()
# print(name + ", please come to dinner.")
#
# name = guests[1].title()
# print(name + ", please come to dinner.")
#
# name = guests[2].title()
# print(name + ", please come to dinner.")
#
# name = guests[3].title()
# print(name + ", please come to dinner.")
#
# name = guests[4].title()
# print(name + ", please come to dinner.")
#
# name = guests[5].title()
# print(name + ", please come to dinner.")
#
# # Oh no, the table won't arrive on time!
# print("\nSorry, we can only invite two people to dinner.")
#
# name = guests.pop()
# print("Sorry, " + name.title() + " there's no room at the table.")
#
# name = guests.pop()
# print("Sorry, " + name.title() + " there's no room at the table.")
#
# name = guests.pop()
# print("Sorry, " + name.title() + " there's no room at the table.")
#
# name = guests.pop()
# print("Sorry, " + name.title() + " there's no room at the table.")
#
# # There should be two people left. Let's invite them.
# name = guests[0].title()
# print(name + ", please come to dinner.")
#
# name = guests[1].title()
# print(name + ", please come to dinner.")
#
# # Empty out the list.
# del(guests[0])
# del(guests[0])
#
# # Prove the list is empty.
# print(guests)
# locations = ['himalaya', 'andes', 'tierra del fuego', 'labrador', 'guam']
#
# print("Original order:")
# print(locations)
#
# print("\nAlphabetical:")
# print(sorted(locations))
#
# print("\nOriginal order:")
# print(locations)
#
# print("\nReverse alphabetical:")
# print(sorted(locations, reverse=True))
#
# print("\nOriginal order:")
# print(locations)
#
# print("\nReversed:")
# locations.reverse()
# print(locations)
#
# print("\nOriginal order:")
# locations.reverse()
# print(locations)
#
# print("\nAlphabetical")
# locations.sort()
# print(locations)
#
# print("\nReverse alphabetical")
# locations.sort(reverse=True)
# print(locations)

# dimensions = (200, 50)
# print("Original dimensions:")
# for dimension in dimensions:
#     print(dimension)
# even_numbers = list(range(2,11,2))
# print(even_numbers)
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]
#
# my_foods.append('cannoli')
# friend_foods.append('ice cream')
#
# print("My favorite foods are:")
# print(my_foods)
#
# print("\nMy friend's favorite foods are:")
# print(friend_foods)
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician.title() + ", that was a great trick!")
#     print("\tI can't wait to see your next trick, " + magician.title() + ".\n")
#
# print("Thank you everyone, that was a great magic show!")
#
# numbers = list(range(1,6))
# print(numbers)
# squares = []
# for value in range(1, 11):
#     square = value ** 2
#     squares.append(square)
#
# print(squares)
# def hello():
#     print("Hello there!")
# from future.moves import tkinter
# from tkinter import *
# tk=Tk()
# # window=tkinter.Tk()
# btn=Button(tk, text="Click Me!", command=hello)
# btn.pack()
# btn.mainloop()
# window.mainloop()
# window=tk.Tk()
# window.mainloop()

# numbers = list(range(1, 1000001))
#
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))
# cubes = []
# for number in range(1, 11):
#     cube = number**3
#     cubes.append(cube)
#     print(cubes)
# cubes = [number**3 for number in range(1,11)]
# print(cubes)
# cars = ['audi', 'bmw', 'subaru', 'toyota']
#
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())
# usernames = ['eric', 'willie', 'admin', 'erin', 'ever']
#
# for username in usernames:
#     if username == 'admin':
#         print("Hello " + username.upper() + ", would you like to see a status report?")
#     else:
#         print("Hello " + username.title() + ", thank you for logging in again!")
#
# current_users = ['eric', 'willie', 'admin', 'erin', 'Ever']
# new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']
#
# current_users_lower = [user.lower() for user in current_users]
# print(current_users_lower)
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original position: " + str(alien_0['x_position']))

# Move the alien to the right.
# Figure out how far to move the alien based on its speed.
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     # This must be a fast alien.
#     x_increment = 3
#
# # The new position is the old position plus the increment.
# alien_0['x_position'] = alien_0['x_position'] + x_increment
#
# print("New position: " + str(alien_0['x_position']))
# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
# for alien_number in range(0, 30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
#
# for alien in aliens[0:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
#     elif alien['color'] == 'yellow':
#         alien['color'] = 'red'
#         alien['speed'] = 'fast'
#         alien['points'] = 15
#
# # Show the first 5 aliens:
# for alien in aliens[0:30]:
#     print(alien)
# print("...")

#
# users = {'aeinstein': {'first': 'albert',
#                        'last': 'einstein',
#                        'location': 'princeton'},
#          'mcurie': {'first': 'marie',
#                     'last': 'curie',
#                     'location': 'paris'},
#          }
#
# for username, user_info in users.items():
#     print("\nUsername: " + username)
#     full_name = user_info['first'] + " " + user_info['last']
#     location = user_info['location']
#
#     print("\tFull name: " + full_name.title())
#     print("\tLocation: " + location.title())
# Store information about a pizza being ordered.
# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
#     }
#
# # Summarize the order.
# print("You ordered a " + pizza['crust'] + "-crust pizza " +
#       "with the following toppings:")
#
# for topping in pizza['toppings']:
#     print("\t" + topping)
# class Critter:
#     def __init__(self, name):
#         print("A new Critter has been born!")
#         self.name = name
#     def __str__(self):
#         rep = "Critter Object\n"
#         rep +="Name: " + self.name + "\n"
#         return rep
#     def talk(self):
#         print("Hi! I'm", self.name, '\n')
# crit = Critter("Rudolph")
# crit.talk()
# print("Printing crit:")
# print(crit)
# print("Directly accessing crit.name:")
# print(crit.name)
# input("\n\nPress any key to exit")

