#!/bin/bash
python3 models/bcoach_ifdm_lunarlander.py --mode=train --input_file=demonstration/expert_obs/LunarLander-v2.pkl --result_dir=results/bcoach_ifdm/lunarlander/ --model_dir=model/bcoach_ifdm/lunarlander/ --maxEpochs=50 --numExperiments=1