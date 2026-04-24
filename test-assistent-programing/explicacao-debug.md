# Explicação do debug de debug.py

## Identificação do erro
1. Falta de aspas na chamada de `input()` para o preço do item 1: `float(input(Preço do item 1? ))`.
2. `desconto_cupom` é lido como string, mas depois usado em cálculo numérico: `subtotal * (desconto_cupom / 100)`.
3. A linha do item 2 não usa uma f-string correta e imprime o texto literal com chaves: `print(" Item 2:        R$ {total_item2:.2f}")`.
4. O bloco `if desconto_cupom > 0:` não tem indentação no `print()`, causando erro de sintaxe.

## Causa do erro
- O prompt do `input()` sem aspas não é uma string válida em Python, provocando um erro de sintaxe imediatamente.
- `input()` retorna uma string, então `desconto_cupom` precisa ser convertido para `float` antes de dividir por 100.
- Sem o `f` antes das aspas, Python não expande as expressões entre `{}` no `print()`.
- A falta de indentação no corpo do `if` viola a sintaxe de blocos do Python.

## Correção aplicada
- Corrigi a chamada para `float(input("Preço do item 1? "))` e adicionei as aspas ao prompt.
- Converto `desconto_cupom` para `float` no momento da leitura: `desconto_cupom = float(input(...))`.
- Ajustei o `print()` do item 2 para usar f-string: `print(f" Item 2:        R$ {total_item2:.2f}")`.
- Indentei corretamente o `print()` dentro do `if desconto_cupom > 0:`.
- Removi o uso desnecessário de `round()` na exibição final, já que a formatação `:.2f` já cuida dos dois decimais.

## Resultado final
O programa agora lê corretamente os valores dos itens, calcula subtotal, imposto e desconto, e exibe o total formatado em reais.
