#!groovy​
pipeline {
    agent any 
    parameters {
        string(name: 'STATUS_EMAIL', defaultValue: 'hwilli@pennmedicine.upenn.edu', description: 'Comma sep list of email addresses that should recieve test status notifications.')
    }
    stages {
        stage('Build Docs') {
            agent {
                docker { 
                    image 'python:3'
                    args '-u root'
                }
            } 
            steps {
                git credentialsId: 'pennai-jenkins', url: 'git@github.com:EpistasisLab/pennai.git'
                sh 'pip install sphinx'    
                dir ('ai') {
                    sh 'make html'
                }
                publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: 'target/ai_docs', reportFiles: 'index.html, search.html, py-modindex.html', reportName: 'AI docs', reportTitles: ''])
            }
        }
        stage('Unit Tests') { 
            agent {
                dockerfile { 
                    dir 'tests/unit'
                    label 'pennai_unit'
                }
            }   
            steps {
                git credentialsId: 'pennai-jenkins', url: 'git@github.com:EpistasisLab/pennai.git'
                sh 'sh tests/unit_test_runner.sh'
                junit 'target/test-reports/*.xml'
                cobertura autoUpdateHealth: false, autoUpdateStability: false, coberturaReportFile: 'target\\test-reports\\cobertura\\nose_cover.xml', conditionalCoverageTargets: '70, 0, 0', failUnhealthy: false, failUnstable: false, lineCoverageTargets: '80, 0, 0', maxNumberOfBuilds: 0, methodCoverageTargets: '80, 0, 0', onlyStable: false, sourceEncoding: 'ASCII', zoomCoverageChart: false
            }
        }
        /*
        stage('Integration Tests') { 
            steps {
                // checkout
                git credentialsId: 'pennai-jenkins', url: 'git@github.com:EpistasisLab/pennai.git'

                // rebuild
                sh 'cp config/ai.env-template config/ai.env'
                sh 'docker build ./dockers/base -t pennai/base:latest'
                sh 'docker-compose build'

                // run tests
                sh 'docker-compose -f ./docker-compose-int-test.yml down'
                sh 'docker-compose -f ./docker-compose-int-test.yml build'
                sh 'docker-compose -f ./docker-compose-int-test.yml up --abort-on-container-exit'
            }
        }
        */
        /*
        stage('Remote Deploy') { 
            steps {
                sh "ssh jenkins@wayland 'git pull'"
                sh "ssh jenkins@wayland 'git clean -xdf'"
                sh "ssh jenkins@wayland 'cp config/ai.env-template config/ai.env'"
                sh "ssh jenkins@wayland 'docker build ./dockers/base -t pennai/base:latest'"
                sh "ssh jenkins@wayland 'docker-compose build'"
            }
        }
        stage('Remote Start') {
            steps {
                sh "ssh jenkins@wayland 'docker-compose down'"
                sh "ssh jenkins@wayland 'docker-compose up -d'"
            }
        }
        */
    }
    /*
    post {
        always {
            junit 'target/test-reports/*.xml'
            cobertura autoUpdateHealth: false, autoUpdateStability: false, coberturaReportFile: 'target\\test-reports\\cobertura\\nose_cover.xml', conditionalCoverageTargets: '70, 0, 0', failUnhealthy: false, failUnstable: false, lineCoverageTargets: '80, 0, 0', maxNumberOfBuilds: 0, methodCoverageTargets: '80, 0, 0', onlyStable: false, sourceEncoding: 'ASCII', zoomCoverageChart: false
        }
        /*
        failure {
            echo 'Pipeline failure'
            emailext attachLog: false, 
                compressLog: false,
                subject: 'Job \'${JOB_NAME}\' (${BUILD_NUMBER}) failure',
                body: 'Please go to ${BUILD_URL} to view build details.', 
                to: "${params.STATUS_EMAIL}",
                //recipientProviders: [culprits()],
                replyTo: "${params.STATUS_EMAIL}"
        }
        fixed {
            echo 'Pipeline is back to normal'
            emailext attachLog: false, 
                compressLog: false,
                subject: 'Job \'${JOB_NAME}\' (${BUILD_NUMBER}) is back to normal',
                body: 'Please go to ${BUILD_URL} to view build details.', 
                to: "${params.STATUS_EMAIL}",
                //recipientProviders: [culprits()], 
                replyTo: "${params.STATUS_EMAIL}"
        }
    }
    */
}