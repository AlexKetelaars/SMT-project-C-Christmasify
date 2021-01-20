#!/bin/bash
#SBATCH --time=01:00:00
#SBATCH --mem=100G
#SBATCH --mail-type=ALL
#SBATCH --mail-user=EMAIL@DOMAIN.com
#SBATCH --partition gpu --gpus-per-node=RTX6000:1

THEANO_FLAGS='cuda.root=/usr/local/cuda*,device=cuda,floatX=float32' python -u sample_rnn.py --ntunes 1000 metadata/configX-dataset_dutch-20210120-125233.pkl > output_logs/dutch_sample.out
THEANO_FLAGS='cuda.root=/usr/local/cuda*,device=cuda,floatX=float32' python -u sample_rnn.py --ntunes 1000 metadata/configX-dataset_mixed-20210120-130954.pkl > output_logs/mixed_sample.out
THEANO_FLAGS='cuda.root=/usr/local/cuda*,device=cuda,floatX=float32' python -u sample_rnn.py --ntunes 1000 metadata/configX-dataset_christmas-20210120-121835.pkl > output_logs/christmas_sample.out