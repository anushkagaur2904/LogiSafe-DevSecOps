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
                echo "Checking project structure"
                ls
                ls app
                '''
            }
        }

        stage('Basic Validation') {
            steps {
                sh '''
                echo "CI pipeline executed successfully"
                '''
            }
        }
    }
}
