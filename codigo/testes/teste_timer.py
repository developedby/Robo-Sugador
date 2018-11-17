# teste pra ver como faz timer repetindo

from threading import Timer
from cv2 import waitKey

class meutimer:
    def __init__(self):
        self.timer = Timer(.01, self.handler)
        self.timer.start()

    def handler(self):
        print('tempo')
        self.timer.cancel()
        self.timer = Timer(.01, self.handler)
        self.timer.start()

mt = meutimer()

while(True):
    if waitKey(1) == 27:
        break
