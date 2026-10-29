
pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Check Python') {
            steps {
                bat'"C:\Users\DELL\AppData\Local\Programs\Python\Python312\python.exe" --version'
            }
        }

        stage('Install Requirements') {
            steps {
                bat '"C:\Users\DELL\AppData\Local\Programs\Python\Python312\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Pytest') {
            steps {
                bat '"C:\Users\DELL\AppData\Local\Programs\Python\Python312\python.exe" -m pytest'
            }
        }

        stage('Run Hello App') {
            steps {
                bat '"C:\Users\DELL\AppData\Local\Programs\Python\Python312\python.exe" hello.py'
            }
        }

        stage('Evidently Monitoring') {
            steps {
                bat '"C:\Users\DELL\AppData\Local\Programs\Python\Python312\python.exe" monitor.py'
            }
        }

        stage('Verify Report') {
            steps {
                bat 'if exist evidently_report.html (echo Report generated) else (echo Report missing & exit /b 1)'
            }
        }
    }

    post {
        success {
            echo 'POE pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed. Check Console Output.'
        }
    }
}


