# SMT-project-C-Christmasify

## Installation

To install libraries for the LSMT
```bash
pip install --upgrade https://github.com/Theano/Theano/archive/master.zip
pip install --upgrade https://github.com/Lasagne/Lasagne/archive/master.zip
```

## Usage

To generate songs (in this case with the "folkrnn_v2.pkl" model):
```bash
python sample_rnn.py --terminal metadata/folkrnn_v2.pkl
```

To train a model on the "v2_data" dataset:
```bash
python train_rnn.py config5 data/v2_data
```

To parse abc songs to RNN format (dataset.txt):
```bash
python FolkRNN-parser.py -f ../datasets/FOLDER_ABC/ -o DATASET_RNN.txt --include_titles
```
