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
        dir('wechat_notification_resource') {
          script {
            sh 'ls'
            lastTag = """${sh(
            returnStdout: true, script: 'git describe --tags `git rev-list --tags --max-count=1`'
            )}"""
            lastTag =  lastTag.trim()
            echo "${lastTag}"
            
          }
        }
      }
    }
    stage('Build docker image') {
      when {
          branch "${branch}"
      }
      steps {
        dir('wechat_notification_resource') {
          echo "this is build stage ${lastTag}"
        }
      }
    }
  }
}
