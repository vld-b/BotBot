import webbrowser
import random
import time
import os

#Asking for the name
name = input("Hello, what's your name?\n")
print("Hello,", name)
feelings = input("How are you feeling?\n")
if "good" in feelings and "you" in feelings:
  print("I'm fine thanks")
elif feelings.lower() == ("good"):
  print("In case you want to know, I'm always fine!")
elif feelings.lower() == ("bad"):
  print("I hope this will change soon.")
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
while(True):
  befehle = input("Which one of the questions would you like to use?\nthese are my commands: !old, !name, !livingplace, !eyescolor, !haircolor, !IQ, !meme\n")
  if befehle.lower() == ("!meme"):
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

  elif befehle.lower() == ("!name"):
    if len(name) > 0:
      print("My name is BotBot and your name is ", name)
    else:
      print("My name is BotBot, unfortunately you haven't given any name\n")
    time.sleep(2)
  
  elif befehle.lower() == ("!livingplace"):
    livingplace = input("I live in your computer, where do you?\n(please only write the address)\n")
    if len(livingplace) > 0:
      print("ok, saved!\n")
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
    time.sleep(2)
  
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
    time.sleep(2)

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
    time.sleep(2)

  elif befehle.lower() == ("!old"):
    old = input("How old are you?\n")
    if old < ("12"):
      print("You should be happy because you're very young!")
    elif old >= ("13"):
      print("Hello teenager!")
    elif old >= ("18"):
      print("Now, the childhood is over, now, you have to give everything you can.")
    time.sleep(2)
  