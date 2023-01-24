from gtts import gTTS
import os
import time
import openai
from colorama import Fore, Back, Style, init
init()
os.system("clear")
verde = Fore.GREEN
azul = Fore.BLUE
magenta = Fore.MAGENTA
cyan = Fore.CYAN
style = Style.BRIGHT

openai.api_key = "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"

conversation = ""

i = 1

while( i != 0 ):
    question = input(azul + style + "Turing: " + Fore.WHITE)
    conversation += "\nTuring: " + question + "\nIA: "
    response = openai.Completion.create(
        engine = "davinci",
        prompt = conversation ,
        temperature = 0.9 ,
        max_tokens = 150 ,
        top_p = 1 ,
        frequency_penalty = 0 ,
        presence_penalty = 0.6 ,
        stop = ["\n", "Turing: ", "\n", "IA: "]
    )

    anwer = response.choices[0].text.strip()
    conversation += anwer
    
    languaje = 'es'

    speech = gTTS(text = anwer, lang = languaje, slow = False)
    print(verde + "\n" + "IA " + cyan + anwer + "\n")
    os.system("rm Vos.mp3")
    
    speech.save("Vos.mp3")
    os.system("nohup mpv Vos.mp3 > foo.out 2> foo.err < /dev/null &")
    time.sleep(1.5)
    os.system("rm foo.out foo.err")
    f = open("convers.txt","a")
    f.write("\n" + question + "\n" + anwer + "\n")
    f.close()
