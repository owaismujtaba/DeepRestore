import librosa
import numpy as np
from utils import get_all_files_with_paths
from utils import get_directories_in_current_folder
import math
from pathlib import Path
import pdb
import pandas as pd
import os

def calculate_snr(audio_file, noise):
    signal_power = np.mean(np.abs(audio_file)**2)
    noise_power = np.mean(np.abs(noise)**2)
    snr = 10 * math.log10(signal_power / noise_power)

    return snr

def generate_gaussian_noise_audio(duration, sample_rate, amplitude=1, mean=0.0, std_dev=1.0):
    num_samples = int(duration * sample_rate)
    noise = np.random.normal(mean, std_dev, num_samples) * amplitude
    
    return noise

def generate_white_noise_audio(duration, sample_rate, amplitude=1.0):
    num_samples = int(duration * sample_rate)
    noise = np.random.uniform(-1, 1, num_samples) * amplitude
    
    return noise

def analyze_files(function, folder_path, output_dir):

    if function == 'SNR':
        os.makedirs(output_dir, exist_ok=True)
        directories = get_directories_in_current_folder(folder_path)
        
        snr_data = []
        for directory in directories:
            cur_dir = Path(folder_path, directory)
            files_with_paths = get_all_files_with_paths(cur_dir)
            
            for file in files_with_paths:
                model = str(cur_dir).split('\\')[-1]
                word = file.split('\\')[-1].split('.')[0]
                print("Processing {} file".format(word))
                
                audio_file, sample_rate = librosa.load(file)
                duration = librosa.get_duration(y=audio_file, sr=sample_rate)
                
                gaussian_noise = generate_gaussian_noise_audio(duration, sample_rate)
                white_noise = generate_white_noise_audio(duration, sample_rate)
                snr_gaussian = calculate_snr(audio_file, gaussian_noise)
                snr_white = calculate_snr(audio_file, white_noise)
                
                snr_data.append([word, model, snr_gaussian, snr_white])
                print(snr_gaussian, snr_white)
                
        columns = ['word', 'Model', 'snr_gaussian', 'snr_white']
        snr_data = pd.DataFrame(snr_data, columns=columns)
        output_filename = Path(output_dir, 'snr.csv')
        
        
        snr_data.to_csv(output_filename)

        from vis_utils import visualize_snr_data

        visualize_snr_data(output_filename)
        
        
                
