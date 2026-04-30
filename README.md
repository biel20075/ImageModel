# Projeto Site com Reconhecimento de Jóias

Este projeto combina uma página web estática com scripts Python de apoio para testes e demonstrações de programação. A pasta `test-assistent-programing` contém exemplos de código em Python que abordam verificação de números primos, cálculo de estatísticas de listas e um exercício de depuração.

## Estrutura do projeto

- `index.html` - Página web principal do projeto.
- `test-assistent-programing/` - Pasta com scripts Python e explicações de código.
  - `debug.py` - Programa que lê itens e calcula subtotal, imposto e desconto.
  - `num_primo.py` - Verifica se um número inteiro é primo e exibe o resultado.
  - `rafatoracao.py` - Cálculo de estatísticas (total, média, máximo e mínimo) para uma lista de números.
  - `explicacao-debug.md` - Documentação do processo de depuração do script `debug.py`.
  - `explicacao_num_primo.md` - Explicação do funcionamento do script `num_primo.py`.
  - `explicacao_refatoracao.md` - Explicação das melhorias aplicadas no script `rafatoracao.py`.

## Descrição dos componentes

### `index.html`
Página web estática com layout em Bootstrap e estilo customizado. O arquivo define uma interface escura com componentes visuais para webcam, botões e seções de resultados, sugerindo um projeto de reconhecimento de imagens ou detecção de objetos.

### `test-assistent-programing/debug.py`
Script interativo que:
- solicita o nome do cliente;
- lê quantidade e preço de três itens;
- calcula total de cada item, subtotal, imposto de 10% e desconto com base em cupom;
- exibe o valor final formatado em reais.

### `test-assistent-programing/num_primo.py`
Script que verifica se um número é primo usando uma função `eh_primo(n)` otimizada:
- descarta valores menores que 2;
- trata `2` e `3` como casos base;
- elimina múltiplos de 2 e 3;
- testa divisores no formato `6k ± 1` até a raiz quadrada de `n`.

### `test-assistent-programing/rafatoracao.py`
Programa que calcula estatísticas básicas para uma lista de valores:
- total;
- média;
- máximo;
- mínimo.

A função principal `calculate_list_statistics(numbers)` valida entrada para evitar lista vazia e retorna os quatro valores em uma tupla.

## Como executar

### Exibir a página web
Abra `index.html` no navegador.

### Executar os scripts Python
Abra um terminal na pasta do projeto e execute os scripts com Python 3. Por exemplo:

```bash
python test-assistent-programing/debug.py
python test-assistent-programing/num_primo.py
python test-assistent-programing/rafatoracao.py
```

> Observação: Use `python3` em vez de `python` se o seu ambiente requerer essa chamada.

## Notas

- `debug.py` foi escrito como um exercício de depuração e inclui comentários que explicam a lógica de cálculo.
- `num_primo.py` possui docstring em formato Google para facilitar entendimento e documentação.
- `rafatoracao.py` demonstra boas práticas como nomenclatura clara, validação de entrada e funções reutilizáveis.

## Melhorias sugeridas

- Adicionar um script de inicialização para a página web se houver dependências JavaScript externas.
- Converter `debug.py` em uma função reutilizável para aceitar listas de itens e aplicar descontos dinâmicos.
- Incluir testes automatizados para `num_primo.py` e `rafatoracao.py`.
