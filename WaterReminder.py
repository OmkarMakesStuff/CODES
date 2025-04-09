# C:\Users\KEEDAA\AppData\Local\Programs\Python\Python313
# pipreqs . --force
import time
import os
from plyer import notification

print('Welcome to Water Reminder!')
print('This program will remind you to drink 500ml water every hour!')
print('How many litres of water do you need in a day?')
user_litre = input('Enter number of litres (1-9): ')

user_litre = int(user_litre)
total_ml = user_litre * 1000
ml_left = total_ml
print(f'I will remind you to drink 500 Ml every hour for the next {user_litre * 2} hours')
notification.notify(
        title="Let's get started!",
        message="💧 Achieve your daily intake! 💧",
        app_name="Python Script",
        timeout=3  
)
def reminder(ml_left):
    notification.notify(
        title="Drink 500Ml Water!",
        message=f"You need {ml_left} ml more for the day!",
        app_name="Python Script",
        timeout=6  
    )
    
    
time.sleep(5)
i = user_litre * 2
while i > 0:
    reminder(ml_left)
    time.sleep(5)
    i = i - 1
    ml_left = ml_left - 500
print(f"Congratulations! You have completed {user_litre} litres today!")
exit()