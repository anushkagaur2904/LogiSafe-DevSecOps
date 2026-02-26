pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                url: 'https://github.com/anushkagaur2904/LogiSafe-DevSecOps.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                cd app
                pip install -r requirements.txt
                '''
            }
        }

        stage('Basic App Test') {
            steps {
                sh '''
                cd app
                python -c "import app"
                '''
            }
        }
    }
}
