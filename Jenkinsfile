pipeline {
  agent any
  stages {
    stage('Get Last Tag') {
      steps {
        when {
          branch "feature-auto-ci"
        }
        dir('wechat_notification_resource') {
          script {
            lastTag = """${sh(
            returnStdout: true, script: 'git describe --tags `git rev-list --tags --max-count=1`'
            )}"""
            lastTag =  lastTag.trim()
            echo "${lastTag}"
            echo "ls"
          }
        }
      }
    }
    stage('Build docker image') {
      steps {
        when {
          branch "feature-auto-ci"
        }
        dir('wechat_notification_resource') {
          echo "this is build stage ${lastTag}"
        }
      }
    }
  }
}
