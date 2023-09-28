from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from abstractChamado import AbstractChamado


class ControladorChamados(AbstractControladorChamados):
    def __init__(self) -> None:
        super().__init__()
        self.__chamados = []
        self.__tipos_chamados = []

    def total_chamados_por_tipo(self, tipo: TipoChamado) -> int:
        return len([chamado for chamado in self.__chamados if chamado.tipo == tipo])

    def inclui_chamado(
        self,
        data: Date,
        cliente: Cliente,
        tecnico: Tecnico,
        titulo: str,
        descricao: str,
        prioridade: int,
        tipo: TipoChamado
    ) -> Chamado:
        if not isinstance(cliente, Cliente):
            return
        if not isinstance(tecnico, Tecnico):
            return
        if not isinstance(tipo, TipoChamado):
            return
        if not isinstance(data, Date):
            return
        for chamado in self.__chamados:
            if chamado.cliente == cliente and
               chamado.tecnico == tecnico and
                   chamado.data == data and chamado.tipo == tipo:
                return
 
        chamado = Chamado(
            data,
            cliente,
            tecnico,
            titulo,
            descricao,
            prioridade,
            tipo
        )
        self.__chamados.append(chamado)
        return chamado

    def inclui_tipochamado(
        self,
        codigo: int,
        nome: str,
        descricao: str
    ) -> TipoChamado:
        for tipo_chamado in self.__tipos_chamados:
            if tipo_chamado.codigo == codigo:
                raise Exception("Tipo de chamado já cadastrado")
        tipo_chamado = TipoChamado(codigo, nome, descricao)
        self.__tipos_chamados.append(tipo_chamado)
        return tipo_chamado

    @ property
    def tipos_chamados(self):
        return self.__tipos_chamados
