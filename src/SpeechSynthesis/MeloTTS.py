from melo.api import TTS
from pathlib import Path
from utils import get_all_filenames_from_directory
import warnings
warnings.filterwarnings('ignore')


def load_meloTTS_model():
    speed = 1.0
    device='auto'
    model = TTS(language='ES', device=device)
    speakers_ids = model.hps.data.spk2id

    return model, speakers_ids, speed

def synthesize(model_dir, word_list, output_dir):
    print('Synthesizing using MeloTTS Model')
    for word in word_list:
        synthesized_words = get_all_filenames_from_directory(output_dir)
        if word in synthesized_words:
            print('Already synthesized')
            continue
        print('Synthesizing {} word'.format(word))
        
        filename = word + '.wav'
        output_path = Path(output_dir, filename)
        model, speakers_ids, speed = load_meloTTS_model()
        model.tts_to_file(word, speakers_ids['ES'], output_path, speed=speed)

    print('Synthesizing completed')