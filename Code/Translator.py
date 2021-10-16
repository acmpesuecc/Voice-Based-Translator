# Importing necessary modules required
import speech_recognition as spr
from translate import *
from gtts import gTTS
import os
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox


root = Tk()
def mictoggle():

    # Creating a recognizer instance
    recog = spr.Recognizer()

    # Creating a microphone instance
    mic = spr.Microphone()

    # Using the mic instance created as a source to capture audio
    with mic as source:
        print("Say Hello to initiate the conversation !")
        print("..........We are trying to detect your voice..........")
            
        # Language code to be translated to - can be changed to translate to different languages
        to_lang = 'hi'
        
        # Creating a translator instance
        translator = Translator(to_lang)

        print("\nWe found you !!!!\n")

        def display():

            slaves = root.pack_slaves()
            for i in slaves:
                    i.destroy()


            def proceed():

                
                # Translating input to selected output language
                try:
                    for i in lb.curselection():
                        select = (lb.get(i))
                    to_lang = (list(d.keys())[list(d.values()).index(select)])
                except:
                    messagebox.showerror("Error","Please choose output language")
                
                
                translator = Translator(to_lang)
                translated_lines = translator.translate(lines)
                text = translated_lines

                def save():
                    
                
                    # Creating a text-to-speech instance
                    speak = gTTS(text=text, lang=to_lang, slow=False)
                    
                    # Saving the output file onto the local computer
                    f = asksaveasfile(initialfile = 'output_voice.mp3', defaultextension=".mp3",filetypes=[(".mp3 files","*.mp3"),("All Files","*.*")])
                    print(f.name)
                    speak.save(f.name)
                    os.system("start "+f.name+" tempo")


                def play():
                    print("\nThe translated audio should be playing in a few seconds !!")
                
                    # Creating a text-to-speech instance
                    speak = gTTS(text=text, lang=to_lang, slow=False)
                    
                    # Saving the output file onto the local computer
                    f = asksaveasfile(initialfile = 'output_voice.mp3', defaultextension=".mp3",filetypes=[(".mp3 files","*.mp3"),("All Files","*.*")])
                    print(f.name)
                    speak.save(f.name)
                    t = f.name
                    # Playing the saved output (translated) audio file
                    import webbrowser
                    webbrowser.open(t)


                but2 = Button(root, text="Save", command=save, relief="raised", width = "25")
                but2.pack(pady=50)
                but3 = Button(root, text="Save & Play", command=play, relief="raised", width = "25")
                but3.pack(pady=50)
                


            lab4 = Label(text = "Choose language")
            lab4.pack(pady=30)
            lab4.config(font=("Courier", 25))
            lb = Listbox (root)
            lb.pack()
            d = {'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu', 'fil': 'Filipino', 'he': 'Hebrew'}
            codes = list(d.values())
            for i in codes:
                lb.insert(0,i)

            print("Start speaking, we are translating as you speak !!")
            
            recog.adjust_for_ambient_noise(source, duration=0.2)
            audio = recog.listen(source,timeout=3,phrase_time_limit=3)
            lines = recog.recognize_sphinx(audio)

            print("Here's what we h eard :", lines)

            lab1 = Label(text = "Here's what we heard")
            lab1.pack(pady=30)
            lab1.config(font=("Courier", 25))
            sep = ttk.Separator(root,orient='horizontal')
            sep.pack(fill='x')
            lab2 = Label(text = lines)
            lab2.config(font=("Courier", 18))
            lab2.pack(pady=20)
            but3 = Button(root, text="Translate", command=proceed, relief="raised", width = "25")
            but3.pack(pady=50)
        
        display()

labelmn = Label(root, text="Click on Enable Mic and start talking")
labelmn.pack(pady=50)
labelmn.config(font=("Courier", 20))        
but1 = Button(root, text="Enable Mic", command=mictoggle, relief="raised")
but1.pack(pady=50)
root.state("zoomed")
root.mainloop()
