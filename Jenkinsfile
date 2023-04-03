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
	        bat 'pip install -r requirements.txt'
	        }
	   }
		    
	   
	   
    }
}
