#!/bin/bash
python3 models/tips_cartpole.py --mode=train --input_file=demonstration/expert_obs/CartPole-v0.pkl --result_dir=results/tips/cartpole/ --model_dir=model/tips/cartpole/ --maxEpochs=50 --numExperiments=1