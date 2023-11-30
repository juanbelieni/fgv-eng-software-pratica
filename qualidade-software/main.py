import re
from abc import ABC, abstractmethod


class Validator(ABC):
    @abstractmethod
    def validate(self, value) -> bool: ...


class CPFValidator(Validator):
    def __standardize_cpf(self, cpf):
        return re.sub(r"[^0-9]", "", cpf)

    def __verify_if_all_equal(self, cpf: str):
        first_digit = cpf[0]
        return all(digit == first_digit for digit in cpf)

    def __sum_of_products(self, cpf: str, verifier_digit: int):
        sum_of_products, i = 0, 9 + verifier_digit

        for number in cpf[:8+verifier_digit]:
            sum_of_products += int(number) * i
            i -= 1

        return sum_of_products

    def __expected_digit(self, cpf: str, verifier_digit: int):
        mod = self.__sum_of_products(cpf, verifier_digit) % 11
        return 0 if mod < 2 else 11 - mod

    def validate(self, cpf: str):
        cpf = self.__standardize_cpf(cpf)

        if len(cpf) != 11:
            return False

        if self.__verify_if_all_equal(cpf):
            return False

        verifier_digit_1 = int(cpf[9])
        verifier_digit_2 = int(cpf[10])

        expected_1 = self.__expected_digit(cpf, 1)
        expected_2 = self.__expected_digit(cpf, 2)

        return expected_1 == verifier_digit_1 and expected_2 == verifier_digit_2


if __name__ == "__main__":
    cpf = input("Formato para inserir CPF - XXX.XXX.XXX-XX: ")
    cpf_validator = CPFValidator()
    print(cpf_validator.validate(cpf))
