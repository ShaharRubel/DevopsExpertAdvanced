# Tech Stack
![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) ![image](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white) ![image](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) ![image](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=Jenkins&logoColor=white) ![image](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
# About the Branch
This branch focuses on creating a Jenkins pipeline with docker and docker compose


project content as follow:
- `rest_app.py`: RESTful application and API endpoints definitions
- `db_connector.py`: Database Connection functionality
- `backend_testing.py`: rest_app.py testing
- `docker_backend_testing.py`: Testing made for the dockerized application
- `clean_environment.py`: a script to stop both webservers in CI
- `Jenkinsfile`: Jenkin file for CI
- `Dockerfile`: DockerFile to package the application
- `Docker-compose.yaml`: Docker compose file to run the application in CI
- `requirements`: required libraries for the project
- `clean.bat`: simple script to clean up the environment after each run of the CI
- `DevopsExpert.postman_collection.json`: Postman premade requests





# Steps to run it yourself

1. Download required files
```
git clone https://github.com/ShaharRubel/DevopsExpertAdvanced.git
pip install pymysql flask requests selenium
```
2. Update remote db credentials - See Updating the remote DB
3. cd into directory `cd DevopsExpertAdvanced`
3. run backend with compose
```
docker-compose up -d
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