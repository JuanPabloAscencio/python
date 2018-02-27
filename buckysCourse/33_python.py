class Mario():

    def move(self):
        print('I am moving!')


class Shroom():

    def eat_shroom(self):
        print('Now I am big!')

#big mario is going to import
#the functions from mario and shroom
class BigMario(Mario, Shroom):
#pass just prevents exeptions
    pass

bm = BigMario()
bm.move()
bm.eat_shroom()
