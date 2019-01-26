import requests
import json
import os

saral_url=("http://saral.navgurukul.org/api/courses")
def request(url,f_write):
	response=requests.get(url)
	with open(f"{f_write}.json","wb") as file:
		file.write(response.content)
	return response.json()
	
course_id_list=[]

def read_file(f_read):
	with open(f'{f_read}',"r") as file:
		data_read=file.read()
		data_load=json.loads(data_read)
	return(data_load)

def saral_courses():
	data_load=read_file("courses.json")
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

slug=[]
def get_exercise():
	data_load=read_file(f"{exercise_path}.json")
	exercise_data=data_load['data']
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

# def get_slug():
	





if os.path.exists("./courses.json"):
	saral_courses()
	exercises_id=select_course()

	exercise_path=(f"request_data/Courses_Exercise/exercise_{exercises_id}")
	print(exercise_path)
	if os.path.exists(f"{exercise_path}.json"):
		get_exercise()
		# ######
		# slug_store=(f"request_data/Exercise_slug/exercise_{exercises_id}")
		# os.mkdir(slug_store)
		# print("yes....")
		for index in slug:
			slug_url=request(f"{saral_url}/{exercises_id}/exercise/getBySlug?slug={index}")
		# 	print(slug_url)
		# 	print("yes")


	else:
		request(f"{saral_url}/{exercises_id}/exercises",exercise_path)
		get_exercise()
		print("no")
else:
	request(saral_url,"courses")
	saral_courses()
	select_course()
	print("nooo")