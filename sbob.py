import time
import os
#picker mode function 
def picker():
    
    while(1):
     print("Picker Mode\npress (x) times to select\n")
     inp = input("(1) start shift\n (2) mode selection")



     
#training mode function











def training():
    print("Training mode")


#intro message & ask for mode selection
print("\nHello!\nWelcome to Shipbob AR")
time.sleep(3)
os.system("clear")
print("Please select work mode\nPress (x) times to select\n")
mode = input("(1) Picker mode\n(2) Training mode\n")

if (mode == "1"):
    picker()
elif(mode == "2"):
    training()





# def main():
#     print("hey there")


# print("Hello")

# if __name__=="__main__":
#     main()
# Defining main function

  
  
# Using the special variable 
# __name__
