from types import SimpleNamespace
from dataclasses import dataclass
from items import itemList
import time
import os
from en import en
from spa import spa

class NestedNamespace(SimpleNamespace):
    def __init__(self, dictionary, **kwargs):
        super().__init__(**kwargs)
        for key, value in dictionary.items():
            if isinstance(value, dict):
                self.__setattr__(key, NestedNamespace(value))
            else:
                self.__setattr__(key, value)

#settings functionallity#
lang = "en"
unit = "imperial"
text = {}
text.update({lang: NestedNamespace(en)})






def settings (lang):
    while(1):
        inp = input(text[lang].settings.options)
        #language
        if(inp == "1"):
            #language options
            lngInp = input(text[lang].settings.languages)
            #english
            if(lngInp == "1"):
                lang = "en"
                text.update({lang: NestedNamespace(en)})
                print(text[lang].settings.enSelected)
            #spanish
            elif(lngInp == "2"):
                lang = "spa"
                text.update({lang: NestedNamespace(spa)})
                print(text[lang].settings.spaSelected)
            else:
                print("invalid input")

        #unita
        elif(inp == "2"):
            #unit options
            unitInp = input(text[lang].settings.units)
            
            #imperial
            if(unitInp =="1"):
                unit = "imperial"
                print(text[lang].settings.ImpSelected)
            
            #metric
            elif(unitInp == "2"):
                unit = "metric"
                print(text[lang].settings.MetSelected)

            elif(inp == "3"):
                return
            else:
                #invalid input
                print(text[lang].settings.inv)

        elif(inp == "3"):
            return
        else:
            print(text[lang].settings.inv)






#shift start func
def shiftStart():
    print(text[lang].shift.start)
    inp = input(text[lang].shift.scanSlct)
    #passive message function

    #scan mode
    if(inp == "1"):
        print(text[lang].shift.scanningMode)
        while(1):
            scn_val = input(text[lang].shift.ready)
            
            if scn_val in itemList:
                print(itemList[scn_val].name)
                print(itemList[scn_val].description)
                print(itemList[scn_val].location)
                print(itemList[scn_val].qty)



            #search for item
            ##if item found, display contents
            #else not found

            if(scn_val == "1"):
                break




#picker mode function 
def picker():
    
    while(1):
    # print(text[lang].picker.select)
     print(text[lang].picker.select)
     inp = input(text[lang].picker.options)
     
     if(inp == "1"):
         shiftStart()
         
     elif(inp == "2"):
         print(text[lang].picker.rtoMode)
         break

    return


#training mode function
def training():
    print("Training mode")


#intro message & ask for mode selection
def main():
    

    print(text[lang].menu.greeting)
    time.sleep(3)
    os.system("clear")
    print(text[lang].menu.modeSelect)
    while(1):

        mode = input(text[lang].menu.modeOpt)

        if (mode == "1"):
            picker()
        elif(mode == "2"):
            settings(lang)
        else:
            print(text[lang].menu.inv)

        


if __name__=="__main__":
     main()


# def main():
#     print("hey there")


# print("Hello")


# Defining main function

  
  
# Using the special variable 
# __name__
