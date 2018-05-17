
pipeline {
environment {
     name = 'httpd'
     app = docker.build("httpd")
     }

    agent any
    stages {
        stage('build') {
            steps {
                 echo 'building...'
                 checkout scm
                 app.inside{
                      sh 'echo "I am inside docker!"'
                 }
                // sh 'tar -czvf ${name}.tgz /var/lib/jenkins/workspace/httpd'
            }
        }
         stage('upload to nexus registry') {
            steps {
              echo 'uploading to nexus registry...'
              //sh 'curl -v -u admin:admin123 --upload-file /var/lib/jenkins/workspace/httpd/httpd.tgz http://nexus:8081/repository/git-products/'                   
                 //docker.withRegistry('http://nexus:8081/repository/git-products/' , 'admin:admin123'){
                      //app.push(0.0.1)
                      //app.push("latest")
                 //}
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
