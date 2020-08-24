import speech_recognition as sr 
import playsound 
from gtts import gTTS 
import os 
import wolframalpha 
from selenium import webdriver
al=0



num = 1
def assistant_speaks(output): 
                global num
                if al==3:
                    import MAILALERT
                
                num += 1
                print("PerSon : ", output) 

                toSpeak = gTTS(text = output, lang ='en', slow = False) 
                file = str(num)+".mp3" 
                toSpeak.save(file) 
                

                playsound.playsound(file, True) 
                os.remove(file) 



def get_audio(): 

                rObject = sr.Recognizer() 
                audio = '' 

                with sr.Microphone() as source: 
                                print("Speak...") 
                                
                                
                                audio = rObject.listen(source, phrase_time_limit = 2) 
                print("Stop.") 

                try: 

                                text = rObject.recognize_google(audio, language ='en-US') 
                                print("You : ", text) 
                                return text 

                except: 

                                assistant_speaks("Try Again") 
                                



if __name__ == "__main__":
       
                
                while al<=3: 

                                assistant_speaks("If you are well say thank You") 
                                text = get_audio() 

                                if text == None or text == '':
                                        al=al+1
                                       
                                        continue

                                elif "thank you" in str(text) : 
                                                assistant_speaks("starting in a second")
                                                
                                                break
                
                                process_text(text)
                                
