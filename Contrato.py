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
    def insere_novo(self, novo_contrato):
        novo_contrato = { 
            numero_contrato = input(int("Informe o numero do contrato: ")),
            ano_contrato = input(int("Informe o ano do contrato: ")),
            tipo_contrato = int(input("informe o tipo de contrato: ")) ,
            processo = input(int("Informe o numero do proceso: ")) ,
            ano_processo = input(int("Informe o numero do processo: ")) ,
            valor_contratado = input(float("Informe o valor do contrato: ")) ,
            aditivo = input(int("Informe o valor da aditivo: ")) ,
            valor_total = input(float("Informe o valor total:")) ,
            cpfcnpj = input(int("Informe o CPF/CNPJ: ")) ,
            fornecedor = input(str("Informe o nome do fornecedor: ")),
            secretaria = input(str("Informe a secretaria: ")),
            fiscal = input(str("Informe o fiscal: ")) ,
            data_inicio = input(datetime("informe a data de inicio: ")) ,
            data_final = input(datetime("informe a data final: ")),
            data_publicacao = input(datetime("Informe a data de publicação: ")) ,
            data_assinatura = input(datetime("Informe a data de Assinatura do contrato: ")),
            situacao = input(str("Informe a Situação: ")),
            coronavirus = input(bool("Coronavirus ? (S/N): ")),
            objeto = input(str("Informe o obejto: "))
        }
        self.dados = self.dados.append(novo_contrato, ignore_index=True)
        self.dados.to_excel("Contratos-2023.xlsx", index=False)
    

    def excluir_contrato(self, numero_contrato, ano_contrato):
    #Exclui um contrato da planilha a partir do numero e ano do contrato
    mask = (self.dados['numero_contrato'] == numero_contrato) & (self.dados['ano_contrato'] == ano_contrato)
    self.dados = self.dados[~mask]
    self.dados.to_excel("Contratos-2023.xlsx", index=False)


    def consultar_contrato(self, numero_contrato, ano_contrato):
    #Retorna um DataFrame com as informações do contrato a partir do numero e ano do contrato
    mask = (self.dados['numero_contrato'] == numero_contrato) & (self.dados['ano_contrato'] == ano_contrato)
    return self.dados[mask]

    #Retorna um DataFrame com as informações de todos os contratos
    def listar_contratos(self):
        return self.dados


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
    