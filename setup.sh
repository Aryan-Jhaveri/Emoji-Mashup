#!/bin/bash
set -e

# Update package lists
sudo apt-get update

# Install system dependencies
sudo apt-get install -y zlib1g-dev libjpeg-dev libpng-dev

# Upgrade pip and setuptools
pip install --upgrade pip setuptools

# Install Python dependencies
pip install -r requirements.txt
