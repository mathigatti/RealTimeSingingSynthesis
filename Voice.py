import os

from Constants import *
from Composer import compose
from VoiceSpecificator import generateVoiceSpecification

def renderizeVoice(outputName,lyrics,notes,durations,tempo,scale,languageCode):

	compose(notes,durations,scale,LAST_MIDI,VOICE_XML_ORIGINAL)

	lyrics = tokenize(lyrics)

	generateVoiceSpecification(lyrics,tempo,VOICE_XML_ORIGINAL,VOICE_XML_PROCESSED)

	os.system("LD_LIBRARY_PATH=/usr/lib synthesisSoftware/Sinsy-NG-0.0.1/build/sinsyNG -t "+str(tempo)+" -m "+languageCode+" -o " + outputName + " " + VOICE_XML_PROCESSED)

def tokenize(text):
	textSyllables = cleanText(text)
	return list(filter(lambda x: len(x) > 0, textSyllables.replace(" ", "-").split("-")))

def cleanText(text):

	text.replace("\n"," ")
	text = text.lower()

	symbolsToDelete = ".,'!?" + '"'
	for symbol in symbolsToDelete:
		text = text.replace(symbol,"")

	return text
