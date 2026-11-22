# Atividade 4: Testes Automatizados do LocalEats

## 1. Identificação

- **Modalidade:** individual
- **Repositório:** <https://github.com/DaniCaio/Qualidade-de-Software>
- **Diretório da atividade:** <https://github.com/DaniCaio/Qualidade-de-Software/tree/main/atividades/atividade-04>
- **Data da última execução:** 17/11/2026

### Integrantes

1. Caio Daniel

---

## 2. Integrantes e responsabilidades

| ID | Integrante responsável | Tipo | Comportamento verificado | Arquivo e função de teste |
|---|---|---|---|---|
| TU01 | Caio Daniel | Unitário | Quantidade de 1 a 10 é válida (testa 1, 3 e 10) | `tests/test_regras_localeats.py::test_quantidade_entre_um_e_dez_e_valida` |
| TU02 | Caio Daniel | Unitário | Quantidade acima de 10 é inválida | `tests/test_regras_localeats.py::test_quantidade_acima_de_dez_e_invalida` |
| TU03 | Caio Daniel | Unitário | Quantidade zero é inválida | `tests/test_regras_localeats.py::test_quantidade_zero_e_invalida` |
| TU04 | Caio Daniel | Unitário | Quantidade negativa gera ValueError | `tests/test_regras_localeats.py::test_quantidade_negativa_gera_erro` |
| TF01 | Caio Daniel | Funcional | Entrar no sistema e ver a lista de restaurantes | `tests/test_localeats.py::test_usuario_entra_e_ve_restaurantes` |

---

## 3. Testes unitários

### Regra de Caio Daniel

- **Regra escolhida:** Regra 3, quantidade de itens
- **Função implementada:** `quantidade_itens_valida(quantidade)`
- **Arquivo da implementação:** `src/regras_localeats.py`
- **Testes criados:** `test_quantidade_entre_um_e_dez_e_valida`, `test_quantidade_acima_de_dez_e_invalida`, `test_quantidade_zero_e_invalida` e `test_quantidade_negativa_gera_erro`
- **Comportamentos verificados:** de 1 a 10 retorna True (inclusive 1 e 10), 0 e 11 retornam False e número negativo dá ValueError.

Escolhi essa regra porque é a mesma que usei no valor limite da Atividade 3 (0, 1, 10 e 11). Assim os testes unitários conferem na função os mesmos limites que eu planejei testar pela tela.

---

## 4. Aplicação do TDD

### TDD de Caio Daniel

- **Regra escolhida:** Regra 3, quantidade de itens
- **Primeiro teste escrito:** `test_quantidade_entre_um_e_dez_e_valida`, conferindo que 3 retorna True.
- **Por que o teste falhou inicialmente:** a função ainda não existia, então o pytest deu erro na importação.
- **Implementação mínima realizada:** criei a função retornando sempre `True`, só para esse teste passar.
- **Segundo teste escrito:** `test_quantidade_acima_de_dez_e_invalida`, conferindo que 11 retorna False. Ele falhou porque a função sempre retornava True, aí troquei o retorno por `1 <= quantidade <= 10`.
- **Melhoria ou refatoração realizada:** passei os limites para constantes (`QUANTIDADE_MINIMA` e `QUANTIDADE_MAXIMA`), coloquei o `ValueError` para número negativo e criei mais dois testes, um para o zero e outro para o negativo. Também mudei o primeiro teste para usar `pytest.mark.parametrize` com 1, 3 e 10, para pegar os dois limites.

---

## 5. Testes funcionais com Playwright

**Sistema:** https://local-eats-unisenac.vercel.app/

### Teste funcional de Caio Daniel

