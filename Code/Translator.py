import json
def welcome():
	print("Welcome to your dashboard")

def gainAccess(Username=None, Password=None):
	Username = input("Enter your username:")
	Password = input("Enter your Password:")
	import Translator
	translator=Translator()
	out=translator.translate(username)
	out1=translator.translate(password)
	print(out)
	print(out1)

	if not len(Username or Password) < 1:

		if True:
			db = open("database.txt", "r")
			d = []
			f = []
			for i in db:
				a,b = i.split(",")
				b = b.strip()
				c = a,b
				d.append(a)
				f.append(b)
			data = dict(zip(d, f))
			# print(data)


			try:
				if data[Username]:
					try:
						if Password == data[Username]:
							print("Login success!")
							print("Hi", Username)
							welcome()
						else:
							print("Incorrect password or username")
					except:
						print("Incorrect password or username")


				else:
					print("Password or username doesn't exist")
			except:
				print("Password or username doesn't exist")

		else:
			print("Error logging into the system")

	else:
		print("Please attempt login again")
		gainAccess()

		# b = b.strip()
# accessDb()




def register(Username=None, Password1=None, Password2=None):
	Username = input("Enter a username:")
	Password1 = input("Create password:")
	Password2 = input("Confirm Password:")

	db = open("database.txt", "r")
	d = []
	for i in db:
		a,b = i.split(",")
		b = b.strip()
		c = a,b
		d.append(a)

	if not len(Password1)<=8:
		db = open("database.txt", "r")

		if not Username ==None:
			if len(Username) <1:
				print("Please provide a username")
				register()
			elif Username in d:
				print("Username exists")
				register()


			else:

				if Password1 == Password2:
					db = open("database.txt", "a")
					db.write(Username+", "+Password1+"\n")
					print("User created successfully!")
					print("Please login to proceed:")


					# print(texts)


				else:
					print("Passwords do not match")
					register()

	else:
		print("Password too short")



def home(option=None):
	print("Welcome, please select an option")
	option = input("Login | Signup:")
	if option == "Login":
		gainAccess()
	elif option == "Signup":
		register()
	else:
		print("Please enter a valid parameter, this is case-sensitive")




# register(Username, Password1, Password2)
# gainAccess(Username, Password1)
home()


from gtts import gTTS
import os

# Creating a recognizer instance
recog = spr.Recognizer()

# Creating a microphone instance
mic = spr.Microphone()

# Using the mic instance created as a source to capture audio
with mic as source:
    print("Say Hello to initiate the conversation !")
    print("..........We are trying to detect your voice..........")

    # Eliminating echoes/gaps/disturbances in the audio being captured
    recog.adjust_for_ambient_noise(source, duration=0.2)
    audio = recog.listen(source)

    # Converting audio recorded into lower case text
    Text = recog.recognize_sphinx(audio).lower()

    # Looking for prompt
    if 'hello' in Text:

        # Language code to be translated to - can be changed to translate to different languages
        to_lang = 'hi'

        # Creating a translator instance
        translator = Translator(to_lang)

        print("\nWe found you !!!!\n")
	@@ -26,13 +37,19 @@
        recog.adjust_for_ambient_noise(source, duration=0.2)
        audio = recog.listen(source)
        lines = recog.recognize_sphinx(audio)
        
        print("Here's what we heard :", lines)

        # Translating input to selected output language
        translated_lines = translator.translate(lines)
        text = translated_lines
        print("\nThe translated audio should be playing in a few seconds !!")

        # Creating a text-to-speech instance
        speak = gTTS(text=text, lang=to_lang, slow=False)

        # Saving the output file onto the local computer
        speak.save("output_voice.mp3")

        # Playing the saved output (translated) audio file
        os.system("start output_voice.mp3 tempo")




