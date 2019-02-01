import requests, json , os

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

course_id_list=[]
def saral_courses():
	print ("\n\n************************  WELCOME  TO  SARAL  *************************************\n\n")
	data_load=read_file("courses.json")
	available_courses=data_load['availableCourses']
	for index in range(len(available_courses)):
		courses=available_courses[index]
		course_name=courses['name']
		courses_id=courses['id']
		print(index+1,courses_id,course_name)
		course_id_list.append(courses_id)

def space():
  print ("\n\n------------------------------------------------------------------------------------------\n\n")

def select_course():
	space()
	print("\nChoose the Course number which you want to learn:- \n\n")
	user_input=int(input("Your answer : "))
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

def store_exe_data():
	for i in range(len(slug)):
		slug_url=request(f"{saral_url}/{exercises_id}/exercise/getBySlug?slug={slug[i]}",slug_store+"/"+again_slug[i])

def content():
	var=0
	while True:
		content=read_file(f"{slug_store}/{again_slug[var]}.json")
		store_content=content['content']
		print(store_content)
		space()
		user_in=input("Enter 'n' to go to next exercise or 'p' to go to previous exercise or to exit press 'x' key : ")
		if user_in=="x" or user_in== "X":
			exit()
		if user_in=='p' or user_in== "P":
			if var>0:
				var-=1
			else:
				print("There is no previous exercise content!")
				if var==0:
					user_inp=input("""If you want to exit:- press "x" if u want to read continue press "any" key...""")
					if user_inp=="x":
						exit()
		elif user_in=='n' or user_in=="N":
			var+=1

if os.path.exists("./courses.json"):
	saral_courses()
	exercises_id=select_course()
	exercise_path=(f"request_data/Courses_Exercise/exercise_{exercises_id}")

	if os.path.exists(f"{exercise_path}.json"):
		get_exercise()
		slug_store=(f"request_data/Exercise_slug/exercise_{exercises_id}")

		if os.path.isdir(slug_store):
			content()
		else:
			os.mkdir(slug_store)
			store_exe_data()
			content()		
	else:
		request(f"{saral_url}/{exercises_id}/exercises",exercise_path)
		get_exercise()
		slug_store=(f"request_data/Exercise_slug/exercise_{exercises_id}")
		os.mkdir(slug_store)
		store_exe_data()
		content()
else:
	#This code run only one time when you have no any offline data
	request(saral_url,"courses")
	saral_courses()
	exercises_id=select_course()
	exercise_path=(f"request_data/Courses_Exercise/exercise_{exercises_id}")
	request(f"{saral_url}/{exercises_id}/exercises",exercise_path)
	get_exercise()
	slug_store=(f"request_data/Exercise_slug/exercise_{exercises_id}")
	os.mkdir(slug_store)
	store_exe_data()
	content()