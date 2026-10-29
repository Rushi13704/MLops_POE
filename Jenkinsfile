
pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Check Python') {
            steps {
                bat 'python --version'
            }
        }

        stage('Install Requirements') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Pytest') {
            steps {
                bat 'python -m pytest'
            }
        }

        stage('Run Hello App') {
            steps {
                bat 'python hello.py'
            }
        }

        stage('Evidently Monitoring') {
            steps {
                bat 'python monitor.py'
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
