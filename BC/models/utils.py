import tensorflow as tf
import argparse
import os
import pickle
import numpy as np
import datetime as dt
import time

parser = argparse.ArgumentParser()
parser.add_argument("--input_filename", default="demonstration/expert_obs/CartPole-v0.pkl", help="the demonstration inputs")
parser.add_argument("--mode", default="train", choices=["train", "test"], required=True)
parser.add_argument("--session_dir", help="where to save the session")
parser.add_argument("--prev_session_dir", help="where to restore the session from")
parser.add_argument('--usePrevSession', action='store_true')
parser.add_argument("--result_dir", default="results/", help="where to save the results")

parser.add_argument("--epochTrainIts", type=int, default=5000, help="the number of training iterations executed every epoch")
parser.add_argument("--maxEpochs", type=int, default=20, help="the max number of epochs to run")
parser.add_argument("--batch_size", type=int, default=32, help="number of examples in batch")
parser.add_argument("--lr", type=float, default=0.001, help="initial learning rate for adam SGD")

parser.add_argument('--render', action='store_true')
parser.add_argument("--print_freq", type=int, default=1, help="print current reward and loss every print_freq episodes, 0 to disable")

args = parser.parse_args()

def weight_initializer():
  return tf.truncated_normal_initializer(stddev=0.0001)

def bias_initializer():
  return tf.truncated_normal_initializer(stddev=0.0001)