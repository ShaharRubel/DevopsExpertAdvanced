# Tech Stack
![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) ![image](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white) ![image](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) ![image](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white) ![image](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=Jenkins&logoColor=white)
# About the project
The project is a user management API + small frontend  with a mysql database including a jenkins ready pipeline


project content as follow:
- `rest_app.py`: RESTful application and API endpoints definitions
- `web_app.py`: a simple web application to display users
- `db_connector.py`: Database Connection functionality
- `backend_testing.py`: rest_app.py testing
- `frontend_testing.py`: web_app.py testing
- `combined_testing.py`: rest_app.py and web_app.py testing combined
- `clean_environment.py`: a script to stop both webservers in CI
- `Jenkinsfile`: Jenkin file for CI
- `DevopsExpert.postman_collection.json`: Postman premade requests




# Steps to run it yourself

1. Download required files
```
git clone https://github.com/ShaharRubel/DevopsExpertAdvanced.git
pip install pymysql flask requests selenium
```
2. Update remote db credentials - See Updating the remote DB
3. run backend
```commandline
python rest_app.py
```
4. run frontend
```commandline
python web_app.py
```

# Updating the remote db
1. create a free remote mysql service - i used aiven
https://aiven.io/free-mysql-database
2. update the db_connector.py file
```commandline
db="DevopsExperts", \\ update db
host="mysql-23b9542e-devopsexperts.c.aivencloud.com", \\ update host
password="AVNS_WEPQrf0gLBZxdjuphDx", \\ update password
```
3. run the create_table() function in db_connector.py

# Using the Postman premade collection
1. locate DevopsExpert.postman_collection.json
2. import collection in Postman


for safe keeping

curl --user admin:admin -X POST -F "jenkinsfile=<Jenkinsfile" http://localhost:8080/pipeline-model-converter/validate