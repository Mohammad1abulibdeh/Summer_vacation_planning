import random
import time


def sorry(name):
    print(name)

def one():
    print("Monday: Art workshop - Creating a watercolor painting")
    time.sleep(1)
    print ("Tuesday: Bedtime story reading - Adventures of the Little Animals")
    time.sleep(1)
    print ("Wednesday: Outdoor sports activity - Playing soccer")
    time.sleep(1)
    print("Thursday: Numbers learning workshop - Creating paper games for counting")
    time.sleep(1)
    print("Friday: Role-playing session - Imagine a fantasy story and participate in it")
def two():
    print("Monday: Creative writing session - Crafting short stories or poems")
    time.sleep(1)
    print("Tuesday: Science experiment day - Hands-on activities exploring various scientific concepts")
    time.sleep(1)
    print("Wednesday: Outdoor adventure - Hiking and nature exploration")
    time.sleep(1)
    print("Thursday: Artistic expression workshop - Painting or drawing based on personal themes")
    time.sleep(1)
    print("Friday: Book club meeting - Discussing and analyzing a chosen novel or book")
    time.sleep(1)
    print("Saturday: Coding and technology session - Learning basic coding concepts or creating ") 
def th():
    print("Monday: Professional development workshop - Resume building and interview skills")
    time.sleep(1)
    print("Tuesday: Fitness and wellness session - Yoga and mindfulness meditation")
    time.sleep(1)
    print("Wednesday: Creative expression class - Photography or painting workshop")
    time.sleep(1)
    print("Thursday: Discussion forum on current affairs - Debating relevant social and political topics")
    time.sleep(1)
    print("Friday: Networking event - Social gathering for connecting with peers and professionals")
    time.sleep(1)
    print("Saturday: Skill-sharing workshop - Sharing practical skills like cooking, DIY, or financial management")
    time.sleep(1)
    print("Sunday: Movie or documentary night - Screening and discussion of thought-provoking films")
name = input("what is your name ")
age = int (input ("What year were you born? "))
age1 = 2023 - age
print("hello ",name,"you are ",2023 - age)

if age1 <= 4:    
    print("sorry but we dont have activity for this age ")
    exit()
if age1 < 11 and age1 >= 5:
    print ("We will give you this weekly program ")
    one()
if age1 < 19 and age1 >= 11:
    print ("We will give you this weekly program ")
    two()
if age1 < 25 and age1 >= 19:
    print ("We will give you this weekly program ")
    th()

ss = input ("Do you like this weekly program?")

if ss == "no":
    random.choice([one(), two(), th()])
else:
    print("you can rate this program of 5 stars ")
stars = int(input ("rate = "))
if stars == 0:
    print("We are sorry",",", sorry(name), "for our service ")
if stars == 1:
    print("We are sorry",",", sorry(name), "for our service  ")
if stars == 2:
    print("We are sorry",",", sorry(name), "for our service ")
if stars >= 3:
    print("Because you liked our service for the summer vacation in your week, we will try to create more of these weekly programs in the summer vacation")
import turtle
t=turtle.Turtle()
t.pencolor("orange")
t.pensize(20)
t.penup()
t.left(90)
t.back(50)
t.left(45)
t.pendown()
t.fd(150)

for r in range (180):
    t
    t.fd(1)
    t.right(1)
    
t.fd(1)
t.pencolor("red")
t.left(90)
t.fd(1)
for r in range(180):
    
    t.right(1)
    t.fd(1)
    

t.fd(150)
t.penup()
t.fd(10000)
turtle.done()