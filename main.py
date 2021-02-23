name = input("Hallo, wie heißt du?\n")
print("Hallo,", name)
if name.lower() == ("felix m."):
  print ("Nein spaß, kein bock auf Dich")

gefuehl = input("Wie geht es dir?\n")
#Jetzt hast du dich BotBot vorgestellt
if gefuehl.lower() == ("gut, dir?"):
  print("Mir auch danke.")
elif gefuehl.lower() == ("gut"):
  print("Mir auch danke!")
elif gefuehl.lower() == ("gut dir?"):
  print("Mir auch danke!")
elif gefuehl.lower() == ("schlecht"):
  print("Ich hoffe es wird sich ändern")
elif gefuehl.lower() == ("gut, dir"):
  print("Mir auch danke.")
elif gefuehl.lower() == ("gut dir"):
  print("Mir auch danke!")
else:
  print("Falls es dich interessiert mir geht es immer gut.")
#Jetzt hast du deine gefühle mit BotBot geteilt

hobby = input("Was sind deine hobbys?\n")
if hobby == ("zocken"):
  print("Hey, meins auch!!!!")
else:
  print("OK, geil")
#Jetzt hast du ihn deine hobbys gesagt
print("") 

#Das sind die Fragen
for befehle in range(0,101):
  befehle = input("Welchen der Fragen würdest du gerne benutzen?\ndas sind meine Befehle: !alter, !name, !wohnort, !augenfarbe, !haarfarbe, !IQ\n")
  if befehle.lower() == ("!name"):
    if len(name) > 0:
      print("Mein name ist BotBot und dein Name ist", name)
    else:
      print("Mein name ist BotBot, leider hast Du keinen Namen angegeben\n")
  
  elif befehle.lower() == ("!wohnort"):
    wohnort = input("Ich wohne im Computer und Du?\n(schreibe bitte nur die Addresse)\n")
    if len(wohnort) > 0:
      print("ok, gespeichert\n")
    else:
      print("Du hast leider keine gültige Adresse angegeben\n")
  
  elif befehle.lower() == ("!augenfarbe"):
    augenfarbe = input("Was ist deine Augenfarbe?\n")
    if augenfarbe.lower() == ("grün"):
       print("OK, mir gefällt jede Farbe.\n")
    elif augenfarbe.lower() == ("blau"):
      print("Nice, das ist meine Lieblingsfarbe.:)\n")
    elif augenfarbe.lower() == ("braun"):
      print("Braun ist die gewöhnliste Augenfarbe.")
    else:
      print("Dies ist keine farbe.")
  
  elif befehle.lower() == ("!haarfarbe"):
    haarfarbe = input("Was ist deine Haarfarbe?\n")
    if haarfarbe.lower() == ("braun"):
      print("Geil :)")
    elif haarfarbe.lower() == ("blond"):
      print("Geil :)")
    elif haarfarbe.lower() == ("schwarz"):
      print("Geil :)")
    else:
      print("Interessante Haarfarbe :)")
  elif befehle.lower() == ("!IQ"):
    IQ = input("Wie viel IQ denkst du dass du hast?")
    if IQ.lower() < ("50"):
      print("Du musst noch viel lernen!")
    elif IQ.lower() > ("50"):
      print("Du weist schon ein bisschen!")
    elif IQ.lower() == ("100"):
      print("Glückwunsch, dein IQ level steht auf den Durchschnitt eines Deutschen!")
    elif IQ.lower() > ("100"):
      print("GLÜCKWUNSCH, dein IQ level ist über den Durchschnitt der Deutschen!!!!!!!!!!")
  elif befehle.lower() == ("!alter"):
    alter = input("Wie alt bist du?\n")
    if alter < ("12"):
      print("Du bist sehr jung und soltest dich freuen!")
    elif alter >= ("13"):
      print("Hallo Teenager!")
    elif alter >= ("18"):
      print("Jetzt ist die Kindheit ist um, jetzt muss man sich anstrengen.")
  