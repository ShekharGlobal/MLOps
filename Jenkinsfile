pipeline {
agent any

stages {

    stage('Python Version') {
        steps {
            bat 'python --version'
        }
    }

    stage('Train Model') {
        steps {
            bat 'python model_training.py'
        }
    }
}

}
