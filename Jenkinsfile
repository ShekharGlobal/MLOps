pipeline {
agent any

```
environment {
    IMAGE_NAME = "110044/mlops-churn-api"
    IMAGE_TAG = "latest"
}

stages {

    stage('Checkout Code') {
        steps {
            checkout scm
        }
    }

    stage('Verify Tools') {
        steps {
            sh 'python --version'
            sh 'git --version'
        }
    }

    stage('Install Dependencies') {
        steps {
            sh 'pip install -r requirements.txt'
        }
    }

    stage('Train Model') {
        steps {
            sh 'python model_training.py'
        }
    }

    stage('Build Docker Image') {
        steps {
            sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
        }
    }

    stage('Docker Login') {
        steps {
            withCredentials([
                usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )
            ]) {
                sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
            }
        }
    }

    stage('Push Docker Image') {
        steps {
            sh 'docker push $IMAGE_NAME:$IMAGE_TAG'
        }
    }
}

post {
    success {
        echo 'Build Successful!'
    }
    failure {
        echo 'Build Failed!'
    }
}
```

}
