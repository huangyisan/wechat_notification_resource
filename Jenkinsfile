pipeline {
  agent any
  environment {
    BRANCH="feature-auto-ci"
  }
  stages {
    stage('Get latest tag') {
      when {
        branch "${BRANCH}"
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
          branch "${BRANCH}"
      }
      // run follow commands on linux
      // refer: https://docs.docker.com/engine/install/linux-postinstall/
      // groupadd docker
      // usermod -aG docker jenkins
      // systemctl restart jenkins
      steps {
        script {
          docker.withRegistry("https://index.docker.io/v1/","docker-registry") {
            def img = docker.build("dockerhuangyisan/wechat-notification-resource:${lastTag}",'.')
            stage('Test image') {

              stage('Ensure concourse is up') {
                script {
                  webStatus = """${sh(
                    returnStdout: true, script: 'curl -s -o /dev/null -w "%{http_code}" http://localhost:8080/'
                  )}"""
                  
                  if ("$webStatus" != "200") {
                    echo "Concourse is not up"
                    error "Concourse is not up"
                  } else {
                    echo "Concourse is up"
                  }
                 }
              }

              stage('Render smoke test YAML file') {
                  dir('smoke-test') {
                    withCredentials([string(credentialsId: 'wx-token-self', variable: 'wxToken')]) {
                      sh "python3 wx-alert-smoke-test-pipeline-render.py ${wxToken} ${lastTag}"
                  }
                }
              }

              stage('Update wx-alert-smoke-test-pipeline'){
                dir('smoke-test') {
                  sh "fly -t main login -c http://localhost:8080 -u test -p test"
                  sh "fly -t main sp -p wx-alert-smoke-test -c wx-alert-smoke-test-pipeline.yml -n"
                  sh "fly -t main unpause-pipeline -p wx-alert-smoke-test"
                  sh "fly -t main trigger-job -j wx-alert-smoke-test/smoke-test"
                  // wait for running smoke test
                  sh "sleep 25"
                }
              }

              stage('Get job latest test status') {
                script {
                  // succeeded
                  isSucceeded = """${sh(
                    returnStdout: true, script: 'fly -t main jobs -p wx-alert-smoke-test  | grep "succeeded" | wc -l'
                  )}"""
                  isSucceeded = isSucceeded.trim()
                  echo "$isSucceeded"
                  if ("$isSucceeded" != "1") {
                    echo "Smoke test Failed"
                    error "Smoke test Failed"
                  } else {
                    echo "Smoke test Successful"
                  }
                }
              }

              stage('Retag to latest') {
                img.push('autoci-latest')
              }
            }
          }
        }
      }
    }
  }
  post {
    always {
      script {
          def COMMIT_ID = ""
          COMMIT_ID = sh(returnStdout: true, script:'git log --pretty=format:"%h" -1')
          
          def mimeType = 'text/html'

          def to = 'anonymousyisan@gmail.com'

          def subject = '【构建通知】$PROJECT_NAME - ' + "${COMMIT_ID}" +  ' - Build # $BUILD_NUMBER - $BUILD_STATUS!'

          def body = 
          '''
<html>
  <head>
    <meta charset="UTF-8">
    <title>${ENV, var="JOB_NAME"}-第${BUILD_NUMBER}次构建日志</title>
  </head>
<body leftmargin="8" marginwidth="0" topmargin="8" marginheight="4" offset="0">
  <table width="95%" cellpadding="0" cellspacing="0"
    style="font-size: 11pt; font-family: Tahoma, Arial, Helvetica, sans-serif">
    <tr>
        <div>
            <p>本邮件由系统自动发出，无需回复</p>
            <p>小主，您好！以下为${PROJECT_NAME}项目构建信息</p>
            <p>
                <font color="#CC0000">构建结果 - ${BUILD_STATUS}</font>
            </p>
        </div>
    </tr>
    <tr>
        <td><br />
            <b>
                <font color="#0B610B">构建信息</font>
            </b>
            <hr size="2" width="100%" align="center" />
        </td>
    </tr>
    <tr>
        <td>
            <ul>
                <li>项目名称 ： ${PROJECT_NAME}</li>
                <li>构建编号 ： 第${BUILD_NUMBER}次构建</li>
                <li>触发原因： ${CAUSE}</li>
                <li>构建状态： ${BUILD_STATUS}</li>
                <li>构建日志： <a href="${BUILD_URL}console">${BUILD_URL}console</a></li>
                <li>构建 Url ： <a href="${BUILD_URL}">${BUILD_URL}</a></li>
                <li>工作目录 ： <a href="${PROJECT_URL}ws">${PROJECT_URL}ws</a></li>
                <li>项目 Url ： <a href="${PROJECT_URL}">${PROJECT_URL}</a></li>
            </ul>
            <h4>
                <font color="#0B610B">失败用例</font>
            </h4>
            <hr size="2" width="100%" />
            $FAILED_TESTS<br />
            <hr size="2" width="100%" />
            <ul>
                ${CHANGES_SINCE_LAST_SUCCESS, reverse=true, format="%c", changesFormat="<li>%d [%a] %m</li>"}
            </ul>
            <p>详细提交: <a href="${PROJECT_URL}changes">${PROJECT_URL}changes</a></p>
        </td>
    </tr>
  </table>
</body>
</html>
              '''

        emailext(
            to: to,
            subject: subject,
            mimeType: mimeType,
            body: body
        )
      }
    }
  }
}

