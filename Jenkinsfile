pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/anushkagaur2904/LogiSafe-DevSecOps.git'
            }
        }

        stage('Install Dependencies & Test') {
            agent {
                docker {
                    image 'python:3.10-slim'
                }
            }
            steps {
                sh '''
                python --version
                cd app
                pip install -r requirements.txt
                python -c "import app"
                '''
            }
        }
    }
}
