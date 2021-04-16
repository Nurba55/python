import json, time, datetime

 

 #now = datetime.datetime.now()
 #then = datetime.datetime(2021,12,14)
 #delta = now -then
 #print(delta.days) 

data = [
{"ID":1},{"ID":2},{"ID":3}, 
{"username":"admin"},
{"username":"first_user"},
{"username":"second_user"},{"registered_at":"d"}
]



with open("data_file.json", "w") as file:
    json.dump(data, file)
    file.close()

with open("data_file.json", "r") as file:
    data = json.load(file)
    print(data)