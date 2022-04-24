import time
import os

#settings functionallity#
language = "english"
unit = "imperial"


def settings ():
    while(1):
        inp = input("settings: (1) language (2) unit (3) exit\n")
        #language
        if(inp == "1"):
            lngInp = input("select language:(1) english, (2) spanish\n")
            if(lngInp == "1"):
                language = "english"
                print("%s selected", language)
            elif(lngInp == "2"):
                language = "spanish"
                print("%s selected", unit)
            else:
                print("invalid input")

        #unit
        elif(inp == "2"):
            unitInp = input("select unit: (1)imperial(lb) (2)metric\n")
            if(unitInp =="1"):
                unit = "imperial"
                print("%s selected", unit)
            elif(unitInp == "2"):
                unit = "metric"
                print("%s selected", unit)

        elif(inp == "3"):
            return
        else:
            print("invalid input\n")






#shift start func
def shiftStart():
    print("shift started")
    inp = input("(1) scanning mode")
    #passive message function

    #scan mode
    if(inp == "1"):
        print("scanning mode")
        while(1):
            scn_val = input("ready for scan")

            #search for item
            ##if item found, display contents
            #else not found

            if(scn_val == "1"):
                break




#picker mode function 
def picker():
    
    while(1):
     print("Picker Mode\npress (x) times to select\n")
     inp = input("(1) start shift\n(2) mode selection\n")
     
     if(inp == "1"):
         shiftStart()
         
     elif(inp == "2"):
         print("returning to mode selection")
         break

    return


#training mode function
def training():
    print("Training mode")


#intro message & ask for mode selection
def main():
    print("\nHello!\nWelcome to Shipbob AR")
    time.sleep(3)
    os.system("clear")
    print("Please select work mode\nPress (x) times to select\n")
    while(1):

        mode = input("(1) Picker mode\n(2) Settings\n")

        if (mode == "1"):
            picker()
        elif(mode == "2"):
            settings()
        else:
            print("invalid input")

        


if __name__=="__main__":
     main()


# def main():
#     print("hey there")


# print("Hello")


# Defining main function

  
  
# Using the special variable 
# __name__
