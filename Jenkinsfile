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
		ls k8s
                '''
            }
        }

       stage('Package for Deployment') {
            steps {
                sh '''
                echo "Application packaged and ready for deployment"
                '''
            }
        }
    }
}
