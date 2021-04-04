#!/bin/bash

if [ ! -d /home/jovyan/.jenkins/jobs ]; then
  mkdir -p /home/jovyan/.jenkins/jobs
  chown -R jovyan /home/jovyan/.jenkins/jobs
  cp -pfr /tmp/resource/jenkins-configs/* /home/jovyan/.jenkins/jobs/
fi
