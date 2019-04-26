import requests
import json
import os

saral_url=("http://saral.navgurukul.org/api/courses")
def request(url):
	response=requests.get(url)
	with open("courses.json","wb") as file:
		file.write(response.content)
	return response.json()

# id_list is a varible in which a new list is assigned to store id of the courses.		
course_id_list=[]

def read_file():
	with open('courses.json',"r") as file:
		data_read=file.read()
		data_load=json.loads(data_read)

	available_courses=data_load['availableCourses']
	for index in range(len(available_courses)):
		courses=available_courses[index]
		course_name=courses['name']
		courses_id=courses['id']
		print(index+1,courses_id,course_name)
		course_id_list.append(courses_id)	

def select_course():
	user_input=int(input("\n\nselect your course list number:- "))
	select_id=course_id_list[user_input-1]
	return (f"\t\nAapne jo course {user_input} select kiya hai us course ki ID {select_id} hai")


if os.path.exists("./courses.json"):
	read_file()
	print(select_course())
else:
	request(saral_url)
	read_file()
	print(select_course())
