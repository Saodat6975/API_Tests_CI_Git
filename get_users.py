# Most active Authors

# API URL: https://jsonmock.hackerrank.com/api/article_users?page=<page_number>
# threshold: integer that represents the threshold value for the number of submission count 
# The function should return an arrray of strings(list of strings) that represent the usernames of users whose submission count is greater 
# than the given threshold. The usernames in the array must be ordered in the order they appear in the API response 

import requests



BASE_URL = 'https://jsonmock.hackerrank.com/api'

def select_users(max_submission):
    current_page = 1
    total_page = 1
    user_list = []

    while current_page <= total_page:
       url = f'{BASE_URL}/article_users'
       params = {'page': current_page}
       response = requests.get(url, params=params)
       dt = response.json()

       for user in dt['data']:
           print(f"Current page: {current_page} - username: {user['username']} - submission_count: {user['submission_count']}")
           if user['submission_count'] > max_submission:
               user_list.append(user['username'])
       total_page = dt['total_pages']
       current_page = current_page + 1

    print(user_list)
    return user_list

select_users(1000)