#!/bin/bash
python3 models/bcoach_spm_contmcar.py --mode=train --input_file=demonstration/expert_obs/MountainCar-v0.pkl --result_dir=results/bcoach_spm/contmcar/ --model_dir=model/bcoach_spm/contmcar/ --maxEpochs=50 --numExperiments=1 --cont_actions --useSPM