# PL2025

## Unidade Curricular

**Nome:** Processamento de linguagens

**Sigla:** PL

**Ano:** 2025

## Aluno

**Nome:** João Miguel Mendes Moura

**Id:** A100615

## Trabalho efetuado:

O programa utiliza a biblioteca ply.lex para definir tokens que representam as diferentes instruções que podem ser fornecidas à máquina de vendas, como LISTAR, MOEDA, SELECIONAR, SALDO e SAIR.

Os usuários podem selecionar itens disponíveis na máquina pelo seu código. O programa verifica se o item está em estoque e se o saldo do usuário é suficiente para a compra. Se sim, o item é dispensado e o saldo é atualizado. Caso contrário, são exibidas mensagens apropriadas indicando saldo insuficiente ou estoque esgotado.

O programa lida adequadamente com entradas inválidas do usuário, fornecendo mensagens de erro claras e identificáveis para orientação.

O estoque da máquina é mantido em um arquivo JSON chamado "stock.json", permitindo que as informações sobre os itens disponíveis sejam preservadas entre as execuções do programa e que tambem um produto sem estoque seja selecionado pelo user.