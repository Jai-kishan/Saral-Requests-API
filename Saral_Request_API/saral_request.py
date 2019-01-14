#Requests is a python module that you can use to send all kinds of HTTP requests
import requests

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
from pprint import pprint 
# pprint(saral_data)


# URL of the saral API to be downloaded is defined as response
response=requests.get(saral_api) # create HTTP response object
# send a HTTP request to the server and save 
# the HTTP response in a response object called response
with open("users.json","wb") as file:
	 # Saving received content as a json file in 
     # binary format 


    # write the contents of the response (response.content) 
    # to a new file in binary mode. 
	file.write(response.content)

