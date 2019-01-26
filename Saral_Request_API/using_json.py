import requests
import json
import os

saral_url=("http://saral.navgurukul.org/api/courses")
def request(url):
	response=requests.get(url)
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
	print("KISH")