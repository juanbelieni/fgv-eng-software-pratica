import re

class CFPValidator:
    def __init__(self, cpf):
        self.cpf = self._standardize_cpf(cpf)
    
    def _standardize_cpf(self, cpf):
        return re.sub(r"[^0-9]", "", cpf)
    
    def _sum_of_products(self, cpf, digit:int=1):
        sum_of_products, i = 0, 9 + digit
        for number in cpf[:8+digit]:
            sum_of_products += int(number) * i 
            i -= 1
            print(sum_of_products)
        return sum_of_products
    
    def _expected_digits(self, cpf, digit:int=1):
        mod = self._sum_of_products(cpf, digit) % 11
        print(mod)
        print(0 if mod < 2 else 11 - mod)
        return 0 if mod < 2 else 11 - mod
    
    def validator_digit(self):
        if self._expected_digits(self.cpf) == int(self.cpf[9]) and self._expected_digits(self.cpf, 2) == int(self.cpf[10]):
            return True
        else:
            return False
    
if __name__ == "__main__":
    cpf = input("Formato para inserir CPF - XXX.XXX.XXX-XX: ")
    cpf_validator = CFPValidator(cpf)
    print(cpf_validator.validator_digit())


"""import re

cpf_fornecido = input("Formato para inserir CPF - XXX.XXX.XXX-XX: ")
cpf_tratado = re.sub(r"[^0-9]", "", cpf_fornecido)

if cpf_tratado == cpf_tratado[0] * len(cpf_tratado):
    print("CPF inválido")
else:
    cpf_sem_digitos_verificadores = cpf_tratado[:9]
    nr_digitos = 10
   
    digito_calculado = 0
   
    for cada_digito in cpf_sem_digitos_verificadores:
        digito_calculado += int(cada_digito) * nr_digitos
        nr_digitos -= 1
   
    digito_verificador_1 = (digito_calculado * 10) % 11
   
    if digito_verificador_1 <= 9:
        digito_verificador_1 = digito_verificador_1
    else:
        digito_verificador_1 = 0
   
    cpf_com_um_digito_verificador = cpf_sem_digitos_verificadores + str(digito_verificador_1)
    nr_digitos = 11
   
    digito_calculado = 0
   
    for cada_digito in cpf_com_um_digito_verificador:
        digito_calculado += int(cada_digito) * nr_digitos
        nr_digitos -= 1
   
    digito_verificador_2 = (digito_calculado * 10) % 11
   
    if digito_verificador_2 <= 9:
        digito_verificador_2 = digito_verificador_2
    else:
        digito_verificador_2 = 0
   
    if (int(cpf_tratado[9]) == digito_verificador_1) and (int(cpf_tratado[10]) == digito_verificador_2):
        print("CPF é válido")
    else:
        print("CPF inválido")"""
