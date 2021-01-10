from abc import ABCMeta,abstractmethod
class Player:
    def __init__(self,face=None,body=None,arm=None,leg=None):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return "%s,%s,%s,%s"%(self.face,self.body,self.arm,self.leg)

class PlayerBuider(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass
    def build_body(self):
        pass
    def build_arm(self):
        pass
    def build_leg(self):
        pass

class SexyGirlBuilder(PlayerBuider):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "beautiful face"

    def build_body(self):
        self.player.body = "slim"

    def build_arm(self):
        self.player.arm = "good arm"

    def build_leg(self):
        self.player.leg = "long leg"

class Monster(PlayerBuider):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "monsterface"

    def build_body(self):
        self.player.body = "monsterbody"

    def build_arm(self):
        self.player.arm = "monsterarm"

    def build_leg(self):
        self.player.leg = "monsterleg"

class PlayerDirector:
    def buid_player(self,builder):
        builder.build_face()
        builder.build_body()
        builder.build_arm()
        builder.build_leg()
        return builder.player

builder = SexyGirlBuilder()
director = PlayerDirector()
p = director.buid_player(builder)
print(p)
