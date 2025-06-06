pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git 'https://github.com/vijaysayyaparaju/facebook-login-test.git'
            }
        }

        stage('Check Python and pip') {
            steps {
                bat 'python --version || echo Python not found'
                bat 'pip --version || echo pip not found'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Test') {
            steps {
                bat 'python facebook_login_test.py'
            }
        }
    }
}
