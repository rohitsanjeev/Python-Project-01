class players:
    nationality = "indian" #CLASS VARIABLE

    def __init__(self,name,profile,ipl):
        self.name = name #INSTANCE VARIABLE
        self.profile = profile #INSTANCE VARIABLE
        self.ipl = ipl #INSTANCE VARIABLE

    def plays_for(self): #INSTANCE METHOD
        print(self.name, "plays for", self.ipl)
p1 = players("Virat Kohli","aata radhu","rcb")
p2 = players("rohit sharma","batsman","mi")


print(p1.name,p1.profile) #op for INSTANCE VARIABLE

p1.plays_for() #INSTANCE METHOD
# print(p1.nationality)
# print(p2.nationality) #OP FOR CLASS VARIBLE

players.nationality = "bharat" #OP FOR CLASS VARIABLE
print(p1.nationality)

# SO BASICALLY INSTANCE VARIABLE : INDIVIDUAL VARIABLE/ SPECIFIC FOR A object
# INSTACE METHOD: USED TO OPERATE ON INSTANCE VARIABLES OF AN object
# CLASS METHOS: COMMON VARIABLE? APLLICABLE TO ALL INSTANCES OF THE class
