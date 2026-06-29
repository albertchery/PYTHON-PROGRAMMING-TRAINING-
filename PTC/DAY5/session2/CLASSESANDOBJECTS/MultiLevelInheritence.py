class GrandFather:
    def Skill(self):
        print("Reading current affairs")
class Father(GrandFather):
    def FatherSkill(self):
        print("Father makes money")
class Son(Father):
    def SonSkill(self):
        print("Watching reels\nSleeping")
# Instance of SON
son=Son()
son.SonSkill()
son.FatherSkill()
son.Skill()