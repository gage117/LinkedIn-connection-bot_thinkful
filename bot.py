from webbot import Browser
import time

web = Browser()
web.go_to('linkedin.com')
web.click('Sign in')
time.sleep(1)
web.type('User123' , into='username' , id='username') #!!! Enter your username as first argument
web.click('NEXT' , tag='input')
web.type('Password123' , into='password') #!!! Enter your password as second argument
web.click('Sign in')
web.go_to('https://www.linkedin.com/school/thinkful/people/')

can_continue_scrolling = True
counter = 85 #!! Set to 85 for headroom to add manual connections as well. LinkedIn sets invitation restrictions at 100 connection invites in a day. Hitting this multiple times in a day gets your account flagged for a few days, adjust if needed.

while counter > 0:
	try:
		web.click('Connect')
		web.click('Add a note')
		#!!! Change intro message in next line, it's best to send these out with something different than others have used
		web.type('Hi! I\'m a Thinkful Software Engineering grad looking to expand my connections and would love to connect!' , into='textarea' , id='custom-message')
		web.click('Send invitation')
		counter -= 1
		can_continue_scrolling = True
	except:
		web.scrolly(980) #!!! Adjust scroll height if needed (pixels)
		if (can_continue_scrolling == False):
			looping = False
		else:
			can_continue_scrolling == True

print('>>>> Connection crawler complete')