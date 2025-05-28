class Player:
    def __init__(self,name):
        self.name = name
        

class ipl_team(Player):
        def __init__(self,name,team):
            super().__init__(name) #call parent constructor
            self.team = team

        def plays_for(self):
            print(self.name, "plays for" ,self.team)


p1 = ipl_team("virat","RCB")
p1.plays_for()



# class a:
#      def greet(self):
#           print("hello for a")
# class b(a):
#      pass
# obj = b()
# obj.greet()


# class Parent:
#     def __init__(self):
#         print("Parent Constructor")

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("Child Constructor")

# c = Child()


class Person:
     def __init__(self,name):
          self.name = name
     def introduce(self):
          print("Hi, I am",self.name)


class Player(Person):
     def __init__(self,name,sport):
          super().__init__(name)
          self.sport = sport
     def plays(self):
          print(f"{self.name} plays {self.sport}")

class Cricketer(Player):
     def __init__(self,name,sport,team):
          
          super().__init__(name,sport)
          self.team = team
     def info(self):
          print(f"{self.name} plays {self.sport} for {self.team}")

dhoni = Cricketer("dhoni","Cricket","India")

dhoni.introduce()
dhoni.plays()
dhoni.info()



# 💻 CODE CHALLENGE: Multiple Inheritance
# ✅ Your Task:
# Create these classes:

# Class: Person

# Attribute: name

# Method: introduce() → print "Hi, I am {name}"

# Class: Trainer

# Attribute: experience (years of experience)

# Method: show_experience() → print "{name} has {experience} years of experience"

# Class: CricketCoach (inherits from both Person and Trainer)

# Add a method coach_team(team) → print "{name} coaches {team} team"

class Person:
    def __init__(self,name):
        self.name = name
    def introduce(self):
        print(f"Hi, I am {self.name}")

class Trainer:
    def __init__(self,experience):
        self.experience = experience
    def show_experience(self):
        print(f"{self.name} has {self.experience} years of experience")   
        

class CricketCoach(Person,Trainer):
    def __init__(self, name, experience):
        Person.__init__(self,name)
        Trainer.__init__(self,experience)
        
    def coach_team(self,team):
        print(f"{self.name} coaches {team} team")
        

coach = CricketCoach("Ravi Shastri", 20)
coach.introduce()
coach.show_experience()
coach.coach_team("India")




