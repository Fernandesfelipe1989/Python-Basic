class Televisao:
    def __init__(self):
        self.ligado = False
        self.canal = 5

    def power(self):
        self.ligado = not self.ligado

    def aumenta_canal(self):
        if self.ligado:
            self.canal += 1
            if self.canal > 100:
                self.canal =1

    def diminui_canal(self):
        if self.ligado:
            self.canal -= 1
            if self.canal < 1:
                self.canal = 100
if __name__ == '__main__':
    televisao = Televisao()
    print('Televisão está ligada: {}'.format(televisao.ligado))
    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligado))
    for i in range(101):
        televisao.diminui_canal()
        print('O canal da televisão é igual a: {}'.format(televisao.canal))

