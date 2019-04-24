#Requests is a Python HTTP library, released under the Apache2 License.
# The goal of the project is to make HTTP requests simpler and more human-friendly.
import requests

saral_url=("http://saral.navgurukul.org/api/courses")  //# Global variable storing api
def request(url):
	#GET is by far the most used HTTP method. We can use GET request to retrieve data from any destination
	response=requests.get(url)
	#All the information about our request is now stored in a Response object called response. 
	with open("courses.json","wb") as file:
		file.write(response.content)
	#The Requests library comes with one built-in JSON parser and we can use requests.get('url').json() to parse it as a JSON object.
	return response.json()

#Calling request()
print(request(saral_url))
