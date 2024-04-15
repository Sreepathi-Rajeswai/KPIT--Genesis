#1addition,sub,mul,div
'''a,b=map(int,input().split())
print(a+b,a-b,a*b,a/b)'''
#2guess a number game
'''import random
c=random.randint(1,100)
t=0;player=0
while player!=c:
    player=int(input("enter"))
    t=t+1
    if player<c:
        print("too low")
    elif player>c:
        print("too high")
    else:print("correct you got",t,"times")'''
#g multiplication of any given number
'''n=int(input())
for i in range(1,11):
    if n>0:
        print(i*n)'''
#count number of words in a file
'''fin=open("C://Users/SREEPATHIR/Documents/lava/sana.txt")
for key in fin:
    w=key.split()
    print(len(w))'''
#f.rock,paper,sciesors
'''import random
n=input("")
c=["rock","paper","scissors"]
p=random.choice(c)
print(p)
if n==p:
    print("tie")
elif((n=="rock" and p=="scissors") or (n=="paper" and p=="rock") or (n=="scissors" and p=="paper")):
    print("you win")
else:print("you lose")'''
#i.add,view,delete
'''a)Build a simple calculator that can perform basic operations like addition, subtraction, multiplication,
 and division.'''
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Cannot divide by zero"
    else:
        return a/b
    
print("Select Operation:")
print("1:Add")
print("2:Subtract")
print("3:Multiply")
print("4:Divide")

#Take input from the user
choice=int(input("Enter Choice(1/2/3/4)"))
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))

if choice==1:
   print(add(a,b))
elif choice==2:
    print(subtract(a,b))
elif choice==3:
    print(multiply(a,b))
elif choice==4:
    print(divide(a,b))
else:
    print("Invalid Input")

'''b)Create a program that generates a random number and asks the user to guess it. 
Provide hints if the guess is too high or too low.'''
import random
num=random.randint(1,10)
guess=0
while guess!=num:
     guess=int(input("Guess a num between 1 and 10:"))
     if guess==num:
        print("Congratulations!!, Your guess is correct..")
        break
     else:
         print("Nope, sorry! Try again.")
   
'''c)Develop a to-do list application where users can add tasks, mark them as completed, and remove them. (in a file)'''
import json
 
def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks
 
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)
 
def add_task(task):
    tasks = load_tasks()
    tasks.append({'task': task, 'completed': False})
    save_tasks(tasks)
 
def mark_task_completed(task_index):
    tasks = load_tasks()
    if task_index < len(tasks):
        tasks[task_index]['completed'] = True
        save_tasks(tasks)
    else:
        print("Task index out of range.")
 
def remove_task(task_index):
    tasks = load_tasks()
    if task_index < len(tasks):
        del tasks[task_index]
        save_tasks(tasks)
    else:
        print("Task index out of range.")
 
def display_tasks():
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        status = "Completed" if task['completed'] else "Pending"
        print(f"{i+1}. {task['task']} - {status}")
 
while True:
    print("\n1. Add Task")
    print("2. Mark Task as Completed")
    print("3. Remove Task")
    print("4. View Tasks")
    print("5. Exit")
 
    choice = int(input("Enter your choice: "))
 
    if choice == 1:
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == 2:
        display_tasks()
        task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
        mark_task_completed(task_index)
    elif choice == 3:
        display_tasks()
        task_index = int(input("Enter the index of the task to remove: ")) - 1
        remove_task(task_index)
    elif choice == 4:
        display_tasks()
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")

'''d) Create a basic alarm clock that plays a sound or displays a message at a specified time.
import datetime
import time
#import winsound
def set_alarm(alarm_time,message):
    while True:
        current_time=datetime.datetime.now().strftime("%H:%M")
        if current_time==alarm_time:
            print(message)
            break
        time.sleep(60) #check every minute

alarm_time=input("Enter the alarm time in 24-Hour Format (HH:MM)")
message=input("Enter the message to display: ")
set_alarm(alarm_time, message)'''

