#!/bin/bash

set -Eeuo pipefail

echo "Opening bot repository"
cd /home/git_deployer/rabotnichki_bot

echo "Pulling changes from github"
git switch main
git pull

echo "Updating .venv"
./.venv/bin/python -m pip install -r requirements.txt

echo "Restarting service"
sudo systemctl restart rabotnichki_bot.service 

echo "Checking status"
sudo systemctl is-active --quiet rabotnichki_bot.service 

echo "Bot deployed successfully!"
