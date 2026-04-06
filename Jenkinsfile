pipeline {
    agent any

    environment {
        COMPOSE_FILE = 'docker-compose.jenkins.yml'
        PROJECT_NAME = 'rentease_jenkins'
    }

    stages {

        stage('Clone Repository') {
            steps {
                echo 'Cloning RentEase repository from GitHub...'
                git branch: 'main',
                    url: 'https://github.com/codewithniha/rentease.git'
                echo 'Code cloned successfully!'
            }
        }

        stage('Verify Code') {
            steps {
                echo 'Verifying project structure...'
                sh 'ls -la'
                sh 'ls -la backend/'
                sh 'ls -la frontend/'
                echo 'Project structure verified!'
            }
        }

        stage('Build - Stop Old Containers') {
            steps {
                echo 'Stopping any previously running containers...'
                sh 'docker compose -f ${COMPOSE_FILE} -p ${PROJECT_NAME} down --remove-orphans || true'
                echo 'Old containers stopped.'
            }
        }

        stage('Build - Launch Containers') {
            steps {
                echo 'Building and launching containerized application...'
                sh 'docker compose -f ${COMPOSE_FILE} -p ${PROJECT_NAME} up -d --build'
                echo 'Containers launched!'
            }
        }

        stage('Verify Build') {
            steps {
                echo 'Verifying all containers are running...'
                sh 'docker compose -f ${COMPOSE_FILE} -p ${PROJECT_NAME} ps'
                sh 'sleep 15'
                sh 'docker ps | grep jenkins_rentease'
                echo 'Build verification complete!'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully! RentEase is running.'
            echo 'App available at: http://15.206.158.180:8080'
        }
        failure {
            echo 'Pipeline failed. Collecting logs...'
            sh 'docker compose -f ${COMPOSE_FILE} -p ${PROJECT_NAME} logs --tail=50 || true'
        }
    }
}