import functools 

def decoratorexample():
	@functools.wraps(func)
	def wrapper():
		print('Hello World')
		func()
		print('Hello World 2')
	return wrapper

#HOW DO DECORATORS WORK:
#FIRST YOU DEFINE AN OUTER FIRST CLASS FUNCTION
#THEEN YOU DEFINE A WRAPPER IN WHICH YOU HAVE A SERIES OF COMMANDS AN ANOTHER FUNCTION.
#THE DECORATOR RETURNS THE WRAPPER OBJECT WITHOUT BEING CALLED
#IF YOU WANT TO CALL THE DECORATOR APPLIED TO EXTENDING ANOTHER FUNCTION YOU CAN EITHER:
def function_to_be_extended():
	print ('Hello World 0.5')

function_to_be_extended =  decoratorexample(function_to_be_extended)
#or
@decoratorexample

#both of this return an uncalled thing
#you can call it by saying function_to_be_extended()


#example
from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

def say_whee():
    print("Whee!")

say_whee = not_during_the_night(say_whee)
