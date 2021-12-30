import time
from enlighten._basecounter import *
from enlighten.manager import get_manager
import sys
from enlighten._counter import Counter as _Counter
import uitls.enlightenPlus.spinner_const as spinner_const


class Spinner():
    def __init__(self, name, spin=spinner_const.spinners["dots"]):
        super().__init__()
        self.spin = spin
        manager = get_manager(
            stream=sys.stdout, counter_class=self.__class__, set_scroll=False)
        manager.counters[self] = 1
        self.manager = manager
        self.enabled = True
        self.last_update = 0
        self.back = False
        self.min_delta = 0
        self.start = time.time()
        self.count = 0
        self.name = name
        if "background" in spin.keys():
            self.background = spin["background"]
        else:
            self.background = [" "]

    def update_pass(self, value):
        self.update()
        return value

    def update_scan(self, value):
        for i in value:
            self.update()
            yield i

    def update(self, done=False, force=False, **fields):
        currentTime = time.time()
        self.count = self.count + 1
        self.refresh(elapsed=currentTime - self.start)

    def refresh(self, flush=True, elapsed=None):
        if self.enabled:
            self.last_update = time.time()
            self.manager.write(output=self.format, flush=flush,
                               counter=self, elapsed=elapsed)

    def format(self, width=None, elapsed=None):
        width = width or self.manager.width
        if "frame" == self.spin["type"]:
            l =self.name + ": " + self.spin["frames"][self.count % len(self.spin["frames"])] 
            return l + " "*(width-len(l))
        elif "bouncing" == self.spin["type"]:
            text = self.spin["frames"][0]
            name = self.name + ":"
            text_len = (len(text) + len(name))
            count = (width-text_len)
            count_background = count // len(self.background[0])
            x = (self.count + 1) % (count)
            output = (self.background[0] * (count_background))
            first_piece = output[0:x]
            third_piece = output[len(name)+x:]
            return name + first_piece + text + third_piece
        elif "scrolling" == self.spin["type"]:
            text = self.spin["frames"][self.count%len(self.spin)]
            name = self.name + ":"
            text_len = (len(text) + len(name))
            count = (width-text_len)
            count_background = count // len(self.background[0])
            x = (self.count % (count))
            output = (self.background[0] * (count_background))
            first_piece = output[0:x]
            third_piece = output[len(name)+x:]
            output = name + first_piece + text + third_piece
            return output
        elif "sequntial" == self.spin["type"]:
            pass
        elif "alongside" == self.spin["type"]:
            pass
        elif "bar" == self.spin["type"]:
            pass
        else:
            pass

    @property
    def elapsed(self):
        """
        Get elapsed time is seconds (float)
        """
        return time.time() - self.start



