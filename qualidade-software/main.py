from validator import *

if __name__ == "__main__":
    cpf = input("Formato para inserir CPF - XXX.XXX.XXX-XX: ")
    cpf_validator = CPFValidator()
    if cpf_validator.validate(cpf):
        print("CPF é válido")
    else:
        print("CPF inválido")
