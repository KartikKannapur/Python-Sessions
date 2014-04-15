import os
import datetime

def text_to_speech(text):
	return os.system("espeak  -s 155 -a 200 "+text+" " )
	
	
def choice():	
	option = raw_input("Would you like to listen to \na) Pre-defined String \nb) Current Time \n Your Choice :")


	#Function Call
	if(option == 'a'):
		text_to_speech("'Good Evening Everybody! I Like Programming In Python.This is a text to speech converter.'")

	elif(option == 'b'):
		#String Formatting in Hours and Minutes
		m = datetime.datetime.now().strftime("%I %M %S")
		text_to_speech("'Greetings! The Current time is"+str(int(m[0:2]))+" "+str(int(m[3:5]))+" : ' ")

	
choice()
