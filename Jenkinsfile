pipeline {
    agent any

    environment{
        NEW_VERSION = '1.3.0'
        SERVER_CREDENTIALS = credentials('fc8de0bc-32f9-416b-96d4-82ca19dfdecb')
    }

    parameters{
        booleanParam(name: 'Recursive', defaultValue: true, description: 'Recursive: True/False')
    }

    stages {
        stage('Build') {
            steps {
                echo 'Hello World'
                echo "building version ${BUILD_NUMBER}"
            }
        }

        stage('Test') {
            when{                
                    expression
                    {
                        params.Recursive
                    }                
            }
            steps {
                echo 'Hello World'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Hello World' 
            }
        }
    }
    post{
        always{
            //
            echo "In always"
        }
        success{
             echo "In success"
        }
        failure{
            echo "In failure"
        }
    }
}
