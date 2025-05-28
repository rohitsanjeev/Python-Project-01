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






