# Desafio: Criando um Sistema Bancário

## Objetivo Geral

Criar um sistema bancário com as operações: **sacar**, **depositar** e **visualizar extrato**.

## Desafio

Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e, para isso, escolheu a linguagem **Python**. Para a primeira versão do sistema, devemos implementar apenas 3 operações: **depósito**, **saque** e **extrato**.

## Operação de Depósito

- Deve ser possível depositar valores **positivos** na conta bancária.
- A versão inicial do projeto trabalha apenas com **1 usuário**, então não precisamos nos preocupar em identificar o número da agência ou conta bancária.
- Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de **extrato**.

## Operação de Saque

- O sistema deve permitir realizar **3 saques diários**, com limite máximo de **R$ 500,00 por saque**.
- Caso o usuário não tenha saldo suficiente, o sistema deve exibir uma mensagem informando que **não será possível sacar o dinheiro por falta de saldo**.
- Todos os saques devem ser armazenados em uma variável e exibidos na operação de **extrato**.

## Operação de Extrato

- A operação deve listar todos os **depósitos** e **saques** realizados na conta.
- No final da listagem, deve ser exibido o **saldo atual** da conta.
- Se o extrato estiver em branco, exibir a mensagem: **"Não foram realizadas movimentações."**

Os valores devem ser exibidos no formato **R$ xxx.xx**.

**Exemplo**:

- `1500.45` = **R$ 1500,45**
