from transformers import VitsModel, AutoTokenizer
import torch
from scipy.io.wavfile import write
from pathlib import Path
import torchaudio
import warnings
from utils import get_all_filenames_from_directory
warnings.filterwarnings('ignore')
import pdb
def load_facebookTTS_model():
    
    model = VitsModel.from_pretrained("facebook/mms-tts-spa")
    tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-spa")
    
    return model, tokenizer

def synthesize(model_dir, word_list, output_dir):
    print('Synthesizing using Facebook TTS Model')
    for word in word_list:

        synthesized_words = get_all_filenames_from_directory(output_dir)
        if word in synthesized_words:
            print('Already synthesized')
            continue
        print('Synthesizing {} word'.format(word))
        
        filename = word + '.wav'
        output_path = Path(output_dir, filename)
        model, tokenizer = load_facebookTTS_model()
        inputs = tokenizer(word, return_tensors="pt")

        with torch.no_grad():
            output = model(**inputs).waveform
            
        torchaudio.save(output_path, output, model.config.sampling_rate, format='wav')
        

    print('Synthesizing completed')