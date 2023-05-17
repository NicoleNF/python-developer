<h1> Formação Python Developer </h1>

<p> Desafios de projeto e códigos desenvolvidos para o curso de Python Developer da Digital Innovation One. 

<h2> 🛑 Pré-requisitos </h2>

- [x] Linguagem Python 3
- [x] IDE para desenvolvimento Python
- [x] Fundamentos da sintaxe Python

<h2> ⛓️ Proposta - Desafio de Projeto 1</h2>

Desafio de projeto para o curso Python Developer pela DIO, o objetivo é criar um sistema bancário com a linguagem Python.

🔹 Na [Versão 1] (https://github.com/NicoleNF/sistema-bancario/blob/main/desafio_projeto/sistema_bancarioV1.py) do projeto, você foi contratado por um grande banco para desenvolver um novo sistema. Esse banco deseja modernizar as operações e escolheu a linguagem Python. Para a primeira versão você deve implementar apenas 2 operações: depósito, saque e extrato.

<h2> 🎯 Objetivos </h2>

🔹 Operação de Depósito: Deve ser possível depositar valores positivos para a conta bancária. A versão 1 do projeto trabalha apenas com um usuário, dessa forma não é necessário se preocupar em indentificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

🔹 Operação de Saque: O sistema deve permitir realizar 3 saques diários com lmite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro porr falta de saldoo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

🔹 Operação de Extrato: Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listtagem deve ser exiibido o saldo atual da conta. Os valores devem ser exibidos utilizando o formato R$ xxx.xx.

------------------------------------

<h2> ⛓️ Proposta - Desafio de Projeto 2</h2>

Otimizando o sistema bancário com funções Python

🔸 Na [Versão 2] (https://github.com/NicoleNF/python-developer/blob/main/desafio_projeto/sistema_bancarioV2.py) deve-se separar as funções existentes de saques, depósitos e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente do banco) e cadastrar conta bancária.

<h2> 🎯 Objetivos </h2>

🔸 Deixar o código mais modularizado, criando funções para as operações existentes: sacar, depositar e visualizar histórico. Além disso, para a versão 2 do sistema é preciso criar duas novas funções: usuário (cliente do banco) e criar conta corrente (vincular com usuário).

🔸 Deve-se criar funções para todas as operações do sistema. Cada função terá uma regra na passagem de argumentos.

🔸 A função Saque deve receber os argumentos apenas por nome (keyword only).

🔸 A função Depósito deve receber argumentos apenas por posição (positional only).

🔸 A função Extrato deve receber os argumentos por posição e nome (positional only e keyword only).

🔸 Criar Usuário (cliente): O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro, nro - bairro - cidade/sigla estado. Deve ser armazenado somente os números do CPF e não deve ser possível cadastrar dois usuários com o mesmo CPF.

🔸 Criar Conta Corrente: O programa deve armazenar contas em uma lista, uma conta deve ser composta por: agência, número da conta e usuário. O número da conta é sequêncial, iniciando em 1. O número da agência é fixo: "0001" e o usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

------------------------------------

<h2> ➰ Propostas - Desafios de Código (Básicos)</h2>

## 1️⃣- Tuitando

O microblog Twitter é conhecido por limitar as postagens em 140 caracteres. Conferir se um texto vai caber em um tuíte é sua tarefa.

**Entrada**</br>
A entrada é uma linha de texto T (1 ≤ |T| ≤ 500).

**Saída**</br>
A saída é dada em uma única linha. Ela deve ser "TWEET" (sem as aspas) se a linha de texto T tem até 140 caracteres. Se T tem mais de 140 caracteres, a saída deve ser "MUTE".

Veja a resolução do *Desafio 1* <a href= >aqui</a>.

## 2️⃣ - Mês

Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.

**Entrada**</br>

A entrada contém um único valor inteiro.

**Saída**</br>

Imprima por extenso o nome do mês correspondente ao número existente na entrada, com a primeira letra em maiúscula.

Veja a resolução do *Desafio 2* <a href= >aqui</a>.

## 3️⃣ - Encaixa ou Não?

Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para verificar, à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.

**Entrada**</br>

A entrada consiste de vários casos de teste. A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste. Cada caso de teste consiste de dois valores A e B maiores que zero, cada um deles podendo ter até 1000 dígitos.

**Saída**</br>

Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no primeiro valor, confome exemplo abaixo.

Veja a resolução do *Desafio 3* <a href= >aqui</a>.

## 4️⃣ - Dragão!

Daenerys é a khaleesi dos Dothraki. Juntamente com Drogon, eles vão atrás do Tyrion, para tentar dominar Westeros. Ela possui, além do seu dragãozinho, um rastreador que mede o nível de energia de qualquer ser vivo. Todos os seres com o nível menor ou igual a 8000, ela considera como se fosse um inseto. Quando passa deste valor, que foi o caso do Drogon, ela se espanta e grita “Mais de 8000”. Baseado nisso, utilize a mesma tecnologia e analise o nível de energia dos seres vivos.

**Entrada**</br>
A primeira linha contém um número inteiro C relativo ao número de casos de teste. Em seguida, haverá C linhas, com um número inteiro N (100 <= N <= 100000) relativo ao nível de energia de um ser vivo.

**Saída**</br>
Para cada valor lido, imprima o texto correspondente.

Veja a resolução do *Desafio 4* <a href= >aqui</a>.


<h1 align=center>Desafios de Código (Intermediários)</h1>

## 1️⃣ - Aproveite a Oferta

Um supermercado está fazendo uma promoção de venda de refrigerantes. Se um dia você comprar refrigerantes e levar os cascos vazios no dia seguinte, ela troca cada conjunto de K garrafas vazias  por uma garrafa cheia. Um cliente quer aproveitar ao máximo essa oferta e por isso comprou várias garrafas no primeiro dia da promoção. Agora ele quer saber quantas garrafas terá ao final do segundo dia da promoção, se usá-la ao máximo. Faça um programa para calcular isso.

**Entrada**</br>
A primeira linha de entrada contém inteiro T (1 ≤ T ≤ 10000) , que indica o número de casos de teste. Em cada uma das T linhas a seguir vêm dois inteiros N e K (1 ≤ K, N ≤ 10000),  respectivamente o número de refrigerantes comprados e o número de garrafas vazias para ganhar uma cheia.

**Saída**</br>

Para cada caso de teste imprima o número de garrafas que o cliente terá no segundo dia, se aproveitar ao máximo a oferta.

Veja a resolução do *Desafio 1* <a href= >aqui</a>.

## 2️⃣ - Animal

Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita. Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

<img width="400px" align="right" src="https://user-images.githubusercontent.com/13790608/230700086-43601eb7-ad47-4b16-9451-8912043274cc.png">

**Entrada**</br>
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

**Saída**</br>
Imprima o nome do animal correspondente à entrada fornecida.

Veja a resolução do *Desafio 2* <a href= >aqui</a>.



------------------------------------

Este repositório foi criado para fins de estudo e acompanhamento pessoal de progresso com a linguagem Python, através do curso de Python Developer pela DIO e outros cursos e sites de estudo.

[Nicole Ferreira](https://www.linkedin.com/in/nicole-ferreira-929b841a0/).
