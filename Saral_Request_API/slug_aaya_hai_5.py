import requests
import json
import os

saral_url=("http://saral.navgurukul.org/api/courses")
def request(url,f_write):
	response=requests.get(url)
	with open(f"{f_write}.json","wb") as file:
		file.write(response.content)
	return response.json()

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
again_slug=[]
def get_exercise():
	data_load=read_file(f"{exercise_path}.json")
	exercise_data=data_load['data']
	for i in range(len(exercise_data)):
		exercise_name=exercise_data[i]['name']
		exercise_slug=exercise_data[i]['slug']
		slug_replace=exercise_slug.replace("/","_")
		parent_exercise=exercise_data[i]['parentExerciseId']
		child_exercise=exercise_data[i]['childExercises']
		print(i+1,exercise_name)
		slug.append(exercise_slug)
		again_slug.append(slug_replace)

		for j in range(len(child_exercise)):
			child_exercise_name=child_exercise[j]['name']
			child_exercise_slug=child_exercise[j]['slug']
			child_slug_replace=child_exercise_slug.replace("/","_")
			print("\t*"+str(child_exercise_name))
			slug.append(child_exercise_slug)
			again_slug.append(child_slug_replace)

def store_exe_content():
	for i in range(len(slug)):
		slug_url=request(f"{saral_url}/{exercises_id}/exercise/getBySlug?slug={slug[i]}",slug_store+"/"+again_slug[i])
		content=read_file(f"{slug_store}/{again_slug[i]}.json")
	return content

while True:
	if os.path.exists("./courses.json"):
		saral_courses()
		exercises_id=select_course()
		# print("a-jai")

		exercise_path=(f"request_data/Courses_Exercise/exercise_{exercises_id}")
		if os.path.exists(f"{exercise_path}.json"):
			get_exercise()
			# print("b-jai")

			slug_store=(f"request_data/Exercise_slug/exercise_{exercises_id}")
			if os.path.isdir(slug_store):
				# print("c-jai")
				pass
			else:
				os.mkdir(slug_store)
				store_exe_content()
				print("q-jai")

		else:
			request(f"{saral_url}/{exercises_id}/exercises",exercise_path)
			get_exercise()
			slug_store=(f"request_data/Exercise_slug/exercise_{exercises_id}")
			os.mkdir(slug_store)
			a = store_exe_content()
			print("w-jai")	
	else:
		request(saral_url,"courses")
		saral_courses()
		exercises_id=select_course()
		exercise_path=(f"request_data/Courses_Exercise/exercise_{exercises_id}")
		request(f"{saral_url}/{exercises_id}/exercises",exercise_path)
		get_exercise()
		slug_store=(f"request_data/Exercise_slug/exercise_{exercises_id}")
		os.mkdir(slug_store)
		store_exe_content()
		print("e-jai")