<h2> ⛓️ Proposta - Desafio de Projeto 1 Sistema Bancário</h2>

Desafio de projeto cujo objetivo é criar um sistema bancário com a linguagem Python.

🔹 Na [Versão 1](https://github.com/NicoleNF/python-developer/blob/main/desafios_projeto/sistema_bancarioV1.py) do projeto, você foi contratado por um grande banco para desenvolver um novo sistema. Esse banco deseja modernizar as operações e escolheu a linguagem Python. Para a primeira versão você deve implementar apenas 2 operações: depósito, saque e extrato.

<h2> 🎯 Objetivos </h2>

🔹 Operação de Depósito: Deve ser possível depositar valores positivos para a conta bancária. A versão 1 do projeto trabalha apenas com um usuário, dessa forma não é necessário se preocupar em indentificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

🔹 Operação de Saque: O sistema deve permitir realizar 3 saques diários com lmite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro porr falta de saldoo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

🔹 Operação de Extrato: Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listtagem deve ser exiibido o saldo atual da conta. Os valores devem ser exibidos utilizando o formato R$ xxx.xx.

------------------------------------

<h2> ⛓️ Proposta - Desafio de Projeto 2 Otimização do Sistema Bancário</h2>

Otimizando o sistema bancário com funções Python

🔸 Na [Versão 2](https://github.com/NicoleNF/python-developer/blob/main/desafios_projeto/sistema_bancarioV2.py), deve-se separar as funções existentes de saques, depósitos e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente do banco) e cadastrar conta bancária.

<h2> 🎯 Objetivos </h2>

🔸 Deixar o código mais modularizado, criando funções para as operações existentes: sacar, depositar e visualizar histórico. Além disso, para a versão 2 do sistema é preciso criar duas novas funções: usuário (cliente do banco) e criar conta corrente (vincular com usuário).

🔸 Deve-se criar funções para todas as operações do sistema. Cada função terá uma regra na passagem de argumentos.

🔸 A função Saque deve receber os argumentos apenas por nome (keyword only).

🔸 A função Depósito deve receber argumentos apenas por posição (positional only).

🔸 A função Extrato deve receber os argumentos por posição e nome (positional only e keyword only).

🔸 Criar Usuário (cliente): O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro, nro - bairro - cidade/sigla estado. Deve ser armazenado somente os números do CPF e não deve ser possível cadastrar dois usuários com o mesmo CPF.

🔸 Criar Conta Corrente: O programa deve armazenar contas em uma lista, uma conta deve ser composta por: agência, número da conta e usuário. O número da conta é sequêncial, iniciando em 1. O número da agência é fixo: "0001" e o usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

------------------------------------

<h2> ⛓️ Proposta - Desafio de Projeto 3 Modelando o Sistema Bancário em POO com Python </h2>

Nessa [Versão 3](https://github.com/NicoleNF/python-developer/blob/main/desafios_projeto/sistema_bancarioV3.py), a atualização e implementação do sistema bancário para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários, seguindo um modelo UML. Atualizações tabém dos métodos que tratam as opções do menu, para funcionarem com as classes modeladas.

------------------------------------

Este repositório foi criado para fins de estudo e acompanhamento pessoal de progresso com a linguagem Python, através do curso de Python Developer pela DIO e outros cursos e sites de estudo.

[Nicole Ferreira](https://www.linkedin.com/in/nicole-ferreira-929b841a0/).
