
from pathlib import Path
import pdb
import os

def synthesize_words(model_dir, word_list, output_dir):

    model_name = str(model_dir).split('/')[-1]
    output_dir = Path(output_dir, model_name)

    if model_name == 'MozillaTTS':
        from MozillaTTS import synthesize
        os.makedirs(output_dir, exist_ok=True)
        synthesize(model_dir, word_list, output_dir)

    if model_name == 'MeloTTS':
        from src.SpeechSynthesis.MeloTTS import synthesize
        #from MeloTTS import synthesize
        os.makedirs(output_dir, exist_ok=True)
        synthesize(model_dir, word_list, output_dir)
    
    if model_name == 'FacebookTTS':
        from src.SpeechSynthesis.FacebookTTS import synthesize
        os.makedirs(output_dir, exist_ok=True)
        synthesize(model_dir, word_list, output_dir)