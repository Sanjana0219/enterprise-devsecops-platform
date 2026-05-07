#!/bin/bash

echo "=================================="
echo "Running Enterprise Policy Gate"
echo "=================================="

echo "Checking for HIGH or CRITICAL vulnerabilities..."

if grep -i "CRITICAL" trivy-report.txt; then
  echo "CRITICAL vulnerabilities detected!"
  exit 1
fi

if grep -i "HIGH" trivy-report.txt; then
  echo "HIGH vulnerabilities detected!"
  exit 1
fi

echo "No blocking vulnerabilities found"
echo "Policy Gate Passed"