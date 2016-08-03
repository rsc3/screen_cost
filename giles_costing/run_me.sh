#!/usr/bin/env bash
##
##

cd /Users/gochs/Documents/MetaMixis/FInances/Costing/github_tracking/screen_cost/giles_costing/
git pull
python3 cost_tracking.py
git add .
git commit -m "Pushing new costing data"
git push origin master
