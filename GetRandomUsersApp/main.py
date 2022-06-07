import tkinter as tk
import tkinter.messagebox as messagebox
from network import get_response
from user_transformer import parse_user

def on_show_click(display_text):
	messagebox.showinfo( "JSON content", display_text)

root = tk.Tk()
root.geometry("500x500")

user_response = get_response("https://randomuser.me/api/?results=2")
user_obj = parse_user(user_response.content)

for user in user_obj.results:
	first_name_label = tk.Label(root, text="First name: " + user.name.first)
	first_name_label.pack()
	last_name_label = tk.Label(root, text="Last name: " + user.name.last)
	last_name_label.pack()
	country_field_label = tk.Label(root, text="Country: " + user.location.country)
	country_field_label.pack()

show_button = tk.Button(root, text="Show json", command=lambda display_text=user_response.content: on_show_click(display_text))
show_button.pack()

root.mainloop()
