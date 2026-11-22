# Atividade 2: Organização da Qualidade no LocalEats

## 1. Identificação

**Equipe:** Trabalho individual  

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Caio Daniel | @DaniCaio |

**Elemento de Competência:** Identificar papéis, responsabilidades e competências relacionadas às atividades de qualidade e testes.

---

## 2. Tarefa 1: Diagnóstico da situação

### 2.1 Problemas organizacionais

| Problema identificado | Possível consequência para o produto ou para a equipe |
|---|---|
| Não tem critério para dizer quando uma funcionalidade está pronta. | Cada um decide quando terminou e coisas vão para o usuário sem teste, como o total do pedido errado. |
| Parte da equipe acha que só o QA testa. | Ninguém faz teste unitário nem revisão de código, os erros aparecem só no final e o QA fica sobrecarregado. |
| Os defeitos não são registrados nem acompanhados, e ninguém sabe quem aprova uma versão nova. | Defeitos são esquecidos e voltam, e versões saem sem ninguém avaliar o risco. |

### 2.2 Responsabilidade pela qualidade

**A qualidade do LocalEats deve ser responsabilidade exclusiva do profissional de QA? Justifiquem.**

Não. O QA ajuda planejando e executando os testes, mas a qualidade depende de todo mundo. O responsável pelo produto precisa definir bem os critérios de aceitação, o desenvolvedor testa e revisa o código e o líder técnico define os padrões. Se o cálculo do total do pedido tivesse um critério de aceitação e um teste unitário, o erro de centavos teria sido pego antes de chegar no QA.

---

## 3. Tarefa 2: Papéis e competências

| Integrante | Papel analisado | Responsabilidades relacionadas à qualidade | Competências técnicas | Competências comportamentais |
|---|---|---|---|---|
| Caio Daniel | Responsável pelo produto (Product Owner) | Escrever as histórias com critérios de aceitação que dê para testar, decidir quais defeitos corrigir primeiro e aprovar a liberação das versões. | Escrita de critérios de aceitação, conhecer o negócio de pedidos e entregas, priorização e noções de LGPD. | Comunicação, tomada de decisão e negociação de prioridades. |
| Caio Daniel | Desenvolvedor | Implementar seguindo os critérios, criar testes unitários, revisar o código dos colegas e corrigir os defeitos. | As linguagens do projeto (JavaScript e Python), pytest, Git, pull requests e cuidado com cálculo de valores em dinheiro. | Colaboração, saber receber crítica na revisão e atenção aos detalhes. |
| Caio Daniel | QA (analista de qualidade) | Revisar os requisitos desde o começo, planejar e executar os testes de sistema pelos riscos, registrar e acompanhar os defeitos até o reteste e passar a situação da qualidade antes da liberação. | Técnicas de teste (particionamento, valor limite, tabela de decisão e transição de estados), escrever casos de teste e relatos de defeito, GitHub Issues e noções de automação. A CTFL ajuda, mas não substitui a prática. | Pensamento crítico, relatar defeitos sem acusar ninguém, curiosidade e organização. |
| Caio Daniel | Liderança técnica (Tech Lead) | Definir os padrões de código, deixar a revisão por pull request obrigatória, garantir que os testes rodem antes de integrar e avaliar os riscos técnicos da liberação. | Arquitetura da aplicação, integração contínua (GitHub Actions), revisão de código e métricas como cobertura de testes. | Liderança, orientar a equipe e resolver conflitos. |

---

## 4. Tarefa 3: Matriz de responsabilidades

Utilizei:

- **R:** responsável por executar a atividade;
- **A:** aprovador ou responsável final;
- **C:** consultado antes da execução ou decisão;
- **I:** informado sobre o resultado;
- **R/A:** o mesmo papel executa e aprova;
- **-:** o papel não participa da atividade.

| Atividade de qualidade | Responsável pelo produto | Desenvolvedor | QA | Liderança técnica |
|---|:---:|:---:|:---:|:---:|
| Definir critérios de aceitação | R/A | C | C | I |
| Revisar requisitos | A | C | R | C |
| Implementar a funcionalidade | C | R | I | A |
| Revisar o código | - | R | - | A |
| Criar testes unitários | - | R | C | A |
| Planejar e executar testes do sistema | C | C | R/A | I |
| Registrar e acompanhar defeitos | I | R | R/A | I |
| Priorizar a correção dos defeitos | R/A | I | C | C |
| Aprovar a disponibilização da versão | R/A | I | C | C |

Deixei com o responsável pelo produto as decisões de negócio (critérios, prioridade dos defeitos e liberação), ouvindo o QA e o líder técnico. O líder técnico aprova a parte técnica. O desenvolvedor é R no registro de defeitos porque atualiza o defeito quando corrige, e o QA aprova o fechamento depois do reteste. Coloquei o QA como consultado nos testes unitários para mostrar que testar não é só com ele.

### 4.1 Lacuna ou conflito encontrado

**Lacuna ou conflito:**  
"Planejar e executar testes do sistema" ficou concentrado no QA, que é R e A ao mesmo tempo, ou seja, ele testa e aprova o próprio trabalho. E só tem um QA na equipe.

**Consequência:**  
Se o QA ficar sobrecarregado ou faltar, os testes param e a versão atrasa ou sai sem teste. Isso também reforça a ideia de que só o QA testa. Para melhorar, os desenvolvedores poderiam executar parte dos testes de sistema, testando a funcionalidade de um colega, e o QA ficaria como A do plano de testes.

### 4.2 Práticas de QA recomendadas

| Prática recomendada | Problema que ajuda a resolver | Papéis envolvidos |
|---|---|---|
| Reunião com produto, desenvolvimento e QA (os "três amigos") para escrever os critérios de aceitação antes de desenvolver, junto com uma Definition of Done da equipe. | Falta de critério para considerar algo pronto e defeitos chegando ao usuário. | Responsável pelo produto, Desenvolvedor, QA e Liderança técnica |
| Registrar todos os defeitos no GitHub Issues com um modelo (passos, resultado esperado, resultado obtido e evidência), acompanhar o status de cada um e fazer uma triagem por semana. | Defeitos que não são registrados nem acompanhados e atividades sem responsável. | QA, Desenvolvedor, Responsável pelo produto e Liderança técnica |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
Claude (Anthropic).

**Como foi utilizada:**  
Usei para ter ideias de responsabilidades e competências de cada papel, montar uma primeira versão da matriz RACI e revisar o texto.

**Como as respostas foram verificadas:**  
Conferi linha por linha se cada atividade da matriz tem pelo menos um R e só um A, mudei a matriz para o QA não ficar com tudo e vi se as práticas resolvem os problemas que coloquei no diagnóstico.
