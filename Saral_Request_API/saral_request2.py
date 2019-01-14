#Requests is a python module that you can use to send all kinds of HTTP requests
import requests
from pathlib import Path
from pprint import pprint 


#Now, here we are stored the "Saral API" in a "url" variable.
saral_api=("http://saral.navgurukul.org/api/courses")


#Requests is very easy method to send an HTTP request using Requests.
#You begin by importing the module and then make the request. Here is an example:
def request(url):
	#GET is by far the most used HTTP method. We can use GET request to retrieve data from any destination
	response = requests.get(saral_api)
	#All the information about our request is now stored in a Response object called response. 
	return response.json()
	#The Requests library comes with one built-in JSON parser and we can use requests.get('url').json() to parse it as a JSON object.

# print(request(saral_api))
saral_data=request(saral_api)

'''
The pprint module provides a capability to “pretty-print” arbitrary
Python data structures in a well-formatted and more readable way!
'''
# pprint(saral_data)


#step-2
course_id_list=[]
saral_course=saral_data['availableCourses']

file = Path("courses.json")
if file.exists():
	pass
else:
	# URL of the saral API to be downloaded is defined as response
	response=requests.get(saral_api) # create HTTP response object
	# send a HTTP request to the server and save 
	# the HTTP response in a response object called response
	with open("courses.json","wb") as file:
	 # Saving received content as a json file in 
     # binary format 

    	# write the contents of the response (response.content) 
    	# to a new file in binary mode. 
		file.write(response.content)

for index in range(len(saral_course)):
	course=saral_course[index]
	course_name=course['name']
	course_id=course['id']
	print(index,course_name)
	course_id_list.append(course_id)



def select_course():
	user_input=int(input("\n which course in you want to Enroll:- "))
	choose_course=course_id_list[user_input]
	return(choose_course)

courses_id=select_course()
source = requests.get('{}/{}/exercises'.format(saral_api,courses_id))
all_exercises =(source.json())

exercise=all_exercises['data']
exercise_store= "exercise_"+str(courses_id)+".json"

with open(exercise_store,"wb") as file1:
	file1.write(source.content)


list_exercise_id=[]
slug_list=[]
for index in range(len(exercise)):
	new_exercise=exercise[index]

	parent_exercise=new_exercise['parentExerciseId']
	exercise_name=new_exercise['name']
	slug=new_exercise['slug']
	slug_list.append(slug)

for i in range(len(slug_list)):
	print(slug_list[i])

new_user=int(input('enter'))
slug2_list=slug_list[new_user]
urldemo = "{}/{}/exercise/getBySlug?slug={}".format(saral_api,courses_id,slug2_list)
print (urldemo)
dataslug = requests.get(urldemo)
print (dataslug.text)