'''e)Write a program that extracts information from a simple website. 
You can use libraries like requests for fetching the web page and BeautifulSoup for parsing HTML.
import requests
from bs4 import BeautifulSoup
#URL of the website to extract information from
url="www.example.com"
#send a GET request to the URL
response=requests.get(url)
#parse the HTML content of the website
soup=BeautifulSoup(response.content,'html.parser')
#Extract information from the website
#For example, to extract the title of the website
title=soup.title.text
#To extract all the links on the website by their class or id
links=soup.find_all('a')
for link in links:
    print(link.get('href'))'''

'''f)Implement a simple text-based game where the player chooses rock, paper, or scissors, and the computer does the same. 
Determine the winner based on the choices.'''
import random
 
def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        return get_user_choice()
    return user_choice
 
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])
 
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"
 
def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))
 
play_game()

'''g)Create a program that generates the multiplication table for a given number.'''
n=int(input("Enter a number:"))
for i in range(1,11,1):
    print(n,'*',i,'=',n*i)

'''h)Build a program that counts the number of words in a given text input.(from a file)'''
count=0
file=open("C://Users/THATIPELLIP/Desktop/files/demo.txt","r")
for line in file:
    words=line.split(" ")
    count=count+len(words)

print("Number of words in a given file",count)
file.close()

'''i)Create a basic calendar application that allows users to add, view, and delete events.'''
class calendar:
    def __init__(self):
        self.events={}
    
    def add_event(self,date,event):
        if date in self.events:
            self.events[date].append(event)
        else:
            self.events[date]=[event]

    def view_events(self,date):
        if date in self.events:
            print(f"Events on {date}")
            for event in self.events[date]:
                print(event)
        else:
            print(f"No events on {date}")

    def delete_event(self,date,event):
        if date in self.events and event in self.events[date]:
            self.events[date].remove(event)
            print(f"Event {event} deleted from {date}")
        else:
            print(f"No such event found on {date}")

calendar=calendar()
calendar.add_event("2024-01-01","New year's day")
calendar.add_event("2024-01-01","Family Gathering")
calendar.add_event("2024-01-13","sankranthi Festival")
calendar.add_event("2024-01-15","Birthday Party")

calendar.view_events("2024-01-01")
calendar.view_events("2024-01-13")
calendar.view_events("2024-01-15")

calendar.delete_event("2024-01-01","Family Gathering")
calendar.view_events("2024-01-01")

'''j)Write a program that converts currency between different exchange rates. 
(Use 5 different geographies) - Ask user for input and expected output geography.'''
class CurrencyConverter:
    def __init__(self):
        self.exchange_rates={'USD':{'EUR':0.82,'GBP':0.72,'JPY':103.42,'AUD':1.28},
                             'EUR':{'USD':1.22,'GBP':0.88,'JPY':126.24,'AUD':1.57},
                             'GBP':{'USD':1.39,'EUR':1.14,'JPY':143.93,'AUD':1.79},
                             'JPY':{'USD':0.0097,'EUR':0.0079,'GBP':0.0069,'AUD':0.012},
                             'AUD':{'USD':0.78,'EUR':0.64,'GBP':0.56,'JPY':84.53}}
    def convert_currency(self,amount,from_currency,to_currency):
        if from_currency in self.exchange_rates and to_currency in self.exchange_rates[from_currency]:
            converted_amount=amount*self.exchange_rates[from_currency][to_currency]
            return f"{amount} {from_currency} is equal to {converted_amount} {to_currency}"
        else:
            return "Invalid currency conversion"
        
converter=CurrencyConverter()
from_currency=input("Enter the currency you want to convert from (e.g: USD,EUR,GBP,JPY,AUD):")
to_currency=input("Enter the currency you want to convert to (e.g: USD,EUR,GBP,JPY,AUD):")
amount=float(input(f"Enter the amount in {from_currency}:"))
result=converter.convert_currency(amount,from_currency,to_currency)
print(result)

    



