from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Valter')


caneta = Caneta('neon')

maquina = MaquinaDeEscrever('Eletrica')


escritor.ferramenta = caneta
escritor.ferramenta.escrever()

escritor.ferramenta.apagar()

