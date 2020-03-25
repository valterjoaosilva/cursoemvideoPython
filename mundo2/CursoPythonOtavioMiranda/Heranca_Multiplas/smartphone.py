from CursoPythonOtavioMiranda.Heranca_Multiplas.eletronico import Eletronico
from CursoPythonOtavioMiranda.Heranca_Multiplas.log import LogMixin


class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectar = False

    def conectar(self):
        if not self._ligado:
            info = f'{self._nome} Não está ligado'
            print(info)
            self.log_info(info)
            return

        if self._conectar:
            error = f"{self._nome} já está conectado "
            print(error)
            self.log_error(error)
            return

        self._conectar = True
        info = f'{self._nome} Foi Conectado com Sucesso'
        print(info)
        self.log_info(info)

    def desconectar(self):
        if not self._ligado:
            error = f'{self._nome} não está legado'
            print(error)
            self.log_error(error)
            return

        if not self._conectar:
            error = f'{self._nome} não está conectado'
            print(error)
            self.log_error(error)
            return

        self._conectar = False
        info = f'{self._nome} desconectado com sucesso'
        print(info)
        self.log_info(info)




