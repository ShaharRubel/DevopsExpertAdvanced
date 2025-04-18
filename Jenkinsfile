pipeline {
agent any
    stages {
        stage("Clone Repo") {
            steps {
                git([url: 'git@github.com:ShaharRubel/DevopsExpertAdvanced.git', branch: 'main', credentialsId: 'github_repo'])
            }
        }
        stage("Run Backend Server"){
            steps {
                bat 'start /min python rest_app.py'
            }
        }
        stage("Run Frontend Server "){
            steps {
                bat 'start /min python web_app.py'
            }
        }
        stage("Run Backend Test") {
            steps {
                bat 'python backend_testing.py'
            }
        }
        stage("Run Frontend Test") {
            steps {
                bat 'python frontend_testing.py'
            }
        }
        stage("Run Combined Test") {
            steps {
                bat 'python combined_testing.py'
            }
        }
        stage("Clean Environment") {
            steps {
                bat 'python clean_environment.py'
            }
        }
    }
}