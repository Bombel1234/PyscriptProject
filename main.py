from pyscript import display
from pyscript import document
import requests
import os
import json


my_element = document.querySelector(".messenge")
my_input = document.querySelector(".my_input")

connect = document.querySelector(".connect")

display('Python is running!')
# from pyscript.media import Device, list_devices

# devices = await list_devices()
# my_device = devices[0]

n = 0


def handler_defined_in_python(event):  
    global n
    if my_input.value:
        a = int(my_input.value) 
        if 100 < a < 200:
            my_element.innerText = "Przedlozka cieta 320mm"
        elif 200 < a < 300:
            my_element.innerText = "Przedlozka  cala"
        elif 300 < a < 400:
            my_element.innerText = "Przedlozka cieta 320mm"
        elif 400 < a < 500:
            my_element.innerText = "Przedlozka  cala"
        else:
            my_element.innerText = "Niema takich wymiarow"
            
def connect_requests(events):
    if my_input.value != "":
        try:
            response = requests.get(my_input.value)
            if response.status_code == 200:
                connect.innerText = "Connected to GitHub API"
            else:
                connect.innerText = "Failed to connect to GitHub API"
        except requests.exceptions.RequestException as e:
            connect.innerText = f"Error connecting to GitHub API: {e}"
    else:
        # alert("Please enter a valid URL")
        pass
        
def create_database(event):
    path =  f"{os.getcwd()}"
    connect.innerText = os.listdir(path)
    
def read_file(event):
    with open("main.json", 'r') as file:
        content = json.load(file)
        connect.innerText = content['name']
    # try:
    #     with open("subdir/main.json", 'r') as file:
    #         content = json.load(file)
    #         connect.innerText = content['name']
    # except FileNotFoundError:
    #     connect.innerText = "Database file not found."
    # except Exception as e:
    #     connect.innerText = f"An error occurred: {e}"
        
def update_file(event):
    messenge = my_input.value
    try:
        with open("subdir/main.json", 'r') as file:
            content = json.load(file)
        content['name'] = messenge
        json_str = json.dumps(content, indent=4)
        with open("subdir/main.json", 'w') as file:
            file.write(json_str)
        connect.innerText = "File updated successfully."
    except FileNotFoundError:
        connect.innerText = "Database file not found."
    except Exception as e:
        connect.innerText = f"An error occurred: {e}"
    
    
