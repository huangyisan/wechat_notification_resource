pipeline {
  agent any
  environment {
    branch="feature-auto-ci"
  }
  stages {
    stage('Get Last Tag') {
        when {
          branch "${branch}"
        }
      steps {
        script {
          lastTag = """${sh(
          returnStdout: true, script: 'git describe --tags `git rev-list --tags --max-count=1`'
          )}"""
          lastTag = lastTag.trim()
        }
      }
    }
    stage('Build docker image') {
      when {
          branch "${branch}"
      }
      // run follow commands on linux
      // refer: https://docs.docker.com/engine/install/linux-postinstall/
      // groupadd docker
      // usermod -aG docker jenkins
      // systemctl restart jenkins
      steps {
        script {
          // 
          docker.withRegistry("https://index.docker.io/v1/","docker-registry") {
            def img = docker.build("dockerhuangyisan/wechat-notification-resource:${lastTag}-autoci",'.')
            stage('Test image') {

              stage('Ensure concourse is up') {
                webStatus = """${sh(
                returnStdout: true, script: 'curl -s -o /dev/null -w "%{http_code}" http://localhost:8080/'
                )}"""

                if ("$webStatus" != 200) {
                  echo "Concourse is not up"
                  error "Concourse is not up"
                }
              }

              stage('Render smoke test YAML file') {
                environment {
                  wxToken = credentials('wx-token-self')
                }
                steps {
                  dir('smoke-test') {
                    sh "python3 wx-alert-smoke-test-pipeline-render.py ${wxToken} ${lastTag}"
                    sh "ls"
                  }
                  
                }
              }
              
              echo "$wxToken"
            }
            // img.push();
          }
            sh 'docker images'
            // sh "docker build . -t test:${lastTag}"
        }
      }
    }
  }
}
