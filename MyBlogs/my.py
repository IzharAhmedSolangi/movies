import requests

url = "https://imdb-top-100-movies.p.rapidapi.com/"

headers = {
	"X-RapidAPI-Key": "ccabb15560msh1fc495aa73d39fbp1f9968jsn82a334c703e1",
	"X-RapidAPI-Host": "imdb-top-100-movies.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)