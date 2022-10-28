from operator import truediv

def test3():
    print("Bij deze test willen ze hoe zien hoe goed wij kunnen multitesten.")
    print("Daarbij geven ons meerder opdrachten om in een korte tijd af te maken.")
    print("Na dat alle testen klaar waren moesten we wachten voor de resultaten op de volgende ochtend.")

    print("A. Slaap tot de volgende ochtend")
    print("B. Slaap niet en maak je zorgen als je het gehaald hebt")
    print("C. Geef op en ga terug naar huis met lege zaken")
    answer = input("Typ hier:")
    if answer == "a":
        volgendeochtend()
    elif answer == "b":
        volgendeochtend()
    elif answer == "c":
        print("je bent dood")
    else:
        print("\nProbeer opniew kies A,B of C \n\n")

def test2():
    print("Bij test 2 moesten we een soort operatie doen met proef kikker daar kunnen ze bepalen hoe goed we zijn met bloed te zien en hoe snel we kunnen reageren op ons patent.")
    

    print("A. Doe de test niet en ga met lege zaken naar huis")
    print("B. Doe de test 3")
    answer = input("Typ hier: ")
    if answer == "a":
        print("je bent dood")
    elif answer == "b":
        test3()
    else:
        print("\nProbeer opniew kies A of B \n\n")

def test():
    print("Er waren 3 testen.")
    print("De eerste test was een toets over medicijnen hoe goed jouw intelligentie over elke soort planten je kan gebruiken voor medicijnen of hoe je een gebroken bot kan behandelen.")

    print("A. Doe de test niet en ga met lege zaken naar huis")
    print("B. Doe de test 2")
    answer = input("Typ hier: ")
    if answer == "a":
        print("je bent dood")
    elif answer == "b":
        test2()
    else:
        print("\nProbeer opniew kies A of B \n\n")

def dochterhulpje():
    print("Bij het inschrijf tent zat een aardige mevrouw die een warme glimlach had.")
    print("Ze gaf mij een formulier om te vullen daar in stonde persoonlijke vragen over hoe gezond je bent.")
    print("Na het in schrijven had ze iedereen omgeroepen bij elkaar om ons te infomeren over de test.")

    print("A. Doe de test niet en ga met lege zaken naar huis")
    print("B. Doe de test")
    answer = input("Typ hier: ")
    if answer == "a":
        print("je bent dood")
    elif answer == "b":
        test()
    else:
        print("\nProbeer opniew kies A of B \n\n")

def schoonmaker():
    print("Bij inschrijven van schoonmaker was er helemaal niemand daar alleen de persoon waar je moet inschrijven.")
    print("De persoon die daar zat was aan het slapen en leek dat hij niet daar wou zijn.")
    print("Toen ik had ingeschreven waren er geen test om te doen.")
    print("Ze zijden dat ik de volgende ochtend al mag beginnen. ")

    print("A. Wacht voor de volgende ochtend    ")
    print("B. Ga naar huis met lege zaken  ")
    answer = input("Typ hier: ")
    if answer == "a":
        volgendeochtend()
    elif answer == "b":
        print("je bent dood")
    else:
        print("\nProbeer opniew kies A of B \n\n")

def deBoss():
    print("Ik was opeens in het boos beland ik wist niet waar ik was enige ding wat ik wel wist niet waar ik was. ")

    print("A. Zoek je weg terug naar de kamp en red het net voor het resultaten")
    print("B. Raak verdwaald en ken je weg niet terug")
    answer = input("Typ hier: ")
    if answer == "a":
        volgendeochtend()
    elif answer == "b":
        print("je bent dood")
    else:
        print("\nProbeer opniew kies A of B \n\n")

def hetverliest():
    print("Ik ging schuilen voor het spel als een lafaard pas toen ik hoorde van de generaal dat het gevecht voorbij is ging ik weg van me verstop plek.")
    print("Na het gevecht zij de generaal dat we de resultaten volgende ochtend krijgen.")
    print("Toen iedereen de nieuws horde wouden veel feesten.")

    print("A. ga meteen naar bed om energie te hebben voor de volgende dag")
    print("B. ga vieren met je team dat jullie gewonnen met andere teams erbij")
    answer = input("Typ hier: ")
    if answer == "a":
        print("je bent dood")
    elif answer == "b":
        feest()
    else:
        print("\nProbeer opniew kies A of B \n\n")

