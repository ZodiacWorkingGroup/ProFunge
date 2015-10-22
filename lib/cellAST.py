class IFStatement:
    def __init__(self, condition, yescode, nocode):
        self.cond = condition
        self.yescode = yescode
        self.nocode = nocode

    def eval(self, tos):
        if tos == self.cond:
            return self.yescode
        else:
            return self.nocode