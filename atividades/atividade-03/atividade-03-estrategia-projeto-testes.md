# Atividade 3: Estratégia e Projeto de Testes do LocalEats

## 1. Identificação

**Equipe:** Trabalho individual  

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Caio Daniel | @DaniCaio |

**Elemento de Competência:** Planejar e projetar testes selecionando técnicas adequadas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Planejamento dos testes

### 2.1 Objetivo dos testes

Verificar se o usuário logado consegue montar e finalizar um pedido, se os valores dos itens e o total estão certos até os centavos (no carrinho e em Meus Pedidos) e se o sistema respeita o limite de 1 a 10 itens, sem deixar finalizar pedido vazio, acima do limite ou sem login.

Regras do LocalEats que usei (do material da disciplina):

- o pedido tem que ter de 1 a 10 itens;
- o valor mínimo do pedido é R$ 30,00;
- pedido a partir de R$ 100,00 tem 10% de desconto.

Nos casos que conferem o cálculo (CT01 e CT02) usei pedidos entre R$ 30,00 e R$ 100,00, para o valor mínimo e o desconto não atrapalharem o resultado.

### 2.2 Escopo

#### Funcionalidades incluídas

| Integrante | Funcionalidade incluída | O que será verificado |
|---|---|---|
| Caio Daniel | Fazer pedido | Adicionar e remover pratos no carrinho, limite de 1 a 10 itens, valor de cada linha e do total, bloqueio da finalização com carrinho vazio ou sem login e se o pedido aparece em Meus Pedidos com o mesmo total. |

A tela Meus Pedidos entra só para conferir se o pedido foi registrado. Os textos que ela mostra não fazem parte do escopo.

#### Funcionalidade não incluída

| Funcionalidade não incluída | Justificativa |
|---|---|
| Favoritar e desfavoritar restaurantes | Não mexe na criação nem no valor do pedido, e um erro nela pesa menos para o cliente do que um erro de cobrança. |
| Filtrar e pesquisar restaurantes | Só servem para chegar no restaurante. Nos testes eu abro o restaurante direto pela lista Explorar. |

### 2.3 Abordagem

| Item | Decisão | Justificativa |
|---|---|---|
| Níveis de teste | Sistema | Vou testar pela tela, do começo ao fim: abrir o restaurante, montar o pedido, finalizar e conferir em Meus Pedidos. |
| Tipos de teste | Funcional | O foco são as regras do pedido: quantidade, cálculo e quando dá para finalizar. Desempenho e outros testes não funcionais ficaram de fora. |
| Perspectiva caixa-preta ou caixa-branca | Caixa-preta | Não tenho acesso ao código, então os casos saem do que eu coloco (pratos, quantidades, login) e do que aparece na tela. |
| Técnicas de teste | Análise de valor limite (com as classes do particionamento de equivalência) e tabela de decisão | A quantidade tem um intervalo (1 a 10) e os erros costumam aparecer nas bordas, em 0 e 1 e em 10 e 11. A tabela de decisão serve porque conseguir finalizar depende de duas coisas juntas: estar logado e ter item no carrinho. |

### 2.4 Ambiente e responsabilidades

| Item | Definição |
|---|---|
| Ambiente necessário | Aplicação em <https://local-eats-unisenac.vercel.app/>, Google Chrome no computador, internet, uma conta de teste (sem dados pessoais nem senha real), o Restaurante Sabor 2 com o Prato Especial 0 (R$ 64.13) e o Prato Especial 1 (R$ 17.91) e uma calculadora. |
| Responsáveis pelo planejamento | Caio Daniel |
| Responsáveis pela especificação dos casos | Caio Daniel |
| Responsáveis pela futura execução | Caio Daniel |

### 2.5 Critérios

| Critério | Definição |
|---|---|
| Entrada | Site no ar, login com a conta de teste funcionando, cardápio do Restaurante Sabor 2 aparecendo e casos CT01 a CT06 revisados. |
| Saída | Todos os casos executados com resultado (passou ou falhou) e evidência, defeitos registrados como issue e os riscos R01, R02 e o requisito RQ01 cobertos por casos executados. |
| Suspensão | Site fora do ar, login sem funcionar, cardápio sem carregar ou algum erro que não deixe finalizar nenhum pedido. |

---

## 3. Tarefa 2: Riscos e técnicas de teste

### 3.1 Análise dos riscos

Para a prioridade, combinei probabilidade e impacto assim:

| Probabilidade \ Impacto | Baixo | Médio | Alto |
|---|:---:|:---:|:---:|
| Alta | Média | Alta | Alta |
| Média | Baixa | Média | Alta |
| Baixa | Baixa | Baixa | Média |

