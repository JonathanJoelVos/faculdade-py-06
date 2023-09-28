from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        super().__init__()
        self.__clientes = []
        self.__tecnicos = []

    @property
    def clientes(self) -> list:
        return self.__clientes

    @property
    def tecnicos(self) -> list:
        return self.__tecnicos

    def inclui_cliente(
        self,
        codigo: int,
        nome: str
    ) -> Cliente:
        for client in self.__clientes:
            if client.codigo == codigo:
                raise Exception("Cliente já cadastrado")
        cliente = Cliente(nome, codigo)
        self.__clientes.append(cliente)
        return cliente

    def inclui_tecnico(
        self,
        codigo: int,
        nome: str
    ) -> Tecnico:
        for tecnico in self.__tecnicos:
            if tecnico.codigo == codigo:
                raise Exception("Tecnico já cadastrado")
        tecnico = Tecnico(nome, codigo)
        self.__tecnicos.append(tecnico)
        return tecnico
