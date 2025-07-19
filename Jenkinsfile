pipeline {
    agent any

    environment {
        NEW_VERSION = '1.3.0'
        SERVER_CREDENTIALS = credentials('test_credentials')
    }

    parameters {
        booleanParam(name: 'Test', defaultValue: true, description: 'Recursive: True/False')
    }

    stages {
        stage('Build') {
            steps {
                echo 'Hello World'
                //echo "building version ${BUILD_NUMBER}"
            }
        }
        stage('CheckOut') {
            steps {
                git branch: 'test/pipeline_ci_ct',
                        url: 'https://github.com/rajarshi21/Web.git'
            }
        }

        stage('Test') {
            when {
                expression
                        {
                            params.Test
                        }
            }
            steps {
                script {
                    dir("${env.WORKSPACE}\\Python\\Python_Pr") {
                        //sh "pwd"

                        def result = bat(script: 'python Hello.py', returnStatus: true)
                        env.RESULT = result.toString()
//                     echo ${result}
                    }
                }

//                 sh ‘python3 Python\\Python_Pr\\Hello.py‘
                //sh 'python script.py'
                echo 'Hello World'
            }

        }
        stage('Deploy') {

            when {
                expression
                        {
                            return env.RESULT == "True"
                        }
            }
            // Call a Jenkins Job
            steps {
                script {
                    build job: 'TEST_REPO', wait: true
                }
            }
        }
    }
    post {
        always {
            //
            echo "In always"
        }
        success {
            echo "In success"
        }
        failure {
            echo "In failure"
        }
    }
}