| ID | Integrante | Funcionalidade | Risco | Consequência | Probabilidade | Impacto | Prioridade | Justificativa |
|---|---|---|---|---|:---:|:---:|:---:|---|
| R01 | Caio Daniel | Fazer pedido | O valor de um item ou o total do pedido sair errado, diferente de preço x quantidade ou com arredondamento que faz o total não bater com a soma dos itens. | O cliente vê ou paga um valor diferente do esperado e perde a confiança no app. O restaurante pode receber o valor errado e isso gera reclamação e cancelamento. | Média | Alto | Alta | O impacto é alto porque é dinheiro. A probabilidade não é baixa porque na exploração da Atividade 1 a linha com 2 unidades apareceu como R$ 35.81 (o certo seria R$ 35,82) e a soma dos itens deu R$ 99,94, mas o total mostrava R$ 99,95. |
| R02 | Caio Daniel | Fazer pedido | O pedido ser finalizado com quantidade fora do permitido (1 a 10), ou seja, vazio depois de remover os itens ou com mais de 10 itens. | O restaurante recebe um pedido vazio ou acima da regra, o pedido tem que ser cancelado e o cliente fica frustrado. | Média | Médio | Média | Adicionar e remover itens é comum e dá para clicar em Adicionar várias vezes seguidas. Na exploração o carrinho vazio sumiu da tela, mas não vi nenhum aviso sobre o limite de 10 itens. O impacto é médio porque não tem cobrança errada, mas gera retrabalho. |

Além dos riscos, considerei este requisito:

- RQ01: só usuário logado pode finalizar um pedido. Se a sessão tiver acabado, o sistema tem que pedir login e não registrar o pedido.

### 3.2 Aplicação das técnicas

#### Análise 1: análise de valor limite

**Integrante:** Caio Daniel  
**Funcionalidade:** Fazer pedido  
**Risco relacionado:** R02 e R01  
**Técnica escolhida:** Análise de valor limite, a partir das classes do particionamento de equivalência

**Regra analisada:** o pedido deve ter de 1 a 10 itens. Na tela a quantidade muda pelos botões Adicionar (+1) e "−" (−1). O valor de cada linha é preço x quantidade.

**Por que a técnica foi escolhida:**  
A regra tem um intervalo e os erros costumam aparecer nas bordas. De 1 para 0 decide se o pedido ainda existe e de 10 para 11 decide se o limite é respeitado (R02). Com 2 unidades o sistema faz a primeira multiplicação e pode arredondar errado (R01), que foi o que eu vi na exploração.

**Aplicação da técnica:**

Classes de equivalência:

| Classe | Situação | Valor representativo |
|---|---|---|
| Inválida | Menos de 1 item (itens removidos) | 0 |
| Válida | De 1 a 10 itens | 2 |
| Inválida | Mais de 10 itens | 11 |

Valores limite escolhidos:

| Quantidade | Classe | Por que testar | Caso |
|:---:|---|---|---|
| 0 | Inválida | Logo abaixo do mínimo, não pode finalizar pedido vazio. | CT03 |
| 1 | Válida | Mínimo permitido, a linha e o total têm que ser iguais ao preço do prato. | CT01 |
| 2 | Válida | Logo acima do mínimo, primeira multiplicação (2 x preço). | CT02 |
| 9 | Válida | Logo abaixo do máximo. | CT04 |
| 10 | Válida | Máximo permitido. | CT04 |
| 11 | Inválida | Logo acima do máximo, o sistema não deve aceitar. | CT05 |

No limite máximo (CT04 e CT05) usei um prato só, assim a quantidade do prato é a mesma do pedido. Nesses casos não confiro o total, porque com 10 itens o pedido passa de R$ 100,00 e pode entrar o desconto. O foco é só a quantidade.

**Casos derivados:** CT01, CT02, CT03, CT04 e CT05

#### Análise 2: tabela de decisão

**Integrante:** Caio Daniel  
**Funcionalidade:** Fazer pedido  
**Risco relacionado:** R02 e RQ01  
**Técnica escolhida:** Tabela de decisão

**Por que a técnica foi escolhida:**  
O que acontece quando clica em Finalizar Pedido depende de duas condições ao mesmo tempo: estar logado e ter itens no carrinho. Com a tabela dá para ver todas as combinações, inclusive a do usuário montar o pedido e a sessão acabar antes de finalizar.

**Aplicação da técnica:**

| Regra | Usuário logado? | Carrinho com pelo menos 1 item? | Resultado esperado | Caso |
|:---:|:---:|:---:|---|---|
| 1 | Sim | Sim | Finaliza o pedido e ele aparece em Meus Pedidos. | CT01 e CT02 |
| 2 | Sim | Não | Não deixa finalizar e nenhum pedido é registrado. | CT03 |
| 3 | Não | Sim | Não registra o pedido e pede login. | CT06 |
| 4 | Não | Não | Pede login e nenhum pedido é registrado. | Coberta pelo CT06 |

