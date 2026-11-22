# Responsável: Caio Daniel
import pytest

from src.regras_localeats import quantidade_itens_valida


# TU01 - de 1 a 10 é válido (testando os limites também)
@pytest.mark.parametrize("quantidade", [1, 3, 10])
def test_quantidade_entre_um_e_dez_e_valida(quantidade):
    assert quantidade_itens_valida(quantidade) is True


# TU02 - 11 já passa do limite
def test_quantidade_acima_de_dez_e_invalida():
    assert quantidade_itens_valida(11) is False


# TU03 - pedido sem nenhum item
def test_quantidade_zero_e_invalida():
    assert quantidade_itens_valida(0) is False


# TU04 - número negativo tem que dar erro
def test_quantidade_negativa_gera_erro():
    with pytest.raises(ValueError):
        quantidade_itens_valida(-1)
