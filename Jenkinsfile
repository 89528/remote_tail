node{
    def appenv = '/var/lib/jenkins/workspace/test_job'
    stage ('Clone repository'){
        checkout([$class: 'GitSCM', 
        branches: [[name: '*/master']],
        extensions: [], userRemoteConfigs: [[url: 'https://github.com/89528/remote_tail']]])
    }
    stage ('Run application'){
        dir("{$appenv}/remote_tail_web")
        sh 'python3 manage.py runserver 127.0.0.1:8001'
    }
}
