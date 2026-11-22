# Responsável: Caio Daniel

QUANTIDADE_MINIMA = 1
QUANTIDADE_MAXIMA = 10


def quantidade_itens_valida(quantidade):
    if quantidade < 0:
        raise ValueError("A quantidade de itens não pode ser negativa.")

    return QUANTIDADE_MINIMA <= quantidade <= QUANTIDADE_MAXIMA
