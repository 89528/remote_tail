node{
    def appenv = '/var/lib/jenkins/workspace/test_job'
    stage ('Clone repository'){
        checkout([$class: 'GitSCM', 
        branches: [[name: '*/master']],
        extensions: [], userRemoteConfigs: [[url: 'https://github.com/89528/remote_tail']]])
    }
