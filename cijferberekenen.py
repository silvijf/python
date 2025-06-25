def berekenen():   
    aantalpunten = int(input("hoeveel punten heb je gehaald?	"))
    maxpunten = int(input("wat is het max aantal punten?	"))

    cijfer = aantalpunten/maxpunten*9+1

    if cijfer > 5.5:
        print (f"Je cijfer is: {cijfer}!")
        print ("Je hebt dus een voldoende!")
    else:
        print (f"Je cijfer is: {cijfer}...")
        print ("Dat is helaas een onvoldoende, dus je moet meer leren.")
    berekenen()
berekenen()