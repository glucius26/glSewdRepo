# Check for ticket
# Check for school ID
# Check for guest list
# Check for suspension
# if suspension = no
#   if school ID = yes
#       if ticket = yes or guest list = yes
#           grant entry
#   else:
#       deny entry
#else:
#   deny entry

ticket = str(input("Do you have a ticket?(y/n)"))
iD = str(input("Do you have a school ID?(y/n)"))
guestList = str(input("Are you on the guest list?(y/n)"))
suspension = str(input("Do you have a suspension?(y/n)"))

if suspension == "n":
    if iD == "y":
        if ticket == "y" or guestList == "y":
            print("Entry granted!")
        else:
            print("Entry Denied")
    else:
        print("Entry Denied")
else:
    print("Entry Denied")
