pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "Compiling code..."
                echo "Code compiled successfully"
            }
        }

        stage('Test') {
            steps {
                echo "Testing..."
                echo "Tests ran successfully"
            }
        }

        stage('Deploy') {
            steps {
                echo "This is now being deployed"
            }
        }
    }

    post {

        // Email Ext plugin:
        success {

        }

        failure {

        }
    }
}