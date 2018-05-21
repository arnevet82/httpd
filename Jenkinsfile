pipeline{
     environment {
          name = 'httpd'
          registry='nexus-dev.securegion.com'
          registryport='18079'
          registryurl=''
           }
     agent any
     
     stages{
          
          stage('Clone') {
               steps{
                    echo 'getting code...'
                    checkout scm
               }
          }
          
          stage("Packaging"){
            steps{
                echo 'preparing docker'
                sh 'docker build -t ${name} .'
                sh 'docker tag ${name} ${registry}:${registryport}/${name}'
               }
          }


          
          
          
          
     }
}
