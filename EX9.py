from gtts import gTTS

def text_to_speech():
 text = input("Enter the text to convert to speech: ")
 language = 'ta' # Set the language code to 'bn' for Bengali
 tts = gTTS(text=text, lang=language)
 tts.save('C:\\Users\\CSE-219-50\\Downloads\\Hello_World_Audio.mp3')

# Call the function to convert text to speech
text_to_speech()