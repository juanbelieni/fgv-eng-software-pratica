# Atividades Práticas de Engenharia de Software

## Qualidade de Software

**Questão 1 (5 pontos)**: o grupo deve refatorar o código apresentado com foco na clareza e organização. O paradigma de OO deve ser utilizado, incluindo o Single-responsibility principle e o Open–closed principle.

**Questão 2 (5 pontos)**: elabore uma suíte de testes unitários com base nas técnicas apresentadas em aula e descritas no material enviado. Cobertura mínima de 90%.

Código original:

```python
import re

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
        print("CPF inválido")
```

## Como Executar:

Para executar o código usamos três comandos:

* `make run`: Executa o script main.py.
* `make test`: Roda os testes do arquivo test.py.
* `make coverage`: Exibe a cobertura de testes.