def feest():
    print("De feest wat er gehouden werd was hee leuk en gezellig iedereen ging heel losse en droge de hele nacht door.")

    print("A. Wordt laat waker en hoor niet de generaal zegt")
    print("B. Wordt op tijd waker en weet wel wat de generaal zegt")
    print("C. Slaap niet en ga naar het boos")
    answer = input("Typ hier:")
    if answer == "a":
        volgendeochtend()
    elif answer == "b":
        volgendeochtend()
    elif answer == "c":
        deBoss()
    else:
        print("\nProbeer opniew kies A,B of C \n\n")

def Levenalssoldaat():  
    print("Leven als een soldaat is een leven trotst om jouw land te verdedigen maar op welke kosten zullen niet weten. ")
    print("Tenminste heb ik mijn familie geholpen met ons armoede.")
    print("Ik hoop dat oorlog snel stopt zo dat ik me droom kan laten uit om de hele wereld te rijzen maar tot die dag zal ik hier zijn om te vechten voor mij land.")

def vergadering():
    print("De generaal heeft ons allemaal bij elkaar geroepen omdat om ons te complementeren op ons succes van op de top 20 komen.")
    print("Ik hoop dat jullie mij trotst maken in de toekomst.")

    print("A. Leef je leven als een normale soldaat")
    print("B. Leef je leven als een hardwerkende soldaat")
    answer = input("Typ hier: ")
    if answer == "a":
        Levenalssoldaat()
    elif answer == "b":
        Levenalssoldaat()
    else:
        print("\nProbeer opniew kies A of B \n\n")

def volgendeochtend():
    print("De resultaten waren binnengekomen ze waren opgehangen bij grote boord in het midden van het kamp.")
    print("Ik rende zo snel mogelijk naar de boord om mijn naam te kunnen vinden en daar was het mijn naam in het top 20 lijst ik zat in plaats 13 wat ik totaal niet zag aankomen.")
    print("Na dat iedereen hun resultaten hebben gezien kwam de generaal om de top 20 mensen op te roepen.")

    print("A. Ga niet mee en hoor de generaal niet uit")
    print("B. Ga mee met de generaal")
    answer = input("Typ hier: ")
    if answer == "a":
        vergadering()
    elif answer == "b":
        vergadering()
    else:
        print("\nProbeer opniew kies A of B \n\n")

def teamvsteam():
    print("De test was heel al voorbij veel van het team hebben hun alles gegeven voor het maar trots kan ik zeggen mijn team het als nummer 1 heeft gehaald maar kun niet zonder mij hulp.")
    print("In de eerst paar min was onze leider uit spel omdat meteen ging rennen naar het andere team als dombo. ")
    print("Toen had ik en mijn team plan gemaakt om te winnen en plan werkte en nu is de test officieel voorbij we krijgen de volgende dag de resultaten te zien.")

    print("A. ga meteen naar bed om energie te hebben voor de volgende dag")
    print("B. ga vieren met je team dat jullie gewonnen met andere teams erbij")
    answer = input("Typ hier: ")
    if answer == "a":
        volgendeochtend()
    elif answer == "b":
        feest()
    else:
        print("\nProbeer opniew kies A of B \n\n")

def DeLeider():
    print("Ik heb mezelf er buiten gelaten omdat de groep waar ik inzat lekken de meeste mensen ni vriendelijke en als je één ding al miss doet lijkt het wel dat ze je willen vermoorden.")
    print("De persoon die in onze groep de leider is geworden was grooste en sterkste van ons allemaal.")
    print("De test was simpel werk met elkaar om het andere team te verslaan.")

    print("A. Help je team om te winnen")
    print("B. Verstopt totdat de test voorbij")
    answer = input("Typ hier: ")
    if answer == "a":
        teamvsteam()
    elif answer == "b":
        hetverliest()
    else:
        print("\nProbeer opniew kies A of B \n\n")

