
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
                 script{
                       app = docker.build("httpd")
                       app.inside{
                         sh 'echo "I am inside docker!"'
                                                  }
                      docker.withRegistry('http://nexus:8081/repository/httpd/' , 'nexus'){
                      app.push("latest")
                     }
                      
                 }
                
                // sh 'tar -czvf ${name}.tgz /var/lib/jenkins/workspace/httpd'
            }
        }
         stage('upload to nexus registry') {
            steps {
              echo 'uploading to nexus registry...'
              //sh 'curl -v -u admin:admin123 --upload-file /var/lib/jenkins/workspace/httpd/httpd.tgz http://nexus:8081/repository/git-products/'                   
                
            }
        }
       stage('run'){
                 steps {
                     sh 'python --version'
                     //sh 'docker run hello-world'
                     //sh 'docker build -t httpd .'
                     //sh 'docker run -d -p 7000:7000 httpd'
                   
                 }
             }
         }
     }
