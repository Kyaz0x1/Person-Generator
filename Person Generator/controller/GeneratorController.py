from colorama import Fore, Back
from view.View import View
from web.WebService import WebService
from os import system

class GeneratorController:

    sexo = 'I'
    pontuacao = 'S'
    idade = 0
    cep_estado = None
    cep_cidade = None

    def __init__(self):
        self.get_options(self)
    
    @staticmethod
    def get_options(self):
        self.get_sex_option()
    
    def get_sex_option(self):
        View.show_menu(
            'Gerador de Pessoas - Escolha o Sexo', 
            H = 'Masculino', M = 'Feminino', I = 'Aleatório', S = 'Sair'
        )

        self.sexo = input('* Escolha uma opção: ').upper()

        if not self.sexo in ('H', 'M', 'I', 'S'):
            print(Fore.RED + 'A opção escolhida é inválida, tente novamente!')
            self.get_sex_option()
            return

        if self.sexo == 'S':
            print(Fore.RED + 'Encerrando aplicação...')
            return

        self.get_punctuation_option()
        
    def get_punctuation_option(self):
        View.show_menu(
            'Gerador de Pessoas - Gerar com pontuação?',
            S = 'Sim', N = 'Não'
        )

        self.pontuacao = input('* Escolha uma opção: ').upper()

        if not self.pontuacao in ('S', 'N'):
            print(Fore.RED + 'A opção escolhida é inválida, tente novamente!')
            self.get_punctuation_option()
            return

        self.gen_person()
        

    def gen_person(self):
        data = {
            "acao": "gerar_pessoa",
            "sexo": self.sexo,
            "pontuacao": self.pontuacao,
            "idade": self.idade,
            "cep_estado": self.cep_estado,
            "txt_qtde": 1,
            "cep_cidade": self.cep_cidade
        }

        person = WebService.gen_person(data)

        print(f"""
            {Fore.BLACK}
            {Back.CYAN} Gerador de Pessoas - Informações {Back.RESET}

            {Fore.BLACK}
            {Back.CYAN} Dados Pessoais {Back.RESET}
            {Fore.GREEN}
            * Nome: {person.nome}
            * CPF: {person.cpf}
            * RG: {person.rg}
            * Data de Nascimento: {person.data_nasc}
            * Sexo: {person.sexo}
            * Signo: {person.signo}

            {Fore.BLACK}
            {Back.CYAN} Filiação {Back.RESET}
            {Fore.GREEN}
            * Mãe: {person.mae}
            * Pai: {person.pai}

            {Fore.BLACK}
            {Back.CYAN} Online {Back.RESET}
            {Fore.GREEN}
            * E-mail: {person.email}
            * Senha: {person.senha}

            {Fore.BLACK}
            {Back.CYAN} Endereço {Back.RESET}
            {Fore.GREEN}
            * CEP: {person.cep}
            * Endereço: {person.endereco}
            * Número: {person.numero}
            * Bairro: {person.bairro}
            * Cidade: {person.cidade}
            * Estado: {person.estado}

            {Fore.BLACK}
            {Back.CYAN} Telefones {Back.RESET}
            {Fore.GREEN}
            * Telefone: {person.telefone_fixo}
            * Celular: {person.celular}

            {Fore.BLACK}
            {Back.CYAN} Caracteristicas Físicas {Back.RESET}
            {Fore.GREEN}
            * Altura: {person.altura}
            * Peso: {person.peso}
            * Tipo Sanguineo: {person.tipo_sanguineo}

            {Fore.BLACK}
            {Back.CYAN} Outros {Back.RESET}
            {Fore.GREEN}
            * Cor favorita: {person.cor}
        """)

        system("pause")