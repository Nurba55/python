import datetime, json



current_datetime = datetime.datetime.now().strftime("%d/%m/%d %H:%M:%S")



data = [
	{"id": 1, "username":"admin", "email":"admin@ample.com", "registered_at":current_datetime},
	{"id": 2, "username":"first_user", "email":"admin@ample.com", "registered_at":current_datetime},
	{"id": 3, "username":"second_user", "email":"admin@ample.com", "registered_at":current_datetime}
]

with open("data.json", "w") as file:
	json.dump(data,file)
	file.close()

with open("data.json", "r") as file:
	loaded_data = json.load(file)
	print(loaded_data)
	file.close()
