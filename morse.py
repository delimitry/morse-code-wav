#!/usr/bin/env python
#-*- coding:utf-8 -*-
#-----------------------------------------------------------------------
# Author: delimitry
#-----------------------------------------------------------------------

class Morse(object):
	'''
	Morse encode/decode class
	'''

	def __init__(self, dit_sign='.', dah_sign='-'):
		self.morse_table = self.MORSE_TABLE
		self.dit_sign = dit_sign
		self.dah_sign = dah_sign

	def encode(self, data):
		result = ''
		for c in data:
			result += self.morse_table.get(c, c) + ' '
		result = result[:-1].replace('.', self.dit_sign).replace('-', self.dah_sign) # cut the last space and replace dits, dahs
		return result

	def decode(self, data):
		decode_morse_table = dict((self.morse_table[k], k.upper()) for k in self.morse_table)
		result = ''
		words = data.split('   ')
		for w in words:
			for c in w.split(' '):
				result += decode_morse_table.get(c, c)
			result += ' '
		result = result[:-1] # cut the last space
		return result

	def encode_exact(self, data):
		'''
		Encode with exact time conventions
		'''
		result = ''
		for c in data:
			result += (' ' * self.INTER_GAP).join(list(self.morse_table.get(c, c))) + ' ' * self.LETTERS_GAP
		result = result[:-self.LETTERS_GAP].replace('.', self.dit_sign).replace('-', self.dah_sign) # cut the last spaces and replace dits, dahs
		return result 

	DOT_DURATION = 1
	DAH_DURATION = 3 * DOT_DURATION
	INTER_GAP = DOT_DURATION
	LETTERS_GAP = 3 * DOT_DURATION
	WORDS_GAP = 7 * DOT_DURATION

	MORSE_TABLE = {
		'A': '.-',
		'B': '-...',
		'C': '-.-.',
		'D': '-..',
		'E': '.',
		'F': '..-.',
		'G': '--.',
		'H': '....',
		'I': '..',
		'J': '.---',
		'K': '-.-',
		'L': '.-..',
		'M': '--',
		'N': '-.',
		'O': '---',
		'P': '.--.',
		'Q': '--.-',
		'R': '.-.',
		'S': '...',
		'T': '-',
		'U': '..-',
		'V': '...-',
		'W': '.--',
		'X': '-..-',
		'Y': '-.--',
		'Z': '--..',

		'a': '.-',
		'b': '-...',
		'c': '-.-.',
		'd': '-..',
		'e': '.',
		'f': '..-.',
		'g': '--.',
		'h': '....',
		'i': '..',
		'j': '.---',
		'k': '-.-',
		'l': '.-..',
		'm': '--',
		'n': '-.',
		'o': '---',
		'p': '.--.',
		'q': '--.-',
		'r': '.-.',
		's': '...',
		't': '-',
		'u': '..-',
		'v': '...-',
		'w': '.--',
		'x': '-..-',
		'y': '-.--',
		'z': '--..',

		'0': '-----',
		'1': '.----',
		'2': '..---',
		'3': '...--',
		'4': '....-',
		'5': '.....',
		'6': '-....',
		'7': '--...',
		'8': '---..',
		'9': '----.',

		'.': '.-.-.-',
		',': '--..--',
		'?': '..--..',
		"'": '.----.',
		'!': '-.-.--',
		'/': '-..-.',
		'(': '-.--.',
		')': '-.--.-',
		'&': '.-...',
		':': '---...',
		';': '-.-.-.',
		'=': '-...-',
		'+': '.-.-.',
		'-': '-....-',
		'_': '..--.-',
		'"': '.-..-.',
		'$': '...-..-',
		'@': '.--.-.',
	}
