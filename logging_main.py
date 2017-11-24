'''PLAYGROUND---TESTING PURPOSES ONLY'''
import pyHook
import pyttsx
from nltk.corpus import wordnet
import string

speech_engine = pyttsx.init('sapi5') # see http://pyttsx.readthedocs.org/en/latest/engine.html
speech_engine.setProperty('rate', 150)

s=''#to keep track of the sentence typed.
def blindlog_master():
    ## Functions called by each mode ##
    def HookIt(OnKeyboardEvent):
        hm = pyHook.HookManager()
        hm.KeyDown = OnKeyboardEvent
        hm.HookKeyboard()
    def speak(text):
        '''python text to speech function'''
        speech_engine.say(text)
        speech_engine.runAndWait()
    ## The various modes ##
    def Familiar():
        print 'IN FAMILIAR MODE'
        def OnKeyboardEvent(event):
            '''Familiar mode: User gets to explore and get familiar with the keyboard.
               Letters are said as the letter is being typed.'''            
            global s
            if event.WindowName=="blindType Text Editor":            
                key=event.Key
                speak(key)
            return True        
        HookIt(OnKeyboardEvent)
        
        
    def PracticeMode1():
        print 'IN PRACTICE MODE1'
        def OnKeyboardEvent(event):
            '''Practice mode: User has to type VALID words.
               Letters are said cumulatively. User is told if the word is a valid word or not'''
            global s
            if event.WindowName=="blindType Text Editor":            
                key=event.Key
                speak(key)    
                if key=='Space':
                    s=''
                    return True
                if key=='Back':
                    if bool(s):s=s[:-1]
                    return True                
                print 'Key:', key  
                if key in string.ascii_uppercase:
                    s+=key
                print s
                if s in ('HO','AR','HEL','DA'):
                    return True
                if len(s)>1:
                    if wordnet.synsets(s):
                        text=s+' is a valid word, Congratulations!'
                        speak(text)
                    else:speak(text)
            return True        
        HookIt(OnKeyboardEvent)
        
        
    def PracticeMode2():
        print 'IN PRACTICE MODE2'
        def OnKeyboardEvent(event):
            '''Practice mode2: User has to type words.
               Letters are said cumulatively.Word is told regardless of it being a valid word or not'''
            global s
            if event.WindowName=="blindType Text Editor":            
                key=event.Key    
                if key=='Space':
                    speak(s)
                    s=''
                    return True
                if key=='Back':
                    speak(key)
                    if bool(s):s=s[:-1]
                    return True                
                print 'Key:', key  
                if key in string.ascii_uppercase:
                    s+=key
                print s
                if len(s)>1:
                    speak(s)
            return True        
        HookIt(OnKeyboardEvent)
        
        
    def Sentence():
        print 'IN SENTENCE MODE'
        def OnKeyboardEvent(event):
            '''Sentence mode: In this mode, The sequence of words is said when the sentence is complete.'''
            global s
            if event.WindowName=="blindType Text Editor":            
                key=event.Key    
                if key=='Oem_Period':# a full stop
                    speak(s)
                    s=''
                    return True
                if key=='Back':
                    speak(key)
                    if bool(s):s=s[:-1]
                    return True                
                print 'Key:', key  
                if key in string.ascii_uppercase:
                    s+=key
                if key=='Space':s+=' '
                print s
            return True        
        HookIt(OnKeyboardEvent)
        
        
    print '''Modes:
        1) Familiar mode
        2) Practice mode 1 
        3) Practice mode 2
        4) Sentence mode'''
    mode=raw_input('Choose a mode: ')
    if mode=='1':Familiar()
    elif mode=='2':PracticeMode1() 
    elif mode=='3':PracticeMode2() 
    elif mode=='4':Sentence()
    else: print 'Enter a valid option'
        
if __name__ == '__main__':
    import pythoncom
    blindlog_master()
    pythoncom.PumpMessages()
    
 