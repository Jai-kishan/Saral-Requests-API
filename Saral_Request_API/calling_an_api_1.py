import requests

saral_url=("http://saral.navgurukul.org/api/courses")
def request(url):
	response=requests.get(url)
	with open("courses.json","wb") as file:
		file.write(response.content)
	return response.json()

print(type(request(saral_url)))
