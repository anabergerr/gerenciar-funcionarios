def logar_acao(func):
    def nova_funcao(funcionario):
        print(f"Registrando bonus para um novo funcionario: {funcionario.get_nome()}")
        return func(funcionario)

    return nova_funcao


@logar_acao
def mostrar_bonus(funcionario):
    print(f"{funcionario.get_nome()} tem um bonus de: {funcionario.calcular_bonus()}")
