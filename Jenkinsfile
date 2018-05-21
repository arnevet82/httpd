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
          
          stage("Push to registry"){
            steps{
                  sh 'docker push ${registry}:${registryport}/${name} '
               }
          }
          
          stage("Run"){
                steps{
                   sh 'ssh root@dev docker pull ${registry}:${registryport}/${name} '
                   sh 'ssh root@dev docker rm -f ${name} || true'
                   sh 'ssh root@dev docker run --name ${name} -d -p 7000:7000 ${registry}:${registryport}/${name} '
                }
             }




          
          
          
          
     }
}
