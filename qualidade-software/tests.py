from main import CFPValidator


def test_valid_cpf():
    cpf_validator = CFPValidator()
    assert cpf_validator.validate("123.456.789-09")


def test_invalid_cpf_invalid_verifier_digit_1():
    cpf_validator = CFPValidator()
    assert not cpf_validator.validate("123.456.789-08")


def test_invalid_cpf_invalid_verifier_digit_2():
    cpf_validator = CFPValidator()
    assert not cpf_validator.validate("123.456.789-00")


def test_valid_cpf_with_whitespace():
    cpf_validator = CFPValidator()
    assert cpf_validator.validate(" 123.456.789-09 ")


def test_valid_cpf_only_digits():
    cpf_validator = CFPValidator()
    assert cpf_validator.validate("12345678909")


def test_invalid_cpf_with_letters():
    cpf_validator = CFPValidator()
    assert not cpf_validator.validate("A23.456.789-09")


def test_invalid_cpf_with_special_characters():
    cpf_validator = CFPValidator()
    assert not cpf_validator.validate("123.456.789-@#")


def test_invalid_cpf_all_equal():
    cpf_validator = CFPValidator()

    for n in range(0, 10):
        assert not cpf_validator.validate(str(n) * 11)
