import numpy as np
from resemblyzer import VoiceEncoder, preprocess_wav
from pathlib import Path

fpath = Path('test.wav')
wav = preprocess_wav(fpath)
encoder = VoiceEncoder()
embed = encoder.embed_utterance(wav)
np.set_printoptions(precision=3, suppress=True)
print(embed)