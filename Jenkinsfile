pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Kaviya-0006/multi_module_app.git'
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

        stage('Deploy to Kubernetes') {
    steps {
        bat "kubectl --kubeconfig=C:\\jenkins_k8s\\config config view"
    }
}
    }

    post {
        success {
            echo 'CI/CD Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check logs.'
        }
    }
}