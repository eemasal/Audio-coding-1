# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 11:31:08 2016

@author: Emad
"""
import struct
import scipy.io.wavfile as wav
import pyaudio
import numpy
import numpy as np
import matplotlib.pyplot as plt
import cPickle as pickle

channels =2

def playFile(audio, samplingRate):


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


    
x=np.linspace(-24592,24592,2**16)  
z=np.linspace(-2,2,)  
def encframewk():
    samplerate, wavArray = wav.read("Track48.wav")
    #shorts = (struct.unpack( 'h' * np.size(wavArray), wavArray ));
    #samples=np.array(list(shorts),dtype=float);
    g=open('encoded.txt', 'w')
    a=np.amax(wavArray)
    q=2.0*a/2**16
    samples=np.round(wavArray/q)
    pickle.dump(samples,g)
    return q, samplerate
q,samplerate=encframewk()

def decframewk():
    samples= pickle.load(open("encoded.txt"))
    rec=samples*q
    h=open('decoded.wav', 'w')
    (pickle.dump(rec,h))
    return(rec)


y=decframewk()
#playFile(y,samplerate)

def encframewk8bit():
    samplerate, wavArray = wav.read("Track48.wav")
    g1=open('encoded8bit.txt', 'wb')
    a1=np.amax(abs(wavArray))
    q1=2.0*a1/2**4
    samples1=np.round(wavArray/q1)
    samples1=np.int8(samples1)
    pickle.dump(samples1,g1,1)
    return q1, samplerate
q1,samplerate=encframewk8bit()

def decframewk8bit():
    samples= pickle.load(open("encoded8bit.bin"))
    rec1=samples*q1
    rec1=np.int8(rec1)
    h1=open('decoded8bit.wav', 'w')
    (pickle.dump(rec1,h1))
    return(rec1)


y1=decframewk8bit()
#playFile(y1,samplerate)
#plt.plot(y)
plt.figure(2)
plt.plot(y1)


