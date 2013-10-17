#!/usr/bin/env python
#-*- coding:utf-8 -*-
#-----------------------------------------------------------------------
# Author: delimitry
#-----------------------------------------------------------------------

import sys
import math
from morse import Morse
from wavefile import WaveFile

def generate_sin_wave(sample_rate, frequency, duration, amplitude):
	'''
	Generate a sinusoidal wave based on `sample_rate`, `frequency`, `duration` and `amplitude`.
	`frequency` in Hertz, `duration` in seconds, the values of `amplitude` must be in range [0..1].
	'''
	data = []
	samples_num = int(duration * sample_rate)
	volume = amplitude * 32767
	for n in xrange(samples_num):
		value = math.sin(2 * math.pi * n * frequency / sample_rate)
		data.append(int(value * volume))
	return data

def encode_text_to_morse_wave(text, filename):
	encoded_text = Morse().encode(text)
	encoded_exact_text = Morse('=','===').encode_exact(text)
	print '"%s" in Morse code:' % text
	print encoded_text
		
	sample_rate = 8000 # 8000 Hz
	frequency = 600	# 600 Hz
	dot_dur = 0.050	# 50 ms
	volume = 0.8 # 80%
	
	wave = WaveFile(sample_rate)
	wave_duration = 0
	wave_data = []
	for c in encoded_exact_text:
		wave_duration += dot_dur
		if c != ' ':
			wave_data += generate_sin_wave(sample_rate, frequency, dot_dur, volume)
		else:
			wave_data += generate_sin_wave(sample_rate, frequency, dot_dur, 0)
	wave.add_data_subchunk(wave_duration, wave_data)
	wave.save(filename)

def test():
	encode_text_to_morse_wave('SOS', 'sos.wav')
	encode_text_to_morse_wave('MORSE CODE', 'morse_code.wav')

if __name__ == '__main__':
	if len(sys.argv) == 3:
		encode_text_to_morse_wave(sys.argv[1], sys.argv[2])
	else:
		print 'Usage: %s "text to convert" "filename"' % sys.argv[0]
