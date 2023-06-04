from translate import Translator
def Ganesh():

	# Define the text to be translated
	text = "how are you?"

	# Define the target language
	target_language = 'fr'  # French


	# Initialize the translator
	translator = Translator(to_lang=target_language)

	# Translate the text
	translated_text = translator.translate(text)

	# Print the translated text
	try:
		print(translated_text)
	except UnicodeEncodeError:
		print(translated_text.encode('ascii', 'ignore').decode('ascii'))
Ganesh()
