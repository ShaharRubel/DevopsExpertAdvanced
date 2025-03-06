import requests
import json
from db_connector import connect_db
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


url = "http://127.0.0.1:5000/users/3"

# Step 1
try:
    data = {"user_name": "David"}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
except:
    raise Exception("Test Failed")
# Step 2
try:
    data = requests.get(url)
    data = data.json()
    print(data['user_name'])

    if data['user_name'] == "David":
        print("test is successful")
    else:
        raise Exception("Test Failed")
except:
    print("operation failed")

# Step 3

# connect to DB
connection = connect_db()
cursor = connection.cursor()
cursor.execute("SELECT * FROM DevopsExperts.users WHERE user_id = 3;")
name = cursor.fetchall()[0]['user_name']

if name == "David":
    print("test is successful")
else:
    raise Exception("Test Failed")
connection.close()

# Step 4-6
driver = webdriver.Chrome()

driver.get("http://127.0.0.1:5001/users/get_user_data/3")

try:
    driver.find_element("id", "user")
    name = driver.find_element("id", "user").text
    print(name)
    if name == "David":
        print("Test is successful")
    else:
        raise Exception("Test Failed")

except:
    print("Element not found")