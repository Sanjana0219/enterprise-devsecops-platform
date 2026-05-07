#!/bin/bash

echo "================================="
echo "Detecting Customer Application Stack"
echo "================================="

cd customer-app

# NODE.JS DETECTION
if [ -f "package.json" ]; then
  echo "Node.js application detected"
  echo "STACK=node" >> $GITHUB_ENV
fi

# PYTHON DETECTION
if [ -f "requirements.txt" ]; then
  echo "Python application detected"
  echo "STACK=python" >> $GITHUB_ENV
fi

# JAVA DETECTION
if [ -f "pom.xml" ]; then
  echo "Java application detected"
  echo "STACK=java" >> $GITHUB_ENV
fi

# DOCKER DETECTION
if [ -f "Dockerfile" ]; then
  echo "Docker configuration detected"
  echo "DOCKER=true" >> $GITHUB_ENV
fi

# TERRAFORM DETECTION
if ls *.tf 1> /dev/null 2>&1; then
  echo "Terraform files detected"
  echo "TERRAFORM=true" >> $GITHUB_ENV
fi

# KUBERNETES DETECTION
if ls *.yaml 1> /dev/null 2>&1; then
  echo "Kubernetes YAML files detected"
  echo "K8S=true" >> $GITHUB_ENV
fi

# HELM DETECTION
if find . -name "Chart.yaml" | grep -q "Chart.yaml"; then
  echo "Helm Chart detected"
  echo "HELM=true" >> $GITHUB_ENV
fi

echo "================================="
echo "Stack Detection Completed"
echo "================================="