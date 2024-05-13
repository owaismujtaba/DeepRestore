from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
from pathlib import Path
import pdb
import config
import os

def visualize_snr_data(filepath = r'C:\DeepRESTORE\Analysis\snr.csv'):
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
    


