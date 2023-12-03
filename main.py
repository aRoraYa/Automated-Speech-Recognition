from Voice import command
from bolo import Speak
from mygpt import GPT

if __name__=="__main__":
    Speak("hello  its jarvis")
    while 1:
        Q = command()
        C = GPT(Q+" ***reply like tony stark jarvis in less words***")
        Speak(C)


#Liaobots
#You