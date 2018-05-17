//so jenkins now will go to git, get code, tar and upload , then get it it again from repo, make docker?
pipeline{
     
     environment {
          name = 'httpd'
           }
     agent any
     
     stages {
          
          stage('get code from git') {
               
               steps{
                    echo 'getting code...'
                    checkout scm
               }
          }
          
          stage('tar and upload to nexus') {
               
               steps{
                    echo 'condensing to tar...'
                    sh 'tar -czvf ${name}.tgz /var/lib/jenkins/workspace/httpd'
                    echo 'uploading to nexus...'
                    sh 'curl -v -u admin:admin123 --upload-file /var/lib/jenkins/workspace/httpd/httpd.tgz http://nexus:8081/repository/httpd/' 
               }
          }
          
          stage('get tar from nexus and extract') {
               
               steps{
                    echo 'retrieving file from nexus...'
                    sh 'curl -X GET -u admin:admin123 http://nexus:8081/repository/git-products/ -O'
               }
          }
          
          stage('build and run docker') {
               
               steps{
                    echo 'building docker...'
               }
          }
     }
}
