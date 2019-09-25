#Define a class Person and its two child classes: Male and Female. All classes have a method "getGender"
# which can print "Male" for Male class and "Female" for Female class.

class person:
    def getGender(self):
        print("gender")

class male(person):
    def getGender(self):
        super().getGender()
        print("Male")

class female(person):
    def getGender(self):
        print("female")

object1=male()
object1.getGender()
object2=female()
object2.getGender()

