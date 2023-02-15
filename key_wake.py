import pvporcupine
from pvrecorder import PvRecorder
from datetime import datetime

keywords_list = ['hey siri','americano','computer','grapefruit','grasshopper','hey barista','hey google','jarvis','ok google','pico clock','picovoice','porcupine','terminator']

def keywork_wake() :
    
    devices = PvRecorder.get_audio_devices()

    for i in range(len(devices)):
        print('index: %d, device name: %s' % (i, devices[i]))

    try:   
        porcupine = pvporcupine.create(
                access_key='FcwVRsUlSsRhtdDUYaHnLHP1oDPbdf8N8YUoO1rdX9YnhgZ6fjLspA==',
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


# ./demo/c/build/porcupine_demo_mic -l ./lib/raspberry-pi/cortex-a72-aarch64/libpv_porcupine.so \
# -m ./lib/common/porcupine_params.pv -k ./resources/keyword_files/raspberry-pi/computer_raspberry-pi.ppn \
# -t 0.5 -a FcwVRsUlSsRhtdDUYaHnLHP1oDPbdf8N8YUoO1rdX9YnhgZ6fjLspA== -d 0
