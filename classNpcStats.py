class NpcStats:
    def __init__(self, pv, pv_max, po, dps, defense, exp, niveau):
        self.pv = pv
        self.pv_max = pv_max
        self.po = po
        self.dps = dps
        self.defense = defense
        self.exp = exp
        self.niveau = niveau

    def get_pv(self):
        return self.pv

    def setPv(self, valeur):
        self.pv = self.pv + valeur

    def get_pv_max(self):
        return self.pv_max

    def get_po(self):
        return self.po

    def get_dps(self):
        return self.dps

    def get_defense(self):
        return self.defense

    def get_exp(self):
        return self.exp

    def get_niveau(self):
        return self.niveau
