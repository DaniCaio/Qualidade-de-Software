# Responsável: Caio Daniel
import re

import pytest
from playwright.sync_api import Page, expect

URL_LOCALEATS = "https://local-eats-unisenac.vercel.app/"

# conta só para teste, com dados inventados
NOME_TESTE = "Caio Teste"
EMAIL_TESTE = "caio.teste.qualidade@example.com"
SENHA_TESTE = "teste123"


@pytest.fixture
def conta_de_teste(page: Page):
    # cria a conta pela API antes do teste
    # se ela já existir, o cadastro é recusado e o teste segue normal
    page.request.post(
        URL_LOCALEATS + "users/register",
        data={"name": NOME_TESTE, "email": EMAIL_TESTE, "password": SENHA_TESTE},
    )


# TF01 - login e lista de restaurantes
def test_usuario_entra_e_ve_restaurantes(page: Page, conta_de_teste):
    page.goto(URL_LOCALEATS)

    # sem login o site manda para a tela de login
    expect(page).to_have_url(re.compile(r"login\.html"))

    page.locator("#loginEmail").fill(EMAIL_TESTE)
    page.locator("#loginPassword").fill(SENHA_TESTE)
    # tem dois "Entrar" na tela (a aba e o botão), então uso o do formulário
    page.locator("#loginForm").get_by_role("button", name="Entrar").click()

    expect(page).to_have_url(re.compile(r"index\.html"))
    expect(page.get_by_text("Olá, Caio")).to_be_visible()
    # o nome do restaurante fica junto com outras infos no card, por isso busco pelo link
    expect(page.get_by_role("link", name="Restaurante Sabor 0")).to_be_visible()
