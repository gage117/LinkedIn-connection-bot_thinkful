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

looping = True
can_continue_scrolling = True

while looping == True:
	try:
		web.click('Connect')
		web.click('Add a note')
		#!!! Change intro message in next line, it's best to send these out with something different than others have used
		web.type('Hi! I\'m a Thinkful Software Engineering grad looking to expand my connections and would love to connect!' , into='textarea' , id='custom-message')
		web.click('Send invitation')
		can_continue_scrolling = True
	except:
		web.scrolly(980) #!!! Adjust scroll height if needed (pixels)
		if (can_continue_scrolling == False):
			looping = False
		else:
			can_continue_scrolling == True

print('>>>> Connection crawler complete')