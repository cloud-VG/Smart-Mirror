import eel
import Snowboy.snowboydecoder as snowboydecoder
from threading import Thread
from time import sleep


eel.init('web')
detector = snowboydecoder.HotwordDetector("OK Google.pmdl", sensitivity=0.5, audio_gain=1)


def detected_callback():
    print("hotword detected")
    # TODO: add assistant routine
    

def init_eel():
    """
    Initialization of electron window
    :return:
        None
    """
    eel.start('index.html', size=(500, 500))


def init_snowboy():
    """
    Initialization of Hotword Detector
    :return:
        None
    """
    detector.start(detected_callback)

    
thread_eel = Thread(target=init_eel)
thread_snowboy = Thread(target=init_snowboy)

thread_eel.start()
thread_snowboy.start()
