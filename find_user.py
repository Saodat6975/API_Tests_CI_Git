import requests



BASE_URL = 'https://reqres.in/api'

def find_full_name(email):
    current_page = 1
    total_page = 1

    while current_page <= total_page:
       url = f'{BASE_URL}/users'
       params = {'page': current_page}
       response = requests.get(url, params=params)
       dt = response.json()

       for user in dt['data']:
        # print(f"Current page: {current_page} - username: {user['username']} - submission_count: {user['submission_count']}")
           if user['email'] == email:
            return f"{user['first_name']} {user['last_name']}"
       total_page = dt['total']
       current_page = current_page + 1



print(find_full_name('charles.morris@reqres.in'))