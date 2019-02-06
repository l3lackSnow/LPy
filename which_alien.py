#TroyMartian, who has at least 3 antenna and at most 4 eyes;
#VladSaturnian, who has at most 6 antenna and at least 2 eyes;
#GraemeMercurian, who has at most 2 antenna and at most 3 eyes.

antenna = int(input("How many antennas?"))
eyes = int(input("How many eyes?))

t = False
v = False
g = False

if antenna >= 3 and eyes <= 4:
    t = True
    print("TroyMartian")
if antenna <= 6 and eyes >= 2:
    v = True
    print("VladSaturnian")
if antenna <= 2 and eyes <= 3:
    g = True
    print("GraemeMercurian")

    
