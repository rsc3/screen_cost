#!/usr/bin/env bash
##
##

cd ~/Desktop/metamixis_costing/screen_cost/nina_costing/
git pull
python3 cost_tracking.py
cd ..
git add .
git commit -m "Pushing new costing data"
git push origin master