def Detest():
    print("De eerste test was een kracht test om te kijken hoe sterk je bent.")
    print("De tweede test was snelheid om te kijken hoe snel je kan reageren op soorten situaties en de alle laste test was om te kijken hoe goed je kan samen werken met elkaar.")
    print("We waren allemaal in groep van 5 gezet.")
    print("Toen we allemaal in onze groep werden verdeeld hadden we 5 min om een leader te kiezen.")

    print("A. Nomineer jezelf als leider")
    print("B. Werk samen met je team om een keuze te maken")
    print("C. Hou je erbuiten")
    answer = input("Typ hier:")
    if answer == "a":
        print("je bent dood")
    elif answer == "b":
        DeLeider()
    elif answer == "c":
        DeLeider()
    else:
        print("\nProbeer opniew kies A,B of C \n\n")

def soldaat():
    print("De generaal die bij het inschrijf tafel zat kwam echt voor als een strenge manier uit maar wanneer je met hem praat was hij heel kalm persoon.")
    print("Hij vertelde als ik erin wil zijn moet ik eerst test completen. ")

    print("A. Doe de test en word teen soldaat")
    print("B. Geef op en ga met lege zaken naar huis")
    answer = input("Typ hier: ")
    if answer == "a":
        Detest()
    elif answer == "b":
        print("je bent dood")
    else:
        print("\nProbeer opniew kies A of B \n\n")

def DereisnaardeoorlogkampvanNL():
    print("De reis hiernaartoe was heel zwaar en gevaarlijk de kans om zomaar gedood te worden.")
    print("De zweer was heel zwaar bij het kamp het zag er heel depressief uit je kan echt zien dat Mesen wel hebben mee gemaakt in deze strijd.")
    print("Maar is de focus op het aanmelden bij het lager. ")

    print("A. Schrijf je in als een soldaat")
    print("B. Schrijf je in als een dochter hulpje")
    print("C. Schrijf je in als een schoonmaker")
    answer = input("Typ hier:")
    if answer == "a":
        soldaat()
    elif answer == "b":
        dochterhulpje()
    elif answer == "c":
        schoonmaker()
    else:
        print("\nProbeer opniew kies A,B of C \n\n")

def Voorhetvertrek():
    print("Op de school waar ik op zit heb ik een vriend die werkt bij het lager dus misschien heb ik een kans om daar een goeie baan te vinden.")
    print("Het beste punt uit deze vriend hij kan regelen dat ik met de trein kan reizen met hem en hoef niks te betalen voor het de reden daarvoor is dat ze mensen nodig hebben bij de oorlog van Nederland tussen Duitsland.")

    print("A. Ga naar Nederlands waar de safe zone is")
    print("B. Ga naar Duitsland en wordt gepakt als een verrader ")
    print("C. Blijf in het dorp en blijf veilig van de oorlog ")
    answer = input("Typ hier:")
    if answer == "a":
        DereisnaardeoorlogkampvanNL()
    elif answer == "b":
        print("je bent dood")
    elif answer == "c":
        print("je bent dood")
    else:
        print("\nProbeer opniew kies A,B of C \n\n")

def Begin():

    print("Het verhaal gaat over een arm jongentje dat het hele wereld wou ontdekken maar dat was een droom die te ver weg was om te pakken omdat, zijn familie en het dorp waar hij in woont heel arm was.")
    print("Hij probeert altijd een baan te vinden om zijn familie te helpen met het eten op tafel te leggen.")
    print("Hij wil een manier zoeken om geld te verdienen dus hij ging naar ze vriend voor hulp.")

    print("A. Ga naar je vriend en zoek werk")
    print("B. Ga niet op zoek naar je vriend en blijf werkloos en dat je sterf heel langzaam ")
    answer = input("Typ hier: ")
    if answer == "a":
        Voorhetvertrek()
    elif answer == "b":
        print("je bent dood")
    else:
        print("\nProbeer opniew kies A of B \n\n")

Begin()