import tkinter as tk
from network import get_response
from user_transformer import parse_user

root = tk.Tk()
root.geometry("500x500")

user_response = get_response("https://randomuser.me/api/?results=2")
user_obj = parse_user(user_response.content)

for user in user_obj.results:
	first_name_label = tk.Label(root, text="First name: " + user.name.first)
	first_name_label.pack()
	last_name_label = tk.Label(root, text="Last name: " + user.name.last)
	last_name_label.pack()
	country_label = tk.Label(root, text="Country: " + user.location.country)
	country_label.pack()

json_label = tk.Label(root, text=user_response.content, wraplength=500, justify="center")
json_label.pack()

root.mainloop()