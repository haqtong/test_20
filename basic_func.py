# encoding=utf-8
import itertools

class afcFuc:
    def __init__(self):
        pass# 地铁清分

    def pairwise(self, iterable):
        a, b = itertools.tee(iterable)
        next(b, None)
        return zip(a, b)

    def hex_diy(self, x):
        hex_num = hex(x)
        if len(hex_num) == 5:
            list = [hex_num[:2], '0', hex_num[2:]]
            return ''.join(list)
        else:
            return hex_num

    def hex_reverse(self,x):
        return int(x,16)