import os
from pathlib import Path

CUR_DIR = os.getcwd()


FUNCTION = 'ANALYSIS'

# if ANALYSIS set 
SUB_FUNCTION = 'SNR'

# Specify the path of the excel file contaning the list of words
WORDS_FILE_PATH = Path(CUR_DIR, 'FILES/ListWords.xlsx' )
# Path to the directory for synthesized words
SYNTH_WORDS_DIR = Path(CUR_DIR, 'SynthesizedSpeech')

ANALYSIS_DIR = Path(CUR_DIR, 'Analysis')
'''
    Models :
        MeloTTS: python 3.9
        MozillaTTS: python 3.8
        FacebookTTS: python 3.10 and torchaudi 2.0.1
'''
SELECT_MODEL_NAME = 'MeloTTS' 
MODEL_DIR = Path(CUR_DIR, 'MODELS')
SELECTED_MODEL_DIR = Path(MODEL_DIR, SELECT_MODEL_NAME)

IMAGE_DIR = Path(CUR_DIR, 'Images')


