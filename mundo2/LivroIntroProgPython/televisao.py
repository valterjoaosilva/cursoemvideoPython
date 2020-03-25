class Televisao:
    def __init__(self, min, max, canal):

        self.min = min
        self.max = max
        self.ligado = False
        self.canal = canal


    def mudar_canal_abaixo(self):
        if self.canal -1 >= self.min:
            self.canal = self.canal -1
        else:
            self.canal = 99
            return
    def mudar_canal_acima(self):
        if self.canal +1 <= self.max:
            self.canal = self.canal +1

        else:
            self.canal = 1
            return


tv = Televisao(1, 99, 99)
tv.mudar_canal_acima()
print(tv.canal)

tv = Televisao(1, 99, 1)
tv.mudar_canal_abaixo()
print(tv.canal)