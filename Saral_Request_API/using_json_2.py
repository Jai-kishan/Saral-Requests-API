import requests

#The JSON module is mainly used to convert the python dictionary above into a JSON string that can be written into a file.
#While the JSON module will convert strings to Python datatypes,
#normally the JSON functions are used to read and write directly from JSON files.A
import json

import os #The OS module in python provides functions for interacting with the operating system.

saral_url=("http://saral.navgurukul.org/api/courses")
def request(url):
	response=requests.get(url)
	#The best way to do this is using the withstatement.
	#This ensures that the file is closed when the block inside with is exited.
	with open("courses.json","wb") as file:
		file.write(response.content)
	return response.json()

def read_file():
	with open('courses.json',"r") as file:
		data_read=file.read()
		data_load=json.loads(data_read)
	
	available_courses=data_load['availableCourses']
	for index in range(len(available_courses)):
		courses=available_courses[index]
		course_name=courses['name']
		print(index,course_name)


if os.path.exists("./courses.json"):
	read_file()
else:
	request(saral_url)
	read_file()
