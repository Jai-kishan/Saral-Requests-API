import requests
import json
import os

saral_url=("http://saral.navgurukul.org/api/courses")
def request(url):
	response=requests.get(url)
	with open("courses.json","wb") as file:
		file.write(response.content)
	return response.json()

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
	return select_id


def get_exercise(ex_url):	
	response=requests.get(ex_url)
	with open(exercise_path,"wb") as file:
		file.write(response.content)		
	return response.json()

def read_exercise():
	exercise_data=data_load['data']
	slug=[]
	for i in range(len(exercise_data)):
		exercise_name=exercise_data[i]['name']
		exercise_slug=exercise_data[i]['slug']
		parent_exercise=exercise_data[i]['parentExerciseId']
		chile_exercise=exercise_data[i]['childExercises']
		print(i+1,exercise_name)
		slug.append(chile_exercise)

		for j in range(len(chile_exercise)):
			chile_exercise_name=chile_exercise[j]['name']
			chile_exercise_slug=chile_exercise[j]['slug']
			print("\t*"+str(chile_exercise_name))
			slug.append(chile_exercise_slug)


if os.path.exists("./courses.json"):
	read_file()
	exercises_id=select_course()
	exercise_api=(f"{saral_url}/{exercises_id}/exercises")
	exercise_path=(f"request_data/Courses_Exercise/exercises_{exercises_id}.json")
	get_exercise(exercise_api)
	with open(exercise_path,"r") as file:
		data_read=file.read()
		data_load=json.loads(data_read)	
	read_exercise()

else:
	request(saral_url)
	read_file()
