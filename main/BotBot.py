import webbrowser
import random
import time
import os
import socket
import pickle
import sys

#checking for directory
saves = r"save"
if not os.path.isfile("save"):
  try:
    os.makedirs(saves)
  except OSError:
    pass

#Asking for the name
if os.path.isfile("./save/username.dat"):
  name = pickle.load(open("./save/username.dat", "rb"))
  print("Hello,", name)
else:
  name = input("Hello, what's your name?\n")
  print("Hello, " + name + "!")
  pickle.dump(name, open("./save/username.dat", "wb"))

#Now you'll share how you feel with BotBot
if os.path.isfile("./save/userfeelings.dat"):
  print("")
else:
  feelings = input("How are you feeling?\n")
  if "good" in feelings and "you" in feelings:
    print("I'm fine thanks")
  elif feelings.lower() == ("good"):
    print("In case you want to know, I'm always fine!")
  elif feelings.lower() == ("bad"):
    print("I hope this will change soon.")
  else:
    print("In case you want to know, I'm always fine!")
  pickle.dump(feelings, open("./save/userfeelings.dat", "wb"))


#Now you'll tell him your hobbys
if os.path.isfile("./save/userhobby.dat"):
  print("")
else:
  hobby = input("What are your hobbys?\n")
  if hobby == ("gaming"):
    print("Hey, mine too!!!!")
  else:
    print("OK, Cool")
  pickle.dump(hobby, open("./save/userhobby.dat", "wb"))
print("") 

