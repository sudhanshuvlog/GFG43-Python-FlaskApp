pipeline { //pipeline
    agent {label "python-worker1-ec2" }
    stages { //collection of stages
        stage("Deploy the app in dev env"){ // job1
            steps {
                sh 'docker pull jinny1/gfgpython43cicd:latest'
                sh 'docker run -dit --name webapp -p 80:80 jinny1/gfgpython43cicd:latest'
            }
        }
    }
}