def meu_decorator(funcao_original):
    def nova_funcao():
        print("Executando algo antes da função original")
        funcao_original()
        print("Executando algo depois")

    return nova_funcao


@meu_decorator
def diga_ola():
    print("Olá Catalisa!!")


diga_ola()
