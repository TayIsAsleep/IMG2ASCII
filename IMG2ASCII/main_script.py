def img_to_ascii(_IMG,_COLOR,loadingscreen_on,asciival_input,Scale_input):
    import os, os.path #os.system('color 7f') #BGR COLOR FOR CONSOLE
    import PIL
    import sys
    import subprocess
    import ctypes
    
    def loading(it, prefix="", size=60, file=sys.stdout):  #Loading Screen Module (Modded so that it can be "dissabled", as it seems to slow the proccess down a bit
        count = len(it) 
        def show(j):
            x = int(size*j/count)
            file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
            file.flush()         
        if loadingscreen_on: #If "loadingscreen_on" is true then it will run the script as normal, otherwise it will basicly bypass the loading bar scripts
            show(0)
            for i, item in enumerate(it):
                yield item
                show(i+1)
            file.write("\n")
            file.flush()
        else:
            for i, item in enumerate(it): 
                yield item
                
    def rgbme_new(rgbin): #Script to color text (New and simple)
        if _COLOR:
            return ("\033[38;2;{};{};{}m".format(rgbin[0],rgbin[1],rgbin[2]))
        else:
            return ""
    
    from PIL import Image #Import the image (either .jpg or .png)
    
    im = Image.open(str(_IMG),'r') #Opens the image provided by the function call
    width, height = im.size #Get height and width of image  
    
    image_scale = Scale_input #Sets image_scale to the inputted scale, so that it can be modified (?)
    _scale_x = 0 #Sets _scale_x and _scale_y to 0, before any special resolution can be entered.
    _scale_y = 0
    if image_scale == "discord": #If special mode is Discord then it presets the scale settings to the biggest you can send on discord
        _scale_x = 64*1
        _scale_y = 64*0.51
    else:     
        if image_scale == "": #Checks if no scale was entered, and if true, it will set it to the default size (100 height)
            image_scale = (100/width)*100
        else:
            image_scale = int(image_scale)  #If a custom size WAS entered, it will use that instead
    if _scale_x == 0 and _scale_y == 0: #If no custom resolution was entered, it will now do the math for _scale_x and _scale_y, based on the height and width, and it scales it to 10/4 (because characters arent square)
        _scale_x = int(width*1*(image_scale/100))
        _scale_y = int(height*0.51*(image_scale/100))   
 
    print("Scaling image...")
    scaled_im = im.resize((int(_scale_x),int(_scale_y))) #Scales the image to the new resolution 

    print("Getting RGB data") #Gets the RGB data and sets the height and width values
    pixel_values = list(scaled_im.getdata()) #Sets the list "pixel_values" into the rgb values from the image
    width, height = scaled_im.size #Get height and width of image 

    print("Converting RGB into B&W...") #Converts RGB values into B%W values
    new_values = []
    for i in pixel_values:
        new_values.append(int(((i[0])+(i[1])+(i[2]))/3))    



    output_list = []
    for i in loading(new_values, "Choosing characters based on B&W info: ", 40):
        _c = False
        _a = 1
        while _c != True:
            if (255/len(asciival_input))*_a >= i:
                output_list.append(asciival_input[_a-1])
                _c = True
            else:
                _a += 1

    _count = 0 #Puts every line in in a list, and then puts these lists in "final_list". 
    final_list = []
    for i in loading(range(height), "Preparing Data: ", 40):
        templist = []
        for x in range(width):
            templist.append(output_list[_count])
            _count += 1
        final_list.append(templist)
    
    ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 9 ) #Makes sure the terminal is on top
    print("Setting console size...") #Sets the Output Size
    os.system('mode con: cols={} lines={}'.format(width,height + 1))
    subprocess.call('', shell=True) #Apperantly sometimes the color stuff doesnt work unless this is run, so this is a failsafe
    
    print("Starting to render...") #Render the image line by line, also adding color with the rgbme() function.
    _count = 0
    for i in range(len(final_list)):
        newline = ""
        for x in final_list[i]:
            newline = newline + str(rgbme_new(pixel_values[_count])) + x
            _count += 1
        print(newline)
    
    next_image = str(input("")) #Accepts input of a new image. If you input a new image and hit enter, the script will run again with the new image, but with the same settings.
    if next_image[0] == '"': #Checks if the new image has " around it (it sometimes have and sometimes dont)
        next_image = next_image[1:-1] #Removes the quotemarks
    img_to_ascii(next_image,_COLOR,loadingscreen_on,asciival_input,Scale_input) #Runs the script again.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    try:
        import sys #from img_to_ascii import img_to_ascii #Imports the main script (Only needed if this isnt the main script)
        img_to_ascii(sys.argv[1],True,False,[" ",".",")","#","@"],(input("Image Scale (%): "))) #[image,color(True/False),Just_Color_mode(True/False),Loading Sreen(True/False),[Ascii characters to use (in a list)],scale input(%)]
    except Exception as e: #If error, then it will display error message here
        print(e)
        x = input("")
else:
    print ("Main Script Imported")