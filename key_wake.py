import pvporcupine
from pvrecorder import PvRecorder
from datetime import datetime

from gtts import gTTS
import os

text = "Hello, I am ChatGPT, a language model developed by OpenAI."



keywords_list = ['hey siri','americano','computer','grapefruit','grasshopper','hey barista','hey google','jarvis','ok google','pico clock','picovoice','porcupine','terminator']

def keywork_wake() :
    
    devices = PvRecorder.get_audio_devices()

    for i in range(len(devices)):
        print('index: %d, device name: %s' % (i, devices[i]))


    try:   
        porcupine = pvporcupine.create(
                access_key='',
                keywords= keywords_list)

        recorder = PvRecorder(device_index=0, frame_length=porcupine.frame_length)
        recorder.start()
        print('Using device: %s' % recorder.selected_device)
        while True:
            pcm = recorder.read()
            result = porcupine.process(pcm)
            if result >= 0:
                print('[%s] Detected %s' % (str(datetime.now()), keywords_list[result]))

    except pvporcupine.PorcupineInvalidArgumentError as e:
        print("PorcupineInvalidArgumentError")
        
keywork_wake()


    