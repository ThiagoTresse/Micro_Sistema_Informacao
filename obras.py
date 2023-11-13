import pandas as pd
import numpy as np
import datetime

class Obras:
    def __init__(self, 
                id_obra:int,
                nome:str,
                Contratos:str,
                tipo:str
                valorContrato:float,
                estagio:str,
                vigencia:datetime.date,
                bairro:str,
                situacao:str,
                valorPago:float,
                valorEmpenhado:float,
                valorLiquidado:float,              
                ):
        self.id_obra = id_obra
        self.nome = nome
        self.Contratos = Contratos
        self.tipo = tipo
        self.valorContrato = valorContrato
        self.estagio = estagio
        self.vigencia = vigencia
        self.bairro = bairro
        self.situacao = situacao
        self.valorPago = valorPago
        self.valorEmpenhado = valorEmpenhado
        self.valorLiquidado = valorLiquidado






# Métodos GET
    def get_id_obra(self):
        return self.id_obra

    def get_nome(self):
        return self.nome

    def get_Contratos(self):
        return self.Contratos

    def get_tipo(self):
        return self.tipo

    def get_valorContrato(self):
        return self.valorContrato

    def get_estagio(self):
        return self.estagio

    def get_vigencia(self):
        return self.vigencia

    def get_bairro(self):
        return self.bairro

    def get_situacao(self):
        return self.situacao

    def get_valorPago(self):
        return self.valorPago

    def get_valorEmpenhado(self):
        return self.valorEmpenhado

    def get_valorLiquidado(self):
        return self.valorLiquidado

    # Métodos SET
    def set_id_obra(self, id_obra):
        self.id_obra = id_obra

    def set_nome(self, nome):
        self.nome = nome

    def set_Contratos(self, Contratos):
        self.Contratos = Contratos

    def set_tipo(self, tipo):
        self.tipo = tipo

    def set_valorContrato(self, valorContrato):
        self.valorContrato = valorContrato

    def set_estagio(self, estagio):
        self.estagio = estagio

    def set_vigencia(self, vigencia):
        self.vigencia = vigencia

    def set_bairro(self, bairro):
        self.bairro = bairro

    def set_situacao(self, situacao):
        self.situacao = situacao

    def set_valorPago(self, valorPago):
        self.valorPago = valorPago

    def set_valorEmpenhado(self, valorEmpenhado):
        self.valorEmpenhado = valorEmpenhado

    def set_valorLiquidado(self, valorLiquidado):
        self.valorLiquidado = valorLiquidado



