pipeline {
    agent any
    stages {
        stage('fetch') {
            steps {
                echo 'fetcing the code from GitHub'
                sh 'ls'
            }
        }
        stage('Pylint') {
            steps {
                echo 'running Pylint on the code'
            }
        }
        stage('build') {
            steps {
                echo 'building a Docker image out of the code'
            }
        }
        stage('test') {
            steps {
                echo 'starting the docker image and testing if the app is reachable'
            }
        }
        stage('push') {
            steps {
                echo 'pushing Docker image to Docker Hub'
            }
        }
        stage('deploy') {
            steps {
                echo 'deploying the weather-app container on the host\'s Docker'
            }
        }
    }
    post {
        success {
            echo 'pipeline succeeded'
        }
        failure {
            echo 'pipeline failed'
        }
    }
}