pipeline {
agent any
environment {
   VERSION = "${env.BUILD_ID}-${env.GIT_COMMIT}"
   registryCredential = 'dockerhub_id'
   imagename = "darkerlighter/flaskapi"
    }
    stages {
        stage("Clone Repo") {
            steps {
                git([url: 'git@github.com:ShaharRubel/DevopsExpertAdvanced.git', branch: 'docker', credentialsId: 'github_repo'])
            }
        }
        stage("Run Backend Server"){
            steps {
                bat 'start /min python rest_app.py'
            }
        }
        stage("Run Backend testing"){
            steps {
                bat 'python backend_testing.py'
            }
        }
        stage("Clean Environment"){
            steps {
                bat 'python clean_environment.py'
            }
        }
        stage("Build docker image"){
            steps{
//                 script {
//                     dockerImage = docker.build "${imagename}:latest"
//                 }
                bat "docker build -t flaskapi ."
                bat "docker tag flaskapi ${imagename}:${BUILD_NUMBER}"
            }
        }
        stage("Push docker image"){
            steps{
                script {
                    withCredentials([usernamePassword(credentialsId: registryCredential, usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        bat "docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD"

                        // Push the image
                        bat "docker push ${imagename}:${BUILD_NUMBER}"
                    }
                }
            }
        }
        stage("Set Image version"){
            steps{
                bat 'echo IMAGE_TAG=${BUILD_NUMBER} > .env'
            }
        }
        stage("Deploy application with docker compose"){
            steps{
                bat 'docker-compose up -d'
            }
        }
        stage("Run docker backend testing"){
            steps{
                bat 'python docker_backend_testing.py'
            }
        }
        stage("Clean Environment docker"){
            steps{
                bat 'clean.bat'
                bat "docker image rmi darkerlighter/flaskapi:${BUILD_NUMBER}"
            }
        }
    }
}