Não fiz um caso só para a regra 4 porque o resultado esperado é o mesmo da regra 3, e a regra 3 é mais arriscada, já que o usuário tem itens prontos para enviar.

**Casos derivados:** CT06, além das regras 1 e 2, que já são testadas no CT01, CT02 e CT03

---

## 4. Tarefa 3: Casos de teste e rastreabilidade

### 4.1 Casos de teste

Antes de executar, é bom conferir os preços no cardápio. Se tiverem mudado, os resultados esperados precisam ser recalculados.

### CT01: Finalizar pedido com 1 unidade de um prato

**Integrante responsável:** Caio Daniel  
**Funcionalidade:** Fazer pedido  
**Risco ou requisito relacionado:** R01  
**Técnica utilizada:** Análise de valor limite (quantidade 1) e tabela de decisão (regra 1)

**Pré-condição:**  
Usuário de teste logado, carrinho vazio e anotar quantos pedidos tem em Meus Pedidos.

**Dados de entrada:**  
Restaurante: Restaurante Sabor 2  
Prato: Prato Especial 0 (R$ 64,13)  
Quantidade: 1

**Passos:**

1. Em Explorar, abrir o Restaurante Sabor 2.
2. Clicar uma vez em Adicionar no Prato Especial 0.
3. Conferir a linha e o total no carrinho (Seu Pedido).
4. Clicar em Finalizar Pedido.
5. Abrir Meus Pedidos.

**Resultado esperado:**  
O carrinho mostra "1x Prato Especial 0" com R$ 64,13 e total R$ 64,13. Depois de finalizar, Meus Pedidos tem um pedido a mais, com 1 unidade do prato e total R$ 64,13, igual ao do carrinho.

---

### CT02: Conferir o total com 2 unidades de um prato e 1 de outro

**Integrante responsável:** Caio Daniel  
**Funcionalidade:** Fazer pedido  
**Risco ou requisito relacionado:** R01  
**Técnica utilizada:** Análise de valor limite (quantidade 2) e tabela de decisão (regra 1)

**Pré-condição:**  
Usuário de teste logado e carrinho vazio.

**Dados de entrada:**  
Restaurante: Restaurante Sabor 2  
Prato Especial 1 (R$ 17,91), 2 unidades  
Prato Especial 0 (R$ 64,13), 1 unidade

**Passos:**

1. Abrir o Restaurante Sabor 2.
2. Clicar duas vezes em Adicionar no Prato Especial 1.
3. Clicar uma vez em Adicionar no Prato Especial 0.
4. Conferir na calculadora as linhas e o total do carrinho.
5. Clicar em Finalizar Pedido e abrir Meus Pedidos.

**Resultado esperado:**  
A linha "2x Prato Especial 1" mostra R$ 35,82 (2 x 17,91), a linha "1x Prato Especial 0" mostra R$ 64,13 e o total mostra R$ 99,95, que é a soma das duas. Os valores têm duas casas decimais e o pedido em Meus Pedidos tem o mesmo total.

---

### CT03: Não deixar finalizar pedido sem itens

**Integrante responsável:** Caio Daniel  
**Funcionalidade:** Fazer pedido  
**Risco ou requisito relacionado:** R02  
**Técnica utilizada:** Análise de valor limite (quantidade 0) e tabela de decisão (regra 2)

**Pré-condição:**  
Usuário de teste logado, carrinho vazio e anotar quantos pedidos tem em Meus Pedidos.

**Dados de entrada:**  
Restaurante: Restaurante Sabor 2  
Prato: Prato Especial 1, primeiro com 1 unidade e depois com 0

**Passos:**

1. Abrir o Restaurante Sabor 2.
2. Clicar uma vez em Adicionar no Prato Especial 1.
3. No carrinho, clicar no "−" ao lado do prato.
4. Ver se o carrinho e o botão Finalizar Pedido continuam aparecendo.
5. Abrir Meus Pedidos e comparar com a quantidade anotada.

**Resultado esperado:**  
O prato sai do pedido e, com o carrinho vazio, o botão Finalizar Pedido não aparece (ou fica desabilitado). Meus Pedidos continua com a mesma quantidade de pedidos.

---

### CT04: Aceitar pedido com 9 e com 10 itens

**Integrante responsável:** Caio Daniel  
**Funcionalidade:** Fazer pedido  
**Risco ou requisito relacionado:** R02  
**Técnica utilizada:** Análise de valor limite (quantidades 9 e 10)

**Pré-condição:**  
Usuário de teste logado e carrinho vazio.

**Dados de entrada:**  
Restaurante: Restaurante Sabor 2  
Prato: Prato Especial 1, primeiro com 9 unidades e depois com 10

**Passos:**

