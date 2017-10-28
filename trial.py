# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 19:31:12 2016

@author: Emad
"""

import scipy.io.wavfile as wav
import pyaudio
import numpy
import numpy as np
import matplotlib.pyplot as plt
import cPickle as pickle

samplerate, wavArray = wav.read("Track48.wav")
g=open('encoded.bin', 'w')
a=np.amax(wavArray)
q=float(2.0*a/2**16)
samples=np.round(wavArray/q)
pickle.dump(samples,g)