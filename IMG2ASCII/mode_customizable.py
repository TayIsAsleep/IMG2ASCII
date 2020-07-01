try:
    import sys
    from main_script import img_to_ascii #Imports the main script (Only needed if this isnt the main script)
    from pyautogui import confirm,prompt    
    #import ctypes
    #ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )

    def YN(_ask):
        
        ans = confirm(text=_ask, title="Image2Ascii", buttons=['Yes', 'No',"Cancel"])
        if ans == "Yes":
            return True
        elif ans == "No":
            return False
        else:
            exit()
            
    img_to_ascii(sys.argv[1],(YN("Do you want colors?")),False,[" ",".",")","#","@"],(prompt(text='How should the image be scaled? \n("100" = 100% of the pixels being used)', title='Image2Ascii' , default=''))) #[image,color(True/False),Just_Color_mode(True/False),Loading Sreen(True/False),[Ascii characters to use (in a list)],scale input(%)]
except Exception as e: #If error, then it will display error message here
  #ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 9 )
  print(e)
  x = input("Stop")