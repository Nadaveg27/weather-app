pipeline {
    agent any
    stages {
        // no fetch stage: "Pipeline script from SCM" checks out the repo automatically
        stage('Pylint') {
            steps {
                echo 'running Pylint on the code'
            }
        }
        stage('build') {
            steps {
                sh 'docker build -t nadaveg27/weather-app:$BUILD_NUMBER .'
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