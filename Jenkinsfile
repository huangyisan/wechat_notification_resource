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

                if ("$webStatus" == 200) {
                  echo "Concourse is not up"
                  error "Concourse is not up"
                }
              }

              stage('Render smoke test YAML file') {
                  dir('smoke-test') {
                    // def wxToken = credentials('wx-token-self')
                    withCredentials([string(credentialsId: 'wx-token-self', variable: 'wxToken')]) {
                         sh "python3 wx-alert-smoke-test-pipeline-render.py ${wxToken} ${lastTag}"
                    // sh "ls"
                  }
                }
              }

              stage('Update wx-alert-smoke-test-pipeline'){
                dir('smoke-test') {
                  sh "fly -t main login -c http://localhost:8080 -u test -p test"
                  sh "fly -t main sp -p wx-alert-smoke-test -c wx-alert-smoke-test-pipeline.yml -n"
                  sh "fly -t main unpause-pipeline -p wx-alert-smoke-test"
                  sh "fly -t main trigger-job -j wx-alert-smoke-test/smoke-test"
                }
              }
            }
            // img.push();
          }
        }
      }
    }
  }
}
