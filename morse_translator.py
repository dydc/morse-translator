from dataclasses import dataclass

@dataclass 
class Translation():
	CHARS_TO_MORSE_CODE_MAPPING = {
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
		'1': '.----',
		'2': '..---',
		'3': '...--',
		'4': '....-',
		'5': '.....',
		'6': '-....',
		'7': '--...',
		'8': '---..',
		'9': '----.',
		'0': '-----',
		'.': '.-.-.-',
		',': '--..--',
		'?': '..--..',
		'\'': '· − − − − ·',
		'!': '− · − · − −',
		'/': '− · · − ·',
		'(': '− · − − ·',
		')': '− · − − · −',
		'&': '· − · · ·',
		':': '− − − · · ·',
		';': '− · − · − ·',
		'=': '− · · · −',
		'+': '· − · − ·',
		'-': '− · · · · −',
		'_': '· · − − · −',
		'"': '· − · · − ·',
		'$': '· · · − · · −',
		'@': '· − − · − ·',
	}

	MORSE_CODE_TO_CHARS_MAPPING = {v: k for k, v in CHARS_TO_MORSE_CODE_MAPPING.items()}

	src:str = ''
	out:str = ''

	def translate(self):
		pass

@dataclass 
class EnglishToMorse(Translation):
	def translate(self):
		out = []
		words = self.src.split(' ')
		for word in words:
			w = []
			for c in word.upper():
				if c in self.CHARS_TO_MORSE_CODE_MAPPING:
					w.append(self.CHARS_TO_MORSE_CODE_MAPPING[c])
				else:
					print('c', c)
					return 'Invalid Morse Code Or Spacing'
			out.append(' '.join(w).lower())
		self.out = '   '.join(out)
		return self.out

@dataclass 
class MorseToEnglish(Translation):
	
	def translate(self):
		out = []
		words = self.src.split('   ')
		for word in words:
			w = []
			for c in word.split(' '):
				if c in self.MORSE_CODE_TO_CHARS_MAPPING:a
					w.append(self.MORSE_CODE_TO_CHARS_MAPPING[c])
				else:
					return 'Invalid Morse Code Or Spacing'
			out.append(''.join(w).lower())
		self.out = ' '.join(out)
		return self.out

class Solution:
	
	def run(self, morseToEnglish, textToTranslate):
		service = MorseToEnglish if morseToEnglish else EnglishToMorse
		translatedText = service(textToTranslate).translate()
		return translatedText
