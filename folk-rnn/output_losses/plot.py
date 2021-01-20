import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import glob

dirs = os.listdir('./output_losses')
for dir in dirs:
    if (dir!='.DS_Store' and dir!='plot.py' and dir!='plots'):
        os.chdir('./output_losses/'+dir)
        files = glob.glob('*.{}'.format('csv'))

        #global df_training
        #global df_test
        for file in files:
            if file.endswith("train.csv"):
                df_training = pd.read_csv(file)
            if file.endswith("test.csv"):
                df_test = pd.read_csv(file)

        # rolling average
        df_training['ra'] = df_training['train_loss'].rolling(window=100).mean()

        df_training['ra'] = np.log2(df_training['train_loss'])
        df_test['test_loss'] = np.log2(df_test['test_loss'])


        ax = plt.gca()
        df_training.plot(kind='line',x='epoch',y='ra',ax=ax)
        df_test.plot(kind='line',x='epoch',y='test_loss',ax=ax)
        plt.title(dir)
        plt.grid()
        plt.ylabel('log loss')

        plt.savefig('../plots/'+dir+'_plot.png')
        plt.show()

        os.chdir('../..')



