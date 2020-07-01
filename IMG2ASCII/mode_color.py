try:
    import sys
    from main_script import img_to_ascii #Imports the main script (Only needed if this isnt the main script)
    img_to_ascii(sys.argv[1],True,False,[" ",".",")","#","@"],"") #[image,color(True/False),Just_Color_mode(True/False),Loading Sreen(True/False),[Ascii characters to use (in a list)],scale input(%)]
except Exception as e: #If error, then it will display error message here
  print(e)
  x = input("Stop")