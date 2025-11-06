nameCheck = False
roomLoop = True
inv = []
captchaOne = "n"

while nameCheck == False:
    name = input(str("A young child sits in their room. What is this kid's name?"))
    nameCheck2 = input(str(f"Their name is {name}, is that correct?(y/n)"))
    if nameCheck2 == "y":
        nameCheck = True

print(f"Your name is {name}, and as of today, you are 12 years old! You are currently awaiting a present from your friend. What do you do in the meantime?")
while roomLoop == True:
    one = input(str("(Type EX to examine room, C to look at your computer, or L to leave room)"))

#start examining room
    if one == "EX":
        print("Around your room are a bunch of  UNFUN HORROR GAME POSTERS. You love them so much. You absolutely adore horror games that aren't fun to play. None of that Oulast or Resident Evil shit, no. You love Garten of BanBan, and Five Nights at Freddy's. 1-4 and security breach, that is. That was before they invented gameplay.")
        cOT = input(str("Look in your chest of terrors?(y/n)"))
        if cOT == "n":
            continue
        elif cOT == "y" and captchaOne == "n":
            print("You look inside your chest of terrors. Inside are a bunch of bad horror gameplay relics. You see a weird greyscale oficially liscensed Bendy and the Ink Machine axe(your dad wouldn't let you get the tommy gun bluhh), you see a dark springtrap funkopop, and finally, you see a drone with a custom-made remote that has only one button, like on Garten of Banban.")
            captchaOne = input(str("Do you want to captchalogue these items?(y/n)"))
            if captchaOne == "y":
                inv.append("D. Springtap funko")
                inv.append("GOBB Drone")
                #print(f"DEBUG {inv}")
                sS = "BATIM Axe"
                #print(f"DEBUG {sS}")
                print("You grab the funko pop and the GOBB Drone and put them in your ARRAY MODUS. You use the array modus, because you aren't stupid. You also add your BATIM Axe to your STRIFE SPECIBUS.")
                continue
            elif captchaOne == "n":
                continue
        elif cOT == "y" and captchaOne == "y":
            print("You have already peeped the horrors.")
            continue
    elif one == "C":
        
