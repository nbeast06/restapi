import requests
import pprint

#from the movie db org website
api_key = "0d7fd9abe094d6278738697e5caf0349"
access_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwZDdmZDlhYmUwOTRkNjI3ODczODY5N2U1Y2FmMDM0OSIsInN1YiI6IjVmZjJmMTJjZmJlMzZmMDAzZmY4NGNiYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.xW5eUqN2mHvOI5YGoPkWY5h1JN7vUKDBPPXibE1AheY"
# sample API https://api.themoviedb.org/3/movie/550?api_key=0d7fd9abe094d6278738697e5caf0349
movie_id = 501
api_version = 4
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
headers={
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json;charset=utf-8'
}
r= requests.get(endpoint, headers=headers)
print(r.status_code)
print(r.text)
