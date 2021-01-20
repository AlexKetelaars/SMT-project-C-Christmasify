#!/bin/bash
#SBATCH --time=25:00:00
#SBATCH --mem=100G
#SBATCH --mail-type=ALL
#SBATCH --mail-user=EMAIL@DOMAIN.com
#SBATCH --partition gpu --gpus-per-node=RTX6000:1

THEANO_FLAGS='cuda.root=/usr/local/cuda*,device=cuda,floatX=float32' python -u train_rnn.py configX data/dataset_mixed.txt > output_logs/output_mixed.out
THEANO_FLAGS='cuda.root=/usr/local/cuda*,device=cuda,floatX=float32' python -u train_rnn.py configX data/dataset_christmas.txt > output_logs/output_christmas.out
THEANO_FLAGS='cuda.root=/usr/local/cuda*,device=cuda,floatX=float32' python -u train_rnn.py configX data/dataset_dutch.txt > output_logs/output_dutch.out