import requests
# url ="https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
# r = requests.get(url)
# #print(r.text)
# data = r.json()
# print(data['current_units']['time'])

url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTStSMv9J0DOeTMmQ2OzbYYQnHhm84zsXSlZQ&usqp=CAU"
r = requests.get(url)
with open('encrypted_image.jpg', 'wb') as mf:
    mf.write(r.content)
