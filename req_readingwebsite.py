#Add Package
import requests

#Prepare URL
url="https://api.github.com/users/mohsind"

#Web REST API Calls (GET- HTTP VERB) Request
#response=requests.get(url,params={k:v},args)
r=requests.get(url)

#Fetch Reponse Content
print(r.content)