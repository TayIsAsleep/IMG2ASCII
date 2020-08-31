try:
    import sys
    from main_script import img_to_ascii
    
    #Set to either True or False:
    use_colors = 
    
    #Make a list of all the characters you want the program to use, from bright to dark.  (for example, ["░","▒","▓","█"]  )
    use_characters = []
    
    #Set a integer value of how much it should scale the image from its original size (100 would result in every pixel in the image being one character)
    #If you want it to scale automaticly like mode_color.py then just make it an empty string (""):
    use_scaling =
    
    img_to_ascii(sys.argv[1],use_colors,False,use_characters,str(use_scaling)) 
except Exception as e: 
  print(e)
  x = input("Stop")