#Das sind die Fragen
while(True):
  befehle = input("Which one of the commands would you like to use?\nthese are my commands: old, name, livingplace, eyescolor, haircolor, IQ, meme, myip, reset, highlow\n")
  if befehle.lower() == ("meme"):
    randomMeme = random.randint(1, 25)
    if randomMeme == 1:
      webbrowser.open("100C vs 100F vs 100K with spongebob meme.png")
    elif randomMeme == 2:
      webbrowser.open("apple_everything.png")
    elif randomMeme == 3:
      webbrowser.open("AWDIE9580.mp4")
    elif randomMeme == 4:
      webbrowser.open("cant.png")
    elif randomMeme == 5:
      webbrowser.open("How_would_an alien_wear_a hat.png")
    elif randomMeme == 6:
      webbrowser.open("Human_dog.png")
    elif randomMeme == 7:
      webbrowser.open("Hydraulic_press_channel.png")
    elif randomMeme == 8:
      webbrowser.open("Hyper_Tube_bench.png")
    elif randomMeme == 9:
      webbrowser.open("It's_a_Phillips_head_screw_driver.png")
    elif randomMeme == 10:
      webbrowser.open("me_in_math_be_like.png")
    elif randomMeme == 11:
      webbrowser.open("Neurosurgeon_can.....png")
    elif randomMeme == 12:
      webbrowser.open("nice_phone_case.png")
    elif randomMeme == 13:
      webbrowser.open("riper.png")
    elif randomMeme == 14:
      webbrowser.open("say_no_to_yes_confusion.png")
    elif randomMeme == 15:
      webbrowser.open("scare.png")
    elif randomMeme == 16:
      webbrowser.open("oh_no.png")
    elif randomMeme == 17:
      webbrowser.open("shoulder.png")
    elif randomMeme == 18:
      webbrowser.open("Shrek_in_Minecraft.png")
    elif randomMeme == 19:
      webbrowser.open("that_kid_who_says_he's_not_rich.png")
    elif randomMeme == 20:
      webbrowser.open("trash_icon_evolution.png")
    elif randomMeme == 21:
      webbrowser.open("understandable,_have_a_great_day.jpg")
    elif randomMeme == 22:
      webbrowser.open("video0.mp4")
    elif randomMeme == 23:
      webbrowser.open("what_normal_market_offers_vs_black_market.png")
    elif randomMeme == 24:
      webbrowser.open("C:/Users/vladb/Dropbox/My PC (DESKTOP-Vlad)/Documents/memes/whyyyyyyyyyyyyyy.png")
    else:
      webbrowser.open("Shrek.txt")
    time.sleep(2)

  elif befehle.lower() == ("name"):
    if len(name) > 0:
      print("My name is BotBot and your name is ", name)
    else:
      print("My name is BotBot, unfortunately you haven't given any name\n")
    time.sleep(2)
  
  elif befehle.lower() == ("livingplace"):
    if os.path.isfile("./save/useraddress.dat"):
      livingplace = pickle.load(open("./save/useraddress.dat", "rb"))
      print("Your address is: " + livingplace)
    else:
      livingplace = input("I live in your computer, where do you?\n(please only write the address)\n")
      if len(livingplace) > 0:
        print("ok, saved!\n")
      else:
        print("You unfortunately haven't given a valid address\n")
      pickle.dump(livingplace, open("./save/useraddress.dat", "wb"))
  
  elif befehle.lower() == ("eyescolor"):
    if os.path.isfile("./save/usereye.dat"):
      eyescolor = pickle.load(open("./save/usereye.dat", "rb"))
      print("Your eyescolor is " + eyescolor)
    else:
      eyescolor = input("What's the color of your eyes?\n")
      if eyescolor.lower() == ("green"):
        print("OK, I like every color.\n")
      elif eyescolor.lower() == ("blue"):
        print("Nice, that's my favourite color. :)\n")
      elif eyescolor.lower() == ("brown"):
        print("brown is the most usual eye color.")
      else:
        print("This is not a valid eye color.")
      pickle.dump(eyescolor, open("./save/usereye.dat", "wb"))
    time.sleep(2)
  
  elif befehle.lower() == ("haircolor"):
    if os.path.isfile("./save/userhair.dat"):
      haircolor = pickle.load(open("./save/userhair.dat", "rb"))
      print("Your haircolor is " + haircolor)
    else:
      haircolor = input("What's the color of your hair?\n")
      if haircolor.lower() == ("brown"):
        print("Cool :)")
      elif haircolor.lower() == ("blond"):
        print("Cool :)")
      elif haircolor.lower() == ("black"):
        print("Cool :)")
      else:
        print("Interesting haircolor :)")
      pickle.dump(haircolor, open("./save/userhair.dat", "wb"))
    time.sleep(2)

  elif befehle.lower() == ("IQ"):
    IQ = input("How much IQ do you think that you have?")
    if IQ.lower() < ("50"):
      print("You still have to learn!")
    elif IQ.lower() > ("50"):
      print("You know something!")
    elif IQ.lower() == ("100"):
      print("Congratulations, your IQ is the same as an average american!")
    elif IQ.lower() > ("100"):
      print("CONGRATULATIONS, your IQ is over the average in america!!!!!!!!!!")
    time.sleep(2)

  elif befehle.lower() == ("old"):
    if os.path.isfile("./save/useryear.dat"):
      old = pickle.load(open("./save/useryear.dat", "rb"))
      print("You're " + old + "years old.")
    else:
      old = input("How old are you?\n")
      if old < ("12"):
        print("You should be happy because you're very young!")
      elif old >= ("13"):
        print("Hello teenager!")
      elif old >= ("18"):
        print("Now, the childhood is over, now, you have to give everything you can.")
      pickle.dump(old, open("./save/useryear.dat", "wb"))
    time.sleep(2)
  
  elif befehle.lower() == ("myip"):
    ipConfrim = input("Your IP address is a dangerous characteristic of your PC, which can lead to your PC being hacked. Do you want to continue? y/n ")
    if ipConfrim.lower() == ("y"):
      hostname = socket.gethostname()
      getIP = socket.gethostbyname(hostname)
      print("This is your local IP address: " + getIP)
    else:
      print("ok, no problem")
    time.sleep(2)

  elif befehle.lower() == ("reset"):
    resetConfirm = input("Are you sure you want to reset BotBot?\nThis will make him forget your name, how you feel and your hobby.\n After it has been reset, it will close. y/n   ") 
    if resetConfirm.lower() == ("y"):
      try:
        os.remove("./save/username.dat")
      except OSError:
        pass
      try:
        os.remove("./save/userfeelings.dat")
      except OSError:
        pass
      try:
        os.remove("./save/userhobby.dat")
      except OSError:
        pass
      try:
        os.remove("./save/useraddress.dat")
      except OSError:
        pass
      try:
        os.remove("./save/userhair.dat")
      except OSError:
        pass
      try:
        os.remove("./save/usereye.dat")
      except OSError:
        pass
      try:
        os.remove("./save/useryear.dat")
      except OSError:
        pass
      sys.exit()
    elif resetConfirm.lower() == ("n"):
      print("Ok, didn't reset BotBot")
    else:
      print("invalid answer")

  elif befehle.lower() == ("highlow"):
    print("This is a game of highlow, welcome!")
    diffi = 100
    diff = input("What difficulty do you wish to play on? very easy/easy/medium/hard/very hard\n")
    if ("very easy") in diff:
      ran_num = random.randint(0, 10)
      veh = "higher than 5"
      if ran_num > 5:
        veh = "higher than 5"
      elif ran_num < 5:
        veh = "lower than 5"
      ve = input("Pick a number between 0 and 10. Hint, the number is " + veh + "\n")
      if ve == str(ran_num):
        print("Correct! the random number was " + str(ran_num))
      elif ve != str(ran_num):
        print("Wrong. The random number was " + str(ran_num))  
    elif ("easy") in diff:
      ran_num = random.randint(0, 50)
      eh = "higher than 25"
      if ran_num > 25:
        eh = "higher than 25"
      elif ran_num < 25:
        eh = "lower than 25"
      e = input("Pick a number between 0 and 50. Hint, the number is " + e + "\n")
      if e == str(ran_num):
        print("Correct! the random number was " + str(ran_num))
      elif e != str(ran_num):
        print("Wrong. The random number was " + str(ran_num))
    elif ("medium") in diff:
      ran_num = random.randint(0, 100)
      mh = "higher than 50"
      if ran_num > 50:
        mh = "higher than 50"
      elif ran_num < 50:
        mh = "lower than 50"
      m = input("Pick a number between 0 and 100. Hint, the number is " + mh + "\n")
      if m == str(ran_num):
        print("Correct! the random number was " + str(ran_num))
      elif m != str(ran_num):
        print("Wrong. The random number was " + str(ran_num))
    elif diff == ("very hard"):
      ran_num = random.randint(0, 1000)
      vhh = "higher than 500"
      if ran_num > 500:
        vhh = "higher than 500"
      elif ran_num < 500:
        vhh = "lower than 500"
      vh = input("Pick a number between 0 and 1000. Hint, the number is " + vhh + "\n")
      if vh == str(ran_num):
        print("Correct! the random number was " + str(ran_num))
      elif vh != str(ran_num):
        print("Wrong. The random number was " + str(ran_num))
    elif ("hard") in diff:
      ran_num = random.randint(0, 500)
      hh = "higher than 250"
      if ran_num > 250:
          hh = "higher than 250"
      elif ran_num < 250:
          hh = "lower than 250"
      h = input("Pick a number between 0 and 500. Hint, the number is " + hh + "\n")
      if h == str(ran_num):
          print("Correct! the random number was " + str(ran_num))
      elif h != str(ran_num):
          print("Wrong. The random number was " + str(ran_num))
  else:
    print("invalid command")