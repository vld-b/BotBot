#Asking for the name
name = input("Hello, what's your name?\n")
print("Hello,", name)
feelings = input("How are you feeling?\n")
if feelings.lower() == ("good, how about you?"):
  print("I'm fine thanks!")
elif feelings.lower() == ("good"):
  print("In case you want to know, I'm always fine!")
elif feelings.lower() == ("good how about you?"):
  print("I'm fine thanks!")
elif feelings.lower() == ("bad"):
  print("I hope this will change soon.")
elif feelings.lower() == ("good, how about you"):
  print("I'm fine thanks!")
elif feelings.lower() == ("good how about you"):
  print("I'm fine thanks!")
elif feelings.lower() == ("good, how about you?"):
  print("I'm fine thanks!")
else:
  print("In case you want to know, I'm always fine!")
#Now you've shared how you feel with BotBot

hobby = input("What are your hobbys?\n")
if hobby == ("gaming"):
  print("Hey, mine too!!!!")
else:
  print("OK, Cool")
#Now you've told him you hobbys
print("") 

#Das sind die Fragen
for befehle in range(0,101):
  befehle = input("Which one of the questions would you like to use?\nthese are my commands: !old, !name, !livingplace, !eyescolor, !haircolor, !IQ\n")
  if befehle.lower() == ("!name"):
    if len(name) > 0:
      print("My name is BotBot and your name is ", name)
    else:
      print("My name is BotBot, unfortunately you haven't given any name\n")
  
  elif befehle.lower() == ("!livingplace"):
    livingplace = input("I live in your computer, where do you?\n(please only write the address)\n")
    if len(livingplace) > 0:
      print("ok, saved\n")
    else:
      print("You unfortunately haven't given a valid address\n")
  
  elif befehle.lower() == ("!eyescolor"):
    eyescolor = input("What's the color of your eyes?\n")
    if eyescolor.lower() == ("green"):
       print("OK, I like every color.\n")
    elif eyescolor.lower() == ("blue"):
      print("Nice, that's my favourite color. :)\n")
    elif eyescolor.lower() == ("brown"):
      print("brown is the most usual eye color.")
    else:
      print("This is not a valid eye color.")
  
  elif befehle.lower() == ("!haircolor"):
    haircolor = input("What's the color of your hair?\n")
    if haircolor.lower() == ("brown"):
      print("Cool :)")
    elif haircolor.lower() == ("blond"):
      print("Cool :)")
    elif haircolor.lower() == ("black"):
      print("Cool :)")
    else:
      print("Interesting haircolor :)")
  elif befehle.lower() == ("!IQ"):
    IQ = input("How much IQ do you think that you have?")
    if IQ.lower() < ("50"):
      print("You still have to learn!")
    elif IQ.lower() > ("50"):
      print("You know something!")
    elif IQ.lower() == ("100"):
      print("Congratulations, your IQ is the same as an average american!")
    elif IQ.lower() > ("100"):
      print("CONGRATULATIONS, your IQ is over the average in america!!!!!!!!!!")
  elif befehle.lower() == ("!old"):
    old = input("How old are you?\n")
    if old < ("12"):
      print("You should be happy because you're very young!")
    elif old >= ("13"):
      print("Hello teenager!")
    elif old >= ("18"):
      print("Now, the childhood is over, now, you have to give everything you can.")
  