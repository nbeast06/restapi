import requests

#from the movie db org website
api_key = "0d7fd9abe094d6278738697e5caf0349"

# sample API https://api.themoviedb.org/3/movie/550?api_key=0d7fd9abe094d6278738697e5caf0349
movie_id = 500
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"

r= requests.get(endpoint)# json={"api_key":api_key})

print(r.status_code)
print(r.text)