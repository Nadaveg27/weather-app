pipeline {
    agent any
    stages {
        // no fetch stage: "Pipeline script from SCM" checks out the repo automatically
        stage('Pylint') {
            steps {
                sh '''
                    threshold=5
                    out=$(docker run --rm -v jenkins_home:/var/jenkins_home -w "$WORKSPACE" python:3.12-slim sh -c 'pip install -q -r requirements.txt pylint && pylint app.py')
                    echo "$out"
                    score=$(echo "$out" | grep -o 'rated at [-0-9.]*' | awk '{print $NF}')
                    awk -v s="$score" -v t="$threshold" 'BEGIN { exit !(s > t) }' || { echo "Pylint score $score is not above $threshold"; exit 1; }
                    '''
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
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DH_USER', passwordVariable: 'DH_TOKEN')]) {
                    sh '''
                        echo "$DH_TOKEN" | docker login -u "$DH_USER" --password-stdin
                        docker push nadaveg27/weather-app:$BUILD_NUMBER
                    '''
                }
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