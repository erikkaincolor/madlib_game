#----------POST MVP-----
#maybe add typewriter effect if i have time

# Project FINAL:
# You will be asked to provide information about how you got into technology, what you do in tech and more.\n\nThe script then outputs an affirmative madlib and generates you an Octothorpian name for your entrance into our land!

#This is a bandersnatchy, terminal-based, pick your own path experience.

print ("Greetings starshine! Octothorpia Jupitorus welcomes you and others.\nCome on, come along.\n\nAs the director of this groove ship, you are under my command, so take a listen, so you too...can understand.")
  
print ("")

alias = str(input("What is your chosen name?: ").capitalize())

song = str(input("\nWhat is your song/your jam?: "))
song = song.title()

print (f"\nGreetings {alias}! Was your motivation to join tech external or intrinsic?")

import time 

external_tracks = ["", "", "", "(A) Creating generational wealth and/or financial freedom", "(B) A healthy travel addiction","(C) You want to be a role model/representation\n"]
intrinsic_tracks = ["", "", "", "(A) Your own personal agency/autonomy", "(B) You want to be a public servant / protect the vulnerable through tech", "(C) You belong on SharkTank or in an Incubator...you're an entrepreneur!\n"]

external_octo_dict ={"A":"Those in tech passing on generational wealth know it'll help remove many burdens and help its recipients worry less about financial constraints or how to make ends meet.", 
                      "B":"“Studies have shown that people who spend their money on experiences, such as travel tend to be happier in their life.” I think so too!",
                     "C":"You dont understand, you overstand that better representation of marginalized groups is crucial in coming up with the right solutions to challenges, creative thinking and overall customer success."}

intrinsic_octo_dict ={"A":"You understand a career in tech brings this. You are in control and you now have access to many more choices in life in general.",  
              "B":"You are mindful of and caring for the underprivileged in society,  you prioritize the growth and well-being of individuals and their communities, and display awareness, empathy and foresight.", 
                       
               "C":"Venturers are motivated by risk, change, and uncertainty. They thrive when the environment or the work is constantly changing. They tend to like challenges and jump at the opportunity to be the first to do something new."}

def proceed2checkpoint():
  """This function initiates the text based adventure"""
  # motivation = str(input("Motivation2: ").capitalize()) #i cant tell which one is best
  def get_attention():
    """print words"""
    print (f"Get to the checkpoint booth and declare this to the attendant to gain admission into Octothorpia Jupitorus: \n\n*To the tune of '{song}'*")
    print ("")
    print ("-------------------------------")
    print ("")
    print ("'ATTENTION! ATTENTION! ATTENTION!'") 
  while True:
    motivation = str(input("Motivation: ").capitalize()) #i cant tell which one is best
    if not (motivation == "External" or motivation == "Intrinsic"):
      while (motivation !="External" or motivation != "Intrinsic"):
          print ("\nThat is not an option.")
          new_motivation = str(input("Is it <intrinsic> or <external>?: ").capitalize())
          if (new_motivation == "External" or new_motivation == "Intrinsic"):
            break
          else:
            break

    if motivation == "External":
      print ("...ah so what's going on around you gets you going? Cool beans!")
        
      timer = 2
      timer = int(timer)
      while timer > 0:
        #for loop is only to present A-C on a timer
        for tracks in external_tracks:
          print (tracks)
          timer = timer -1
          time.sleep(1) #using the time library's "time" variable  timer = timer -1 
      
      # external_track = str(input("Enter which out the three here: ").capitalize())   
      while motivation == "External":  
        #user chose EXTERNAL
        external_track = str(input("Enter which out the three here: ").capitalize()) #can i have multiple locally?
        print ("")
        if (external_track == "A"):          
          print (f"Smart about your finances? I like you already.\n{external_octo_dict['A']}\n")
          break
        elif (external_track == "B"):
          print (f"This you?\n{external_octo_dict['B']}\n")
          break
        elif (external_track == "C"):
          print (f"The people's champ!\n{external_octo_dict['C']}\n")
          break
        else:
          print ("Aht. Aht. Try again.\n")
          continue
      print (get_attention())
      
        
    
    if motivation == "Intrinsic":
        #intrinsic--------------------------------
        print ("\n...ah so what's going on inside of you gets you going? Me too! Out of these three, which do you relate to the most:\n")
        timer = 2
        timer = int(timer)
        while timer > 0:
          #for loop is only to present A-C on a timer
          for tracks in intrinsic_tracks:
            print (tracks)
            timer = timer -1
            time.sleep(1) 
              
        #user chose INTRINSIC
        # intrinsic_track = str(input("Enter here: ").capitalize())
        while motivation == "Intrinsic":
          print ("")
          intrinsic_track = str(input("Enter here: ").capitalize())
          if (intrinsic_track == "A"):
            print (f"You know tech can position you closer to independence, freedom, and self-direction and overall being able to act in behalf of yourself!\n{intrinsic_octo_dict['A']}\n")
            break
          elif (intrinsic_track == "B"):
            print (f"The people's champ!\n.{intrinsic_octo_dict['B']}\n")
            break
          elif (intrinsic_track == "C"):
            print (f"'Entrepreneurship brings us hope.' -Daymond John\n{intrinsic_octo_dict['C']}\n")
            break
          else:
            print ("Aht. Aht. Try again.\n")
            continue
        print (get_attention())


      
    # if not (motivation == "External" or motivation == "Intrinsic"):
    #   while (motivation !="External" or motivation != "Intrinsic"):
    #     external_track = str(input("Please choose either <intrinsic> or <external>: ").capitalize())
    #     print ("")
    #     t = 1
    #     if t==1:
    #       print ("\nThat is not an option.")
    #       continue
        
    break
    
#-------------
  def print_random_name():
    """this function prints a random first and last name"""
    import random
    adjectives = ["Adroit","Arcadian","Cerulean","Uncalculable","Didactic","Effulgent","Equanimous","Fecund","Prolific","Heuristic","Limpid","Sagacious","Tenacious","Gritty","Spicy","Salty","Juicy","Toothsome","Agile","Ambitious"]
    nouns = ["Baby","Handler","Accountant","Techie","Steve Jobs of Your Family","Bank","ATM","Cash Cow","Lad","Chap","Bush","Goose","Potato", "Billy Goat", "Tree Hugger", "Pheonix", "Icarus", "Drake", "Beyonce", "Viola Davis"]
    
    
    if motivation == "External":
      print(f"\n'I, {random.choice(adjectives)} {random.choice(nouns)}, formerly known as, {alias}, ")
      print ("I am an externally motivated stalwart.")
      # print (print_random_name())
      print(" LET ME INNNNN!!!' ") 
      return 
  
    elif motivation == "Intrinsic":
      print(f"\n'I, {random.choice(adjectives)} {random.choice(nouns)}, formerly known as, {alias},")
      print ("I am innately motivated to do awesome things.")
      # print (print_random_name())
      print(f" LET ME INNNNN!!!' ") 
      return 
    else:
      pass
    

#-----------------------------------
  print_random_name()
  return
#--------------------------------
proceed2checkpoint()
#--------------------------------

