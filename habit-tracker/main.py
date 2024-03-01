import requests

user_info = {"token": "asuqksudajj1982jjj2auaj1717jaj",
             "username": "suneth",
             "agreeTermsOfService": "yes",
             "notMinor": "yes"
             }

response = requests.post(url="https://pixe.la/v1/users", json=user_info)
print(response.text)
