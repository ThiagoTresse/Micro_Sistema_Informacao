import datetime
import pandas as pd

class Contrato:
    def __init__(self,
                numero_contrato: int,
                ano_contrato: int,
                tipo_contrato: str,
                processo: int,
                ano_processo: int,
                valor_contratado:float,
                aditivo:int,
                valor_total:float,
                cpfcnpj:int,
                fornecedor:str,
                secretaria:str,
                fiscal: str,
                data_inicio: datetime.date,
                data_final: datetime.date,
                data_publicacao: datetime.date,
                data_assinatura: datetime.date,
                situacao: str,
                coronavirus: bool,
                objeto: str ):      
        self.numero_contrato = numero_contrato
        self.ano_contrato = ano_contrato
        self.tipo_contrato = tipo_contrato
        self.processo = processo
        self.ano_processo = ano_processo
        self.valor_contratado = valor_contratado
        self.aditivo = aditivo
        self.valor_total = valor_total
        self.cpfcnpj = cpfcnpj
        self.fornecedor = fornecedor
        self.secretaria = secretaria
        self.fiscal = fiscal
        self.data_inicio = data_inicio
        self.data_final = data_final
        self.data_publicacao = data_publicacao
        self.data_assinatura = data_assinatura
        self.situacao = situacao
        self.coronavirus = coronavirus
        self.objeto = objeto
        self.dados = pd.read_excel("Contratos-2023.xlsx")
                

    #Método construtor de Contratos
    def insere_novo(self, Contrato):
        novo_contrato = {
            numero_contrato": Contrato.numero_contrato,
            ano_contrato": Contrato.ano_contrato,
            tipo_contrato": Contrato.tipo_contrato,
            processo": Contrato.processo,
            ano_processo": Contrato.ano_processo,
            valor_contratado": Contrato.valor_contratado,
            aditivo": Contrato.aditivo,
            valor_total": Contrato.valor_total,
            cpfcnpj": Contrato.cpfcnpj,
            fornecedor": Contrato.fornecedor,
            secretaria": Contrato.secretaria,
            fiscal": Contrato.fiscal,
            data_inicio": Contrato.data_inicio,
            data_final": Contrato.data_final,
            data_publicacao": Contrato.data_publicacao,
            data_assinatura": Contrato.data_assinatura,
            situacao": Contrato.situacao,
            coronavirus": Contrato.coronavirus,
            objeto = input(str("Informe o obejto: "))
        }
        self.dados = self.dados.append(novo_contrato, ignore_index=True)
        self.dados.to_excel("Contratos-2023.xlsx", index=False)
       

    


    def alterar_atributos(cls, objeto, **kwargs):
        for atributo, valor in kwargs.items():
          setattr(objeto, atributo, valor)





c = Contrato()

df = c.dados
df[df['NumeroContrato']==588]
df.dtypes

df[df['Fornecedor'].str.contains('LTDA', regex=True)]

df.to_excel("contratos2.xlsx")

c.dados=c.dados['NumeroContrato']==588


#Getters
    def get_numero_contrato(self):
        return self.numero_contrato

    def get_ano_contrato(self):
        return self.ano_contrato

    def get_tipo_contrato(self):
        return self.tipo_contrato

    def get_processo(self):
        return self.processo

    def get_ano_processo(self):
        return self.ano_processo

    def get_valor_contratado(self): 
        return self.valor_contratado

    def get_aditivo(self):
        return self.aditivo

    def get_valor_total(self):
        return self.valor_total

    def get_cpfcnpj(self):
        return self.cpfcnpj

    def get_fornecedor(self):
        return self.fornecedor

    def get_secretaria(self):
        return self.secretaria

    def get_fiscal(self):
        return self.fiscal

    def get_data_inicio(self):
        return self.data_inicio

    def get_data_final(self):
        return self.data_final

    def get_data_publicacao(self):
        return self.data_publicacao

    def get_data_assinatura(self):
        return self.data_assinatura

    def get_situacao(self):
        return self.situacao

    def get_coronavirus(self):
        return self.coronavirus

    def get_objeto(self):
        return self.objeto


#Setters

    def set_numero_contrato(self, numero_contrato):
        self.numero_contrato = numero_contrato

    def set_ano_contrato(self, ano_contrato):
        self.ano_contrato = ano_contrato

    def set_tipo_contrato(self, tipo_contrato):
        self.tipo_contrato = tipo_contrato

    def set_processo(self, processo):
        self.processo = processo

    def set_ano_processo(self, ano_processo):
        self.ano_processo = ano_processo

    def set_valor_contratado(self, valor_contratado):
        self.valor_contratado = valor_contratado

    def set_aditivo(self, aditivo):
        self.aditivo = aditivo

    def set_valor_total(self, valor_total):
        self.valor_total = valor_total

    def set_cpfcnpj(self, cpfcnpj):
        self.cpfcnpj = cpfcnpj

    def set_fornecedor(self, fornecedor):
        self.fornecedor = fornecedor

    def set_secretaria(self, secretaria):
        self.secretaria = secretaria

    def set_fiscal(self, fiscal):
        self.fiscal = fiscal

    def set_data_inicio(self, data_inicio):
        self.data_inicio = data_inicio

    def set_data_final(self, data_final):
        self.data_final = data_final

    def set_data_publicacao(self, data_publicacao):
        self.data_publicacao = data_publicacao

    def set_data_assinatura(self, data_assinatura):
        self.data_assinatura = data_assinatura

    def set_situacao(self, situacao):
        self.situacao = situacao

    def set_coronavirus(self, coronavirus):
        self.coronavirus = coronavirus

    def set_objeto(self, objeto):
        self.objeto = objeto
    