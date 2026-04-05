pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/Kaviya-0006/multi_module_app.git'
            }
        }

        stage('Build Module1 Docker Image') {
            steps {
                bat 'docker build -t module1-image -f Dockerfile.module1 .'
            }
        }

        stage('Build Module2 Docker Image') {
            steps {
                bat 'docker build -t module2-image -f Dockerfile.module2 .'
            }
        }

        stage('Run Containers') {
            steps {
                bat 'docker run -d -p 5000:5000 module1-image'
                bat 'docker run -d -p 6001:6001 module2-image'
            }
        }
    }
}