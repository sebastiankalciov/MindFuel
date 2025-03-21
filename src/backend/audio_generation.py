import torch
from TTS.api import TTS

import shared_variable

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"



# Initialize TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# List speakers
print(tts.speakers)

# Run TTS
# ❗ XTTS supports both, but many models allow only one of the `speaker` and
# `speaker_wav` arguments

# TTS with list of amplitude values as output, clone the voice from `speaker_wav`


# TTS to a file, use a preset speaker
def create_audio(file_path,text_segment,speed):
        tts.tts_to_file(
              text=text_segment,
              speaker="Craig Gutsy",
              language="en",
              file_path=file_path,
              speed= speed
      )


