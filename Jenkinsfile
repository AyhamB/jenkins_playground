pipeline {
    options {
        disableConcurrentBuilds()
    }
  
  agent { 
    dockerfile {
        filename 'DockerJenkinsFile'
        args '-u root:sudo'
    } 
  }
  
  stages {
    stage("Testing python") {
      steps {
        sh 'which python'
        sh 'python --version'
      }
    }
    stage("Set Up ssh key") {
       steps {
         sh 'echo $GITHUB_KEY'
         sh 'mkdir $HOME/.ssh'
         sh 'cat $GITHUB_KEY >> $HOME/.ssh/id_rsa'
         sh 'chmod 600 $HOME/.ssh/id_rsa'
         sh 'ssh-keyscan github.com >> $HOME/.ssh/known_hosts'
       }
    }
    
    
    stage("Run main program") {
        steps {          
            sh 'python main.py'
        }
    }
    
    
  }
  
 post {
      always {
          cleanWs()
      }
  }
}
