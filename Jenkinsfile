pipeline {
agent any
environment {
   VERSION = "${env.BUILD_ID}-${env.GIT_COMMIT}"
   registryCredential = 'dockerhub_id'
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
//         stage("Build docker image"){
//             steps{
//                 bat 'docker build -t flaskapi .'
//                 bat 'docker tag flaskapi darkerlighter/flaskapi:${VERSION}'
//             }
//         }
        stage("Push docker image"){
            steps{
                script {
                    dockerImage = docker.build "darkerlighter/flaskapi" + ":$BUILD_NUMBER"
                    docker.withRegistry( 'https://registry.hub.docker.com', registryCredential ) {
                        dockerImage.push()
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
            }
        }
    }
}