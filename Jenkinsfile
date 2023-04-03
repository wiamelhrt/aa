pipeline {
	agent any
	    stages {
	        stage('Clone Repository') {
	        /* Cloning the repository to our workspace */
	        steps {
	        checkout scm
	        }
	   }
	   stage('Build') {
	        steps {
	        withPythonEnv('venv') {
                    bat 'python -m uvicorn app:app --reload'
                }
	        }
	   }
	   
	   
    }
}
