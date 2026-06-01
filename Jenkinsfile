pipeline {
agent any

```
stages {

    stage('Checkout') {
        steps {
            checkout scm
        }
    }

    stage('Python Version') {
        steps {
            bat 'python --version'
        }
    }

    stage('Install Requirements') {
        steps {
            bat 'pip install -r requirements.txt'
        }
    }

    stage('Train Model') {
        steps {
            bat 'python model_training.py'
        }
    }
}
```

}
