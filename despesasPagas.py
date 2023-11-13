import pandas as pd
import numpy as np
import datetime

class DespesasPagas:
    def __init__(self, 
                 numeroPagamento:int,
                 processoPagamento:int,
                 digitoPagamento:int,
                 idEmpenho:int,
                 numeroEmpenho:int,
                 numeroLiquidacao:int,
                 Exercicio:datetime,
                 data:datetime,
                 descricao:str,
                 licitacao:int,
                 unidadeGestora:str,
                 codUnidadeGestora:int,
                 valor:float, 
                 cpfCnpj:str,
                 nomeFornecedor:str,):
        self.numeroPagamento = numeroPagamento
        self.processoPagamento = processoPagamento
        self.digitoPagamento = digitoPagamento
        self.idEmpenho = idEmpenho
        self.numeroEmpenho = numeroEmpenho
        self.numeroLiquidacao = numeroLiquidacao
        self.Exercicio = Exercicio
        self.data = data
        self.descricao = descricao
        self.licitacao = licitacao
        self.unidadeGestora = unidadeGestora
        self.codUnidadeGestora = codUnidadeGestora
        self.valor = valor
        self.cpfCnpj = cpfCnpj
        self.nomeFornecedor = nomeFornecedor


# Métodos GET
    def get_numeroPagamento(self):
        return self.numeroPagamento

    def get_processoPagamento(self):
        return self.processoPagamento

    def get_digitoPagamento(self):
        return self.digitoPagamento

    def get_idEmpenho(self):
        return self.idEmpenho

    def get_numeroEmpenho(self):
        return self.numeroEmpenho

    def get_numeroLiquidacao(self):
        return self.numeroLiquidacao

    def get_Exercicio(self):
        return self.Exercicio

    def get_data(self):
        return self.data

    def get_descricao(self):
        return self.descricao

    def get_licitacao(self):
        return self.licitacao

    def get_unidadeGestora(self):
        return self.unidadeGestora

    def get_codUnidadeGestora(self):
        return self.codUnidadeGestora

    def get_valor(self):
        return self.valor

    def get_cpfCnpj(self):
        return self.cpfCnpj

    def get_nomeFornecedor(self):
        return self.nomeFornecedor

    # Métodos SET
    def set_numeroPagamento(self, numeroPagamento):
        self.numeroPagamento = numeroPagamento

    def set_processoPagamento(self, processoPagamento):
        self.processoPagamento = processoPagamento

    def set_digitoPagamento(self, digitoPagamento):
        self.digitoPagamento = digitoPagamento

    def set_idEmpenho(self, idEmpenho):
        self.idEmpenho = idEmpenho

    def set_numeroEmpenho(self, numeroEmpenho):
        self.numeroEmpenho = numeroEmpenho

    def set_numeroLiquidacao(self, numeroLiquidacao):
        self.numeroLiquidacao = numeroLiquidacao

    def set_Exercicio(self, Exercicio):
        self.Exercicio = Exercicio

    def set_data(self, data):
        self.data = data

    def set_descricao(self, descricao):
        self.descricao = descricao

    def set_licitacao(self, licitacao):
        self.licitacao = licitacao

    def set_unidadeGestora(self, unidadeGestora):
        self.unidadeGestora = unidadeGestora

    def set_codUnidadeGestora(self, codUnidadeGestora):
        self.codUnidadeGestora = codUnidadeGestora

    def set_valor(self, valor):
        self.valor = valor

    def set_cpfCnpj(self, cpfCnpj):
        self.cpfCnpj = cpfCnpj

    def set_nomeFornecedor(self, nomeFornecedor):
        self.nomeFornecedor = nomeFornecedor