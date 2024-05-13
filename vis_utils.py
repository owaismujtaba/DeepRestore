from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
from pathlib import Path
from utils import get_word_list_with_frequency_info
import pdb
import config
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from pathlib import Path

def visualize_snr_data_freq_wise(filepath=r'C:\DeepRESTORE\Analysis\snr.csv'):
    data = pd.read_csv(filepath)
    data = data[['Model', 'snr_gaussian', 'snr_white', 'freq_group']]
    
    data['freq_group'].fillna('Unknown', inplace=True)
    
    means = data.groupby(['Model', 'freq_group']).mean()
    stds = data.groupby(['Model', 'freq_group']).std()
    
    print("Means")
    print(means)
    print("Standard Deviations")
    print(stds)
    
    palette = {'MeloTTS': 'skyblue', 'FacebookTTS': 'salmon'}
    models = data['Model'].unique()
    freq_groups = data['freq_group'].unique()
    
    fig, axs = plt.subplots(2, 4, figsize=(24, 12), sharey=True)
    for i, freq_group in enumerate(freq_groups):
        freq_data = data[data['freq_group'] == freq_group]
        for j, snr_type in enumerate(['snr_gaussian', 'snr_white']):
            
            sns.boxplot(x='Model', y=snr_type, data=freq_data, ax=axs[j, i], palette=palette)
            axs[j, i].set_title(f'{snr_type.split("_")[1].capitalize()} SNR - {freq_group}')
            axs[j, i].spines['top'].set_visible(False)  # Remove top spine
            axs[j, i].spines['right'].set_visible(False)  # Remove right spine
            #axs[j, i].set_ylim(0, -40)
            for k, model in enumerate(models):
                mean_val = means.loc[(model, freq_group), snr_type]
                std_val = stds.loc[(model, freq_group), snr_type]
                axs[j, i].text(k, mean_val + 0.05, f"Mean: {mean_val:.2f}\nStd: {std_val:.2f}", ha='center', fontsize=10, color='black')

    plt.tight_layout()
    os.makedirs(config.IMAGE_DIR, exist_ok=True)

    filename_with_path = Path(config.IMAGE_DIR, f'MODEL_SNR_FREQ_ALL.png', dpi=600)
    plt.savefig(filename_with_path)

def visualize_snr_data(filepath = r'C:\DeepRESTORE\Analysis\snr.csv'):
    visualize_snr_data_freq_wise()
    data = pd.read_csv(filepath)
    
    data = data[['Model', 'snr_gaussian', 'snr_white']]
    
    
    means = data.groupby('Model').mean()
    stds = data.groupby('Model').std()
    
    print("Means")
    print(means)
    print("Standard Deviations")
    print(stds)
    
    palette = {'MeloTTS': 'skyblue', 'FacebookTTS': 'salmon'}
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    
    sns.boxplot(x='Model', y='snr_gaussian', data=data, ax=axs[0], palette=palette)
    axs[0].set_title('Gaussian SNR')
    for i, model in enumerate(data['Model'].unique()):
        axs[0].text(i, means.loc[model, 'snr_gaussian'] + 0.05, f"Mean: {means.loc[model, 'snr_gaussian']:.2f}\nStd: {stds.loc[model, 'snr_gaussian']:.2f}", ha='center', fontsize=10, color='black')

    sns.boxplot(x='Model', y='snr_white', data=data, ax=axs[1], palette=palette)
    axs[1].set_title('White SNR')
    for i, model in enumerate(data['Model'].unique()):
        axs[1].text(i, means.loc[model, 'snr_white'] + 0.05, f"Mean: {means.loc[model, 'snr_white']:.2f}\nStd: {stds.loc[model, 'snr_white']:.2f}", ha='center', fontsize=10, color='black')

    plt.tight_layout()
    os.makedirs(config.IMAGE_DIR, exist_ok=True)

    filename_with_path = Path(config.IMAGE_DIR, 'MODEL_SNR.png', dpi=600)
    plt.savefig(filename_with_path)

visualize_snr_data()


    


