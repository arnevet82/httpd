
pipeline {
environment {
     name = 'httpd'
     }

    agent any
    stages {
        stage('build') {
            steps {
                 echo 'building...'
                 checkout scm
            }
        }
         stage('upload to nexus registry') {
            steps {
              echo 'uploading to nexus registry...'
               //  sh 'curl -v -u admin:admin123 --upload-file hello.py http://nexus:8081/repository/git-products/'                 
            }
        }
       stage('run'){
                 steps {
                     sh 'python --version'
                   sh 'docker run hello-world'
                   sh 'sudo docker build -t httpd .'
                   
                 }
             }
         }
     }
