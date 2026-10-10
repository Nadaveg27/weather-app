pipeline {
    agent any
    stages {
        // no fetch stage: "Pipeline script from SCM" checks out the repo automatically
        stage('Pylint') {
            steps {
                sh '''
                    threshold=5
                    out=$(docker run --rm -v jenkins_home:/var/jenkins_home -w "$WORKSPACE" python:3.12-slim sh -c 'pip install -q -r requirements.txt pylint && pylint app.py') || true
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
                sh '''
                    docker network create test-net-$BUILD_NUMBER
                    docker run -d --name test-app-$BUILD_NUMBER --network test-net-$BUILD_NUMBER nadaveg27/weather-app:$BUILD_NUMBER
                    docker run --rm --network test-net-$BUILD_NUMBER curlimages/curl -sf --retry 10 --retry-connrefused --retry-delay 2 http://test-app-$BUILD_NUMBER:5000/health
                '''
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
                 sh '''
                    docker rm -f weather-app || true
                    docker run -d --name weather-app -p 8090:5000 nadaveg27/weather-app:$BUILD_NUMBER                    docker run --rm --network host curlimages/curl -sf --retry 10 --retry-connrefused --retry-delay 2 http://localhost:8090/health
                '''
            }
        }
    }
    post {
        always {
            sh 'docker rm -f test-app-$BUILD_NUMBER || true'
            sh 'docker network rm test-net-$BUILD_NUMBER || true'
        }
        success {
            echo 'pipeline succeeded'
        }
        failure {
            echo 'pipeline failed'
        }
    }
}