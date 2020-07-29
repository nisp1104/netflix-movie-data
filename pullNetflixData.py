"""import requests

url = "https://unogs-unogs-v1.p.rapidapi.com/aaapi.cgi"

id = 60029591
querystring = {"t":"loadvideo","q":"%d" % id}

headers = {
    'x-rapidapi-host': "unogs-unogs-v1.p.rapidapi.com",
    'x-rapidapi-key': "3c14721fddmsh6282e2acc432c95p14d022jsn00a8f4c7f50c"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
responseList = response.text.split('"')

movieTitle = responseList[11]
movieYear = responseList[43]
imdbRating = responseList[65]

print(movieTitle, movieYear, imdbRating)"""

import requests

url = "https://unogs-unogs-v1.p.rapidapi.com/aaapi.cgi"

querystring = {"q":"{query}-!1900,2020-!0,5-!0,10-!0-!Movie-!Any-!Any-!gt0-!{downloadable}","t":"ns","cl":"all","st":"adv","ob":"Relevance","p":"1","sa":"and"}

headers = {
    'x-rapidapi-host': "unogs-unogs-v1.p.rapidapi.com",
    'x-rapidapi-key': "3c14721fddmsh6282e2acc432c95p14d022jsn00a8f4c7f50c"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text['title'])