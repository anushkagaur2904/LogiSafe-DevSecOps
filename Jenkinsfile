pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/anushkagaur2904/LogiSafe-DevSecOps.git'
            }
        }

        stage('Verify Project Structure') {
            steps {
                sh '''
                ls
                ls app
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                echo "Building Docker image for LogiSafe"
                sh jenkins/docker-build.sh
                '''
            }
        }
    }
}
