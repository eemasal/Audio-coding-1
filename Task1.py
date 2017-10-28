# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:07:35 2016

@author: Emad
"""

import scipy.io.wavfile as wav
import pyaudio
import numpy
import numpy as np
import matplotlib.pyplot as plt
import cPickle as pickle

def playFile(audio, samplingRate, channels):


    p = pyaudio.PyAudio()

    # open audio stream

    stream = p.open(format=pyaudio.paInt16,
                    channels=channels,
                    rate=samplingRate,
                    output=True)
    # play. May repeat with different volume values (if done interactively)


    sound = (audio.astype(numpy.int16).tostring())
    stream.write(sound)

    # close stream and terminate audio object
    stream.stop_stream()
    stream.close()
    p.terminate()
    return




#define stream chunk Track48 sndfile
chunk = 102



samplerate, wavArray = wav.read("Track48.wav")

print (wavArray[20], len(wavArray), samplerate, wavArray.dtype, "Shape", wavArray.shape)

'''
try:
	if wavArray.shape[1] == 2:
		left = wavArray[:, 0]
		right = wavArray[:, 1]
except:
	# print('Wavefile is already mono')
	a = 1
'''



audio = wavArray #input_quantized #quant_stereo #left #wavArray left_quantized

channels = 2

#playFile(wavArray, samplerate*2, channels)
#time=len(wavArray)/samplerate

print samplerate
print wavArray.dtype

#samplerate1 = 22500
#playFile(audio, samplerate1, channels)


nsample=len(wavArray)
middle=nsample/2
d=4*samplerate
data=wavArray[middle-d:middle+d]
#playFile(data,samplerate, channels)


maxval0=float(np.amax(data[:,0]))
maxval1=float(np.amax(data[:,1]))


a=np.divide(data[:,0],maxval0)
b=np.divide(data[:,1],maxval1)

data1=np.array([a,b])
data1=np.transpose(data1)
#playFile(data,samplerate, channels)

plt.figure(1)
plt.plot(data)
plt.figure(2)
plt.plot(data1)


a=data[:,1]
for i in range(0,chunk*4,chunk):
    print i
    b=np.fft.fft(a[i:chunk+i])
    plt.plot(b)
plt.legend(['1st= b', '2nd = b', '3rd = b', '4th = b'], loc='down right')

plt.show()
