# Explicação do arquivo `num_primo.py`

O código em `num_primo.py` define a função `eh_primo` e organiza a execução de teste em `main()`.

## 1. Definição da função `eh_primo`

```python
def eh_primo(n: int) -> bool:
    """Retorna True se n for primo, caso contrário False."""
```

- Define a função `eh_primo`.
- `n: int` indica que o parâmetro deve ser inteiro.
- `-> bool` indica que o retorno é booleano.
- A docstring descreve o comportamento da função.

```python
    if n < 2:
        return False
```

- Números menores que 2 não são primos.
- Retorna `False` imediatamente nesses casos.

```python
    if n in (2, 3):
        return True
```

- Trata os casos especiais de 2 e 3.
- Esses valores são primos e não precisam de verificações adicionais.

```python
    if n % 2 == 0 or n % 3 == 0:
        return False
```

- Elimina múltiplos de 2 ou de 3.
- Usa o resto da divisão inteira `%`.
- Se `n` for divisível por 2 ou 3, não é primo.

```python
    divisor = 5
    while divisor * divisor <= n:
```

- Inicializa o divisor candidato em 5.
- O laço roda enquanto o quadrado do divisor for menor ou igual a `n`.
- É suficiente testar até a raiz quadrada de `n`.

```python
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
```

- Verifica dois candidatos a cada passo: `divisor` e `divisor + 2`.
- Essa abordagem cobre números na forma `6k-1` e `6k+1`.
- Se `n` for divisível por qualquer um desses, retorna `False`.

```python
        divisor += 6
```

- Avança o divisor em 6 unidades.
- Pula múltiplos de 2 e 3, tornando a busca mais eficiente.

```python
    return True
```

- Se não for encontrado divisor até a raiz quadrada, `n` é primo.
- Retorna `True`.

## 2. Função principal de teste

```python
def main() -> None:
    try:
        numero = int(input("Digite um número inteiro: "))
        if eh_primo(numero):
            print(f"{numero} é primo.")
        else:
            print(f"{numero} não é primo.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
```

- A função `main()` solicita ao usuário um número inteiro via entrada padrão.
- Usa um bloco `try-except` para capturar erros de conversão (caso o usuário digite algo não numérico).
- Converte a entrada para inteiro e chama `eh_primo` para verificar se é primo.
- Imprime uma mensagem indicando se o número é primo ou não.

```python
if __name__ == "__main__":
    main()
```

- Garante que o código de teste rode apenas quando o arquivo é executado diretamente.
- Se o módulo for importado, `main()` não será executada automaticamente.

## Resumo

A refatoração melhora a legibilidade ao:
- adicionar docstring,
- separar a lógica de teste em `main()`,
- usar nomes de variáveis mais claros,
- e manter a mesma verificação eficiente de primalidade.
