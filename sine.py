# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 15:54:41 2020

@author: Humberto Basurto
"""

import numpy as np
import wave, math

sRate = 44100
nSamples = sRate * 5
x = np.arange(nSamples)/float(sRate)
vals = np.sin(2.0*math.pi*146.83*x)
data = np.array(vals * 32767, 'int16').tostring()
file = wave.open('sine146_83.wav', 'wb')
file.setparams((1, 2, sRate, nSamples, 'NONE', 'uncompressed'))
file.writeframes(data)
file.close()