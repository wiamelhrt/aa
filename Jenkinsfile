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
                bat 'start cmd /c "python -m uvicorn app:app --reload & echo %PROCESS_ID% > pid.txt"'
            }
        }
        stage('Stop Uvicorn') {
            when {
                buildingTag()
            }
            steps {
                bat 'set /p pid=<pid.txt && timeout /t 60 && taskkill /f /pid %pid%'
            }
        }
    }
}
