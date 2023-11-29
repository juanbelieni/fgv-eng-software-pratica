import re
from abc import ABC, abstractmethod


class Validator(ABC):
    @abstractmethod
    def validate(self, value) -> bool: ...


class CFPValidator(Validator):
    def __standardize_cpf(self, cpf):
        return re.sub(r"[^0-9]", "", cpf)

    def __sum_of_products(self, cpf, digit: int):
        sum_of_products, i = 0, 9 + digit

        for number in cpf[:8+digit]:
            sum_of_products += int(number) * i
            i -= 1

        return sum_of_products

    def __expected_digit(self, cpf: str, digit: int):
        mod = self.__sum_of_products(cpf, digit) % 11
        return 0 if mod < 2 else 11 - mod

    def validate(self, cpf: str):
        cpf = self.__standardize_cpf(cpf)

        digit_1 = int(cpf[9])
        digit_2 = int(cpf[10])

        expected_digit_1 = self.__expected_digit(cpf, 1)
        expected_digit_2 = self.__expected_digit(cpf, 2)

        return expected_digit_1 == digit_1 and expected_digit_2 == digit_2


if __name__ == "__main__":
    cpf = input("Formato para inserir CPF - XXX.XXX.XXX-XX: ")
    cpf_validator = CFPValidator()
    print(cpf_validator.validate(cpf))
