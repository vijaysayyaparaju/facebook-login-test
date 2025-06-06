pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git 'https://github.com/vijaysayyaparaju/facebook-login-test.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Test') {
            steps {
                sh 'python tests/test_facebook_login.py'
            }
        }
    }
}
