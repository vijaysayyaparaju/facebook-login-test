pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/vijaysayyaparaju/facebook-login-test.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Test') {
            steps {
                bat 'python tests/test_facebook_login.py'
            }
        }
    }
}
