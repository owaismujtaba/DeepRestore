import os
import argparse
import config
import pdb

from utils import get_word_list_for_synthesis
from synthesize_words import synthesize_words

def main():

    parser = argparse.ArgumentParser()
 
    parser.add_argument('--FUNCTION', 
                        help='what to do', 
                        default=config.FUNCTION,
                        required=False
                    )
    parser.add_argument('--SELECTED_MODEL_DIR',
                        default=config.SELECTED_MODEL_DIR,
                        required=False
                    )
    parser.add_argument('--WORDS_FILE_PATH', 
                        default=config.WORDS_FILE_PATH,
                        required=False
                    )
    parser.add_argument('--SYNTH_WORDS_DIR', 
                        default=config.SYNTH_WORDS_DIR,
                        required=False)

    parser.add_argument('--SUB_FUNCTION', 
                        default=config.SUB_FUNCTION,
                        required=False)

    arguments = parser.parse_args()

    if arguments.FUNCTION == 'RUN_SYNTHESIS_WORDS':
        
        word_list = get_word_list_for_synthesis(arguments.WORDS_FILE_PATH)
        synthesize_words(arguments.SELECTED_MODEL_DIR, word_list, arguments.SYNTH_WORDS_DIR)

    elif arguments.FUNCTION == 'ANALYSIS':
        if arguments.SUB_FUNCTION == 'SNR':
            from audio_quality import analyze_files
            analyze_files(arguments.SUB_FUNCTION, arguments.SYNTH_WORDS_DIR, config.ANALYSIS_DIR)

if __name__=='__main__':
    main()