- **ID:** `TF01`
- **Fluxo automatizado:** fazer login com uma conta de teste e chegar na página inicial com a lista de restaurantes.
- **Preparação:** antes do teste, a conta de teste (dados inventados) é criada pela API de cadastro. Se ela já existir, o cadastro é recusado e o teste segue.
- **Interação realizada:** preencher e-mail e senha na tela de login e clicar em Entrar.
- **Primeira assertion:** sem login, ao abrir o site ele vai para a tela de login (`login.html`).
- **Segunda assertion:** depois do login abre a página inicial (`index.html`) com "Olá, Caio" no topo.
- **Terceira assertion:** o card do "Restaurante Sabor 0" aparece na lista.
- **Arquivo e função:** `tests/test_localeats.py::test_usuario_entra_e_ve_restaurantes`
- **Resultado final:** aprovado. Na primeira vez falhou na terceira assertion por causa do locator do card, mas depois da correção passou (ver seção 9).

---

## 6. Resultado da execução

Comando usado no PowerShell, dentro da pasta `atividades/atividade-04`:

```powershell
python -m pytest -v | Tee-Object -FilePath relatorio-pytest.txt
```

- **Quantidade total de testes:** 7
- **Testes aprovados:** 7
- **Testes reprovados:** 0
- **Link para o relatório:** [relatorio-pytest.txt](relatorio-pytest.txt)
- **Observações:** todos os testes passaram, em uns 4 segundos. O aviso `PytestRemovedIn10Warning` que aparece no relatório vem de um plugin que é instalado junto com o pytest-playwright, não do meu código, e não muda o resultado.

São 7 porque o TU01 roda 3 vezes (1, 3 e 10), mais o TU02, TU03, TU04 e TF01.

---

## 7. Explicações individuais

### Explicação do teste de Caio Daniel

- **Teste escolhido:** `test_quantidade_acima_de_dez_e_invalida`
- **Comportamento verificado:** pela regra, o pedido pode ter no máximo 10 itens. O teste confere o primeiro valor que passa disso.
- **Dados ou estado inicial:** a quantidade 11. Não precisa preparar nada, a função só recebe um número.
- **Resultado esperado:** a função retorna `False`.
- **O que faria o teste falhar:** se a comparação estivesse errada (por exemplo `<= 11`) ou se alguém tirasse o limite máximo. Também falharia se a função continuasse retornando sempre `True`, como na implementação mínima do TDD.

---

## 8. Uso de inteligência artificial

- **Ferramenta utilizada:** Claude (Anthropic)
- **Como a ferramenta foi utilizada:** para montar a estrutura da atividade, escrever a função e os testes seguindo o TDD e escolher os locators do Playwright.
- **Uma sugestão que precisou ser alterada ou rejeitada:** para o card do restaurante, a sugestão foi usar `get_by_text("Restaurante Sabor 0", exact=True)`. Na primeira execução o TF01 falhou nessa linha, porque o nome não fica sozinho num elemento, ele fica junto com preço, tipo e bairro no card. Troquei por `get_by_role("link", name="Restaurante Sabor 0")`. Também não usei só o nome "Entrar" para clicar no login, porque a tela tem dois elementos com esse texto (a aba e o botão), então usei o botão de dentro do `#loginForm`.
- **Motivo da alteração ou rejeição:** o locator sugerido não achava o elemento e o teste falhava sem o sistema ter defeito.
- **Como o código sugerido foi verificado:** rodei os testes no PowerShell, olhei a mensagem de erro do Playwright na primeira execução (ela mostra os elementos da página), corrigi o locator e rodei de novo. Depois conferi se os 7 testes aparecem no relatório e se os nomes da tabela batem com os dos arquivos.

---

## 9. Diferenciais opcionais

- [x] Terceiro teste unitário para caso de borda: `test_quantidade_zero_e_invalida` em [tests/test_regras_localeats.py](tests/test_regras_localeats.py).
- [x] Uso de `pytest.raises` para verificar exceção: `test_quantidade_negativa_gera_erro`.
- [x] Parametrização com `pytest.mark.parametrize`: `test_quantidade_entre_um_e_dez_e_valida` (1, 3 e 10).
- [x] Registro de uma falha encontrada e corrigida: na primeira execução o TF01 falhou na verificação do card "Restaurante Sabor 0" (`element(s) not found`). O login funcionou, mas o locator por texto exato não achava o nome, que fica junto com outras informações no card. Corrigi usando o link do card e o teste passou na execução seguinte.
