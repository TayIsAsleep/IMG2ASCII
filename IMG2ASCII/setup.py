try:
    import sys
    current_name = (str(sys.argv[0])[-5]) #Checks the last letter in the file name (before the .exe part)
    if current_name == "B": 
        import mode_black_and_white #Runs in B&W preset
    elif current_name == "C":
        import mode_color #Runs in Color preset
    elif current_name == "D":
        import mode_discord #Runs in Discord preset
    elif current_name == "X":
        import mode_customizable #Runs in Custom preset    
    else:
        print("Error : Unable to identify what script to run (Please make sure the end of the EXE file is a valid run code)")
        x = input("STOP")
except Exception as e: #If error, then it will display error message here
  print(e)
  x = input("STOP")