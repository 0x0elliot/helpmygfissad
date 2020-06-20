import os
import praw
import time
import random
import smtplib
import getpass

#If you're editing the code to make it easier then just follow the commments
input('''
I see you have messed up and now your girlfriend is mad at you or She is just geniunely having a bad day because of something else.''')

input('\nEither ways, Don\'t worry though fam. Let me help you out.')

print('\nEditing the code to make your experience better is heavily appreciated.\n')
print()
def requirements():
	global service,reddit, client_secret, username, password, user_agent, subject, cute_list, actual_email, actual_password, reciever_email
	#The reddit API shit, You can get it all from here: https://www.reddit.com/prefs/apps
	
	client_id=input('Enter your client id: ') #Replace right handside with your client id here
	client_secret=input('Enter your client\'s secret: ')    #Replace right handside with your client's secret here
	username=input('Enter your reddit username: ')  #Replace right handside with your username here
	password=getpass.getpass('Enter your reddit password: ')  #Replace right handside with your password here
	
	reddit= praw.Reddit(client_id=client_id,
	client_secret=client_secret,
	username=username,
	password=password,
	user_agent=username)

	subject='Listen here you lil cutie'   #Enter subject 

	cute_list=['babyelephantgifs','stuffoncats', 'puppysmiles', 'cats','cute','aww','catloaf','tuckedinkitties'] #Edit this list. It has all the subreddits.

	actual_email= input('Enter your actual email:		') #Enter the email address you will be using.
	actual_password= getpass.getpass('Enter your actual password:	') #Enter your password/App password.
	reciever_email= input('Enter your lover\'s email:		')  #Enter reciever's email
	service='smtp.gmail.com' #If you use any other service then change this code accordingly. Ex: If you use outlook, then change it to 'smtp.outlook.com'
	#That's all you needed to edit. Now you can chill out fam I gottchu. Expect her to be fucking melted. 

def collect_cute_stuff():
	global body
	total=len(cute_list)
	list1=[]
	goodtogo='no'
	while(goodtogo!='y'):
		print('Fetching cute links..\n')
		try:
			for i in range(len(cute_list)):
				print('\nFetching from r/', cute_list[i])
				now=i+1
				print('Total Progress: ',(now/total)*100,'%\n')
				subreddit= reddit.subreddit(cute_list[i])
				hot_cute= subreddit.hot(limit=10)
				count=0
				for submissions in hot_cute:
					if(count!=1):
						list1.append('www.reddit.com'+submissions.permalink)
					count+=1
			goodtogo='y'
		except Exception as e:
			print('''
		Guess an error happened..

		Error:''', e,
			'''
		Retrying..
		''')
			goodtogo='no'
	print('Crafting a message with love..')
    #Edit the message if you wish to.
	body='''Hey..I know you are not feeling well. So here. Take a look at these cute lil tings.

	Cute lil tings:\n''' 
	print(list1)
	for j in range(len(list1)):
		body+=list1[j]+'\n'
	print()
	print('Message crafted..')
	print()
	msg= f'Subject: {subject}\n\n{body}'

def send_email():
	print('Connecting to your email..')
	s=smtplib.SMTP(host=service, port=587)
	s.ehlo()
	s.starttls()
	s.ehlo()
	s.login(actual_email, actual_password)
	msg= f'Subject: {subject}\n\n{body}'
	print('Logged in..')
	s.sendmail(actual_email, reciever_email, msg)
	print('Email sent successfully..')
requirements()
collect_cute_stuff()
send_email()
print()
