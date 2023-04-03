pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                bat 'pip install -r requirements.txt'
                bat 'pip install uvicorn'
                bat 'start cmd /c "timeout /t 40 && python -m uvicorn app:app --reload"'
            }
        }
        stage('Stop Uvicorn') {
            when {
                buildingTag()
            }
            steps {
                bat 'pkill uvicorn'
            }
        }
    }
}
