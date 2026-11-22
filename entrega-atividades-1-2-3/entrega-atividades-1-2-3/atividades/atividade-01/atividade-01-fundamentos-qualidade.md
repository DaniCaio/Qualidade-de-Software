# Atividade 1: Fundamentos e Características da Qualidade no LocalEats

## 1. Identificação

**Equipe:** Trabalho individual  

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Caio Daniel | @DaniCaio |

**Elemento de Competência:** Compreender os fundamentos de qualidade de software e sua aplicação no desenvolvimento de sistemas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Fundamentos da qualidade

### 2.1 Necessidades explícitas e implícitas

| Tipo | Necessidade | Interessado | Consequência se não for atendida |
|---|---|---|---|
| Explícita | Fazer pedido pelo app escolhendo os pratos de um restaurante. | Cliente e restaurante | O cliente não consegue comprar e o restaurante perde a venda. |
| Explícita | Filtrar os restaurantes por especialidade (italiana, japonesa...). | Cliente | O cliente precisa olhar a lista toda até achar o que quer e pode desistir. |
| Implícita | Os valores do pedido estarem certos, até nos centavos, e o total bater com a soma dos itens. Ninguém pede isso, mas todo mundo espera. | Cliente, restaurante e LocalEats | O cliente desconfia da cobrança e pode reclamar ou cancelar o pedido. |
| Implícita | O histórico de pedidos mostrar o nome do restaurante e dos pratos e o status em português. | Cliente | O cliente não reconhece o que pediu nem sabe como está o pedido. |

### 2.2 Questão sobre os fundamentos da qualidade

**Um sistema que implementa todas as funcionalidades explicitamente solicitadas pode, ainda assim, apresentar baixa qualidade? Justifiquem utilizando pelo menos uma necessidade implícita identificada pela equipe.**

Sim. Não basta a função existir, ela tem que atender o que o usuário espera. No LocalEats dá para consultar os pedidos, mas aparece "Restaurante ID: 3", "Item Id #8" e o status "PENDING" em inglês, então o cliente não entende o próprio pedido. E no carrinho o total não fecha com a soma dos itens. As funções estão lá, mas a qualidade fica baixa.

---

## 3. Tarefa 2: Exploração da aplicação

| Integrante | Funcionalidade | O que foi realizado | O que foi observado | Evidência |
|---|---|---|---|---|
| Caio Daniel | Fazer pedido | Uso esperado: entrei com minha conta de teste, abri o Restaurante Sabor 2, coloquei 2 Prato Especial 1 (R$ 17.91) e 1 Prato Especial 0 (R$ 64.13), finalizei e fui em Meus Pedidos. Uso alternativo: coloquei um prato e tirei no botão "−" para ver se dava para finalizar com o carrinho vazio. | No carrinho apareceu "2x Prato Especial 1" R$ 35.81, "1x Prato Especial 0" R$ 64.13 e total R$ 99.95. Só que 2 x 17,91 dá 35,82, e 35,81 + 64,13 dá 99,94, um centavo a menos que o total. Os valores também aparecem com ponto e não com vírgula. Em Meus Pedidos o pedido ficou como "PENDING", com "Restaurante ID: 3" e "Item Id #8" e "Item Id #7" no lugar dos nomes. No uso alternativo, quando tirei o item o carrinho sumiu junto com o botão Finalizar Pedido, então não deu para finalizar vazio. | [carrinho com total](evidencias/caio-pedido-carrinho-total.png), [meus pedidos](evidencias/caio-pedido-meus-pedidos.png), [carrinho vazio](evidencias/caio-pedido-carrinho-vazio.png) |

---

## 4. Tarefa 3: Requisitos e características de qualidade

| Integrante | Requisito de Qualidade | Característica ou subcaracterística | Justificativa | Como avaliar |
|---|---|---|---|---|
| Caio Daniel | Cada item do pedido tem que valer preço x quantidade e o total tem que ser a soma dos itens, com duas casas decimais (R$ 0,00), mostrando o mesmo valor no carrinho e em Meus Pedidos. | Corretude Funcional (Adequação Funcional) | É sobre o sistema dar o resultado certo, e com dinheiro tem que estar certo até o centavo. Na exploração, o valor das 2 unidades e o total não fecharam. O ponto no lugar da vírgula também é um problema de Usabilidade, mas o principal é o cálculo, por isso fiquei com Corretude Funcional. | Fazer alguns pedidos com pratos e quantidades diferentes e conferir na calculadora cada linha, a soma das linhas e o total em Meus Pedidos. Depois contar em quantos pedidos deu diferença de 1 centavo ou mais. |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
Claude (Anthropic).

**Como foi utilizada:**  
Usei para organizar as necessidades, pensar no requisito e revisar o texto. Também usei para entender como funciona a parte de pedidos do LocalEats.

**Como as respostas foram verificadas:**  
Refiz a exploração com a minha conta e tirei os prints que estão na pasta evidencias. Conferi as contas na calculadora e comparei a característica escolhida com o material da ISO/IEC 25010 da aula.
