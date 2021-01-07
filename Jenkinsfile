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
          echo "${lastTag}"
        }
      }
    }
    stage('Build docker image') {
      when {
          branch "${branch}"
      }
      steps {
          echo "this is build stage ${lastTag}"
      }
    }
  }
}
