#!/bin/bash

if [ ! -L /home/jovyan/jenkins-workspace ]; then
  ln -s /home/jovyan/.jenkins/workspace /home/jovyan/jenkins-workspace
fi
