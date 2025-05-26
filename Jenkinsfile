pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/akv3319/hello-world-jenkins.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
            }
        }
        stage('Run App') {
            steps {
                echo 'Running app...'
            }
        }
    }
}
