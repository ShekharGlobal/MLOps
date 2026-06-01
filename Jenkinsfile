pipeline {
agent any

```
environment {
    IMAGE_NAME = "110044/mlops-churn-api"
    IMAGE_TAG  = "latest"
}

stages {

    stage('Checkout Code') {
        steps {
            checkout scm
        }
    }

    stage('Verify Python') {
        steps {
            bat 'python --version'
        }
    }

    stage('Install Dependencies') {
        steps {
            bat 'pip install -r requirements.txt'
        }
    }

    stage('Train Model') {
        steps {
            bat 'python model_training.py'
        }
    }

    stage('Verify Model') {
        steps {
            bat 'dir'
        }
    }

    stage('Build Docker Image') {
        steps {
            bat 'docker build -t %IMAGE_NAME%:%IMAGE_TAG% .'
        }
    }

    stage('Docker Hub Login') {
        steps {
            withCredentials([
                usernamePassword(
                    credentialsId: 'a9111404-2995-4edb-866a-afc926d58b5d',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )
            ]) {
                bat 'echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin'
            }
        }
    }

    stage('Push Docker Image') {
        steps {
            bat 'docker push %IMAGE_NAME%:%IMAGE_TAG%'
        }
    }
}

post {
    success {
        echo 'CI/CD Pipeline Completed Successfully'
    }

    failure {
        echo 'CI/CD Pipeline Failed'
    }
}
```

}
