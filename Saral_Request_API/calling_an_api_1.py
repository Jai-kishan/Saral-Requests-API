#Requests is a Python HTTP library, released under the Apache2 License.
# The goal of the project is to make HTTP requests simpler and more human-friendly.
import requests
#pprint — Data pretty printer. 
#The pprint module provides a capability to “pretty-print” arbitrary Python data structures in a form which can be used as input to the interpreter.
from pprint import pprint

saral_url=("http://saral.navgurukul.org/api/courses")  # Global variable storing api
def request(url):
	#GET is by far the most used HTTP method. We can use GET request to retrieve data from any destination
	response=requests.get(url)
	#All the information about our request is now stored in a Response object called response. 
	with open("courses.json","wb") as file:
		file.write(response.content)
	#The Requests library comes with one built-in JSON parser and we can use requests.get('url').json() to parse it as a JSON object.
	return response.json()

#Calling request()
pprint(request(saral_url))