1. Abrir o Restaurante Sabor 2.
2. Clicar nove vezes em Adicionar no Prato Especial 1.
3. Conferir a quantidade no carrinho.
4. Clicar mais uma vez em Adicionar no mesmo prato.
5. Conferir a quantidade e clicar em Finalizar Pedido.

**Resultado esperado:**  
Depois do passo 2 o carrinho mostra "9x Prato Especial 1" e depois do passo 4 mostra "10x Prato Especial 1", sem erro. O pedido com 10 itens é finalizado e aparece em Meus Pedidos.

---

### CT05: Não deixar fazer pedido com 11 itens

**Integrante responsável:** Caio Daniel  
**Funcionalidade:** Fazer pedido  
**Risco ou requisito relacionado:** R02  
**Técnica utilizada:** Análise de valor limite (quantidade 11)

**Pré-condição:**  
Usuário de teste logado, carrinho vazio e anotar quantos pedidos tem em Meus Pedidos.

**Dados de entrada:**  
Restaurante: Restaurante Sabor 2  
Prato: Prato Especial 1, 11 unidades

**Passos:**

1. Abrir o Restaurante Sabor 2.
2. Clicar dez vezes em Adicionar no Prato Especial 1 e conferir que o carrinho mostra "10x".
3. Clicar pela 11ª vez em Adicionar no mesmo prato.
4. Conferir a quantidade e tentar clicar em Finalizar Pedido.
5. Abrir Meus Pedidos e comparar com a quantidade anotada.

**Resultado esperado:**  
O sistema não aceita a 11ª unidade: o carrinho continua com "10x Prato Especial 1" ou aparece uma mensagem sobre o limite de 10 itens. Nenhum pedido com 11 itens é registrado.

---

### CT06: Não deixar finalizar quando a sessão acabou

**Integrante responsável:** Caio Daniel  
**Funcionalidade:** Fazer pedido  
**Risco ou requisito relacionado:** RQ01  
**Técnica utilizada:** Tabela de decisão (regra 3)

**Pré-condição:**  
Usuário de teste logado, carrinho vazio e anotar quantos pedidos tem em Meus Pedidos.

**Dados de entrada:**  
Restaurante: Restaurante Sabor 2  
Prato: Prato Especial 0, 1 unidade

**Passos:**

1. Na aba A, abrir o Restaurante Sabor 2 e clicar em Adicionar no Prato Especial 0.
2. Abrir o LocalEats numa nova aba (aba B) e clicar no ícone de sair, do lado do "Olá".
3. Voltar para a aba A, sem atualizar a página, e clicar em Finalizar Pedido.
4. Entrar de novo com a conta de teste e abrir Meus Pedidos.

**Resultado esperado:**  
O sistema não registra o pedido e pede login, indo para a tela Entrar ou mostrando uma mensagem. Depois do novo login, Meus Pedidos continua com a mesma quantidade de pedidos.

---

### 4.2 Matriz de rastreabilidade

| Integrante | Funcionalidade | Risco ou requisito | Técnica utilizada | Casos de teste |
|---|---|---|---|---|
| Caio Daniel | Fazer pedido | R01: valor do item ou total errado (prioridade Alta) | Análise de valor limite (quantidades 1 e 2) | CT01 e CT02 |
| Caio Daniel | Fazer pedido | R02: quantidade fora de 1 a 10 (prioridade Média) | Análise de valor limite (quantidades 0, 9, 10 e 11) e tabela de decisão (regra 2) | CT03, CT04 e CT05 |
| Caio Daniel | Fazer pedido | RQ01: só usuário logado finaliza pedido | Tabela de decisão (regras 3 e 4) | CT06 |

Todos os riscos e o requisito têm pelo menos um caso de teste. Se o tempo para testar diminuir, eu faria primeiro o CT02 e o CT01, que são do R01 (prioridade Alta), depois o CT05, o CT03 e o CT04 (R02) e por último o CT06.

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
Claude (Anthropic).

**Como foi utilizada:**  
Usei para ter ideias de riscos na parte de pedidos, comparar quais técnicas faziam mais sentido e revisar se os passos e os resultados esperados estavam claros.

**Uma sugestão que precisou ser alterada ou rejeitada:**  
Na primeira versão o valor limite só olhava o mínimo (0 e 1), porque a tela do LocalEats não mostra limite máximo, e o CT01 usava um pedido de R$ 17,91. Quando revisei com as regras do LocalEats do material da disciplina (1 a 10 itens e mínimo de R$ 30,00), coloquei os valores 9, 10 e 11 (CT04 e CT05) e troquei o prato do CT01 para o pedido passar de R$ 30,00.

**Como as respostas foram verificadas:**  
Conferi no site os nomes dos botões, dos pratos e os preços, comparei os limites com as regras do material da disciplina, refiz as contas na calculadora e conferi na matriz se todos os riscos têm casos ligados a eles.
