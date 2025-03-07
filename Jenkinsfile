pipeline {
agent any
    stages {
        stage("Clean up") {
            steps {
                deleteDir()
            }
        }
        stage("Clone Repo") {
            steps {
                git([url: 'git@github.com:ShaharRubel/DevopsExpertAdvanced.git', branch: 'main', credentialsId: 'github_repo'])
            }
        }
    }
}