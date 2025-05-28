# # # 💻 Code Challenge: Method Overriding
# # # ✅ Create these classes:

# # # Class: Employee
# # # Method: work() → Print "Employee works 9 to 5"

# # # Class: Manager (inherits from Employee)
# # # Override the work() method to print "Manager works flexible hours"

# # # Class: Intern (inherits from Employee)
# # # Override the work() method to print "Intern works part-time"


# # class Employee:
# #     def work(self):
# #         print("Employee works 9 to 5")

# # class Manager(Employee):
# #     def work(self):
# #         print("Manager works flexible hours")

# # class Intern(Employee):
# #     def work(self):
# #         print("Intern works part-time")


# # e = Employee()
# # m = Manager()
# # i = Intern()

# # e.work()
# # m.work()
# # i.work()



# # 💻 Code Challenge: Use super() in Overridden Method
# # ✅ Create the following classes:
# # Class: Device
# # Method: specs()
# # → Print: "Basic device specs"

# # Class: Smartphone (inherits from Device)
# # Override the specs() method

# # Inside it, first call the parent specs() using super()

# # Then print: "Has touchscreen, camera, and internet access"


# # d = Device()
# # s = Smartphone()

# # d.specs()
# # s.specs()


# class Device:
#     def specs(self):
#         print("basic device specs")

# class Smartphone(Device):
#     def specs(self):
#         super().specs()
    
        
    
#         print("Has touchscreen, camera, and internet access")

# d = Device()
# s = Smartphone()

# d.specs()
# s.specs()



# # hallenge: Multi-level Inheritance with Method Chaining
# # Create these classes:

# # Device

# # Method: specs() → prints "Basic device specs"

# # Smartphone (inherits from Device)

# # Override specs()

# # First calls parent specs()

# # Then prints "Has touchscreen, camera, and internet access"

# # GamingSmartphone (inherits from Smartphone)

# # Override specs()

# # First calls parent specs()

# # Then prints "Optimized for gaming performance and battery"



class Device:
    def specs(self):
        print("Basic device specs")

class Smartphone(Device):
    def specs(self):
        super().specs()
        print("Has touchscreen, camera, and internet access")

# GamingSmartphone (inherits from Smartphone)
class GaminigSmartphone(Smartphone):
    def specs(self):
        super().specs()
        print("Optimized for gaming performance and battery")



        c = GaminigSmartphone()
        c.specs()