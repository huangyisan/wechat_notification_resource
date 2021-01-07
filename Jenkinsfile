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
      steps {
          sh "docker build . -t test:${lastTag}"
      }
    }
  }
}
