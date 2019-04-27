import requests

#The JSON module is mainly used to convert the python dictionary above into a JSON string that can be written into a file.
#While the JSON module will convert strings to Python datatypes,
#normally the JSON functions are used to read and write directly from JSON files.
import json

import os #The OS module in python provides functions for interacting with the operating system.

saral_url=("http://saral.navgurukul.org/api/courses")
def request(url):
	response=requests.get(url)
	#The best way to do this is using the withstatement.
	#This ensures that the file is closed when the block inside with is exited.
	with open("courses.json","wb") as file:
	    # write the contents of the response (response.content) 
	    # to a new file in binary mode. 
		file.write(response.content)
	return response.json()
#Here we define a function for retrive the course name and ID form the server thorug give url.
def read_file():
	with open('courses.json',"r") as file:
		data_read=file.read()
		data_load=json.loads(data_read)
	
	available_courses=data_load['availableCourses']
	for index in range(len(available_courses)):
		courses=available_courses[index]
		course_name=courses['name']
		print(index,course_name)

#The most common way to check for the existence of a file in Python is using the  
#exists() and isfile() methods from the os.path module in the standard library.
if os.path.exists("./courses.json"):
	read_file()
else:	
	# calling the request() which retrive the data form the sarver
	request(saral_url)
	#calling the read() where I store the course name and ID
	read_file()
