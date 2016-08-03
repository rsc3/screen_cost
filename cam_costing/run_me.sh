#!/usr/bin/env bash
##
##

cd ~/Desktop/Lab-data/screen_cost/cam_costing
git pull
python3 cost_tracking.py
git add .
git commit -m "Pushing new costing data"
git push origin master
