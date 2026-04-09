pipeline {
    agent any

    environment {
        DOCKER_USER_ID = "kaviya6369"
        MODULE1_IMAGE = "${DOCKER_USER_ID}/module1-image:v1"
        MODULE2_IMAGE = "${DOCKER_USER_ID}/module2-image:v2"
        CONNECT_IMAGE = "${DOCKER_USER_ID}/connect-module:v3"
        KUBECONFIG_PATH = "C:\\jenkins_k8s\\config"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Kaviya-0006/multi_module_app.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                echo 'Building Module1 Docker image...'
                bat "docker build -t %MODULE1_IMAGE% -f Dockerfile.module1 ."

                echo 'Building Module2 Docker image...'
                bat "docker build -t %MODULE2_IMAGE% -f Dockerfile.module2 ."

                echo 'Building Connect Module Docker image...'
                bat "docker build -t %CONNECT_IMAGE% -f Dockerfile.connect_module ."
            }
        }

        stage('Push Docker Images to DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds', 
                    usernameVariable: 'USER', 
                    passwordVariable: 'PASS'
                )]) {
                    bat """
                        docker login -u %USER% -p %PASS%
                        docker push %MODULE1_IMAGE%
                        docker push %MODULE2_IMAGE%
                        docker push %CONNECT_IMAGE%
                    """
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying Module1...'
                bat "kubectl --kubeconfig=%KUBECONFIG_PATH% apply -f k8s/module1-deployment.yaml"
                bat "kubectl --kubeconfig=%KUBECONFIG_PATH% apply -f k8s/module1-service.yaml"

                echo 'Deploying Module2...'
                bat "kubectl --kubeconfig=%KUBECONFIG_PATH% apply -f k8s/module2-deployment.yaml"
                bat "kubectl --kubeconfig=%KUBECONFIG_PATH% apply -f k8s/module2-service.yaml"

                echo 'Deploying Connect Module (v3)...'
                bat "kubectl --kubeconfig=%KUBECONFIG_PATH% apply -f k8s/connect_module-deployment.yaml"
                bat "kubectl --kubeconfig=%KUBECONFIG_PATH% apply -f k8s/connect_module-service.yaml"
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline executed successfully! All modules are deployed.'
        }
        failure {
            echo 'Pipeline failed. Check Jenkins Console Output.'
        }
    }
}