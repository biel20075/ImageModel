def eh_primo(n: int) -> bool:
    """Retorna True se n for primo, caso contrário False."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    divisor = 5
    while divisor * divisor <= n:
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor += 6

    return True


def main() -> None:
    try:
        numero = int(input("Digite um número inteiro: "))
        if eh_primo(numero):
            print(f"{numero} é primo.")
        else:
            print(f"{numero} não é primo.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")


if __name__ == "__main__":
    main()