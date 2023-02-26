import numpy as np
from datetime import datetime


def bisection(f, a, b, tol, max_it, filename):
    # Iniciando tabela
    if filename is not None:
        with open(filename, "w") as f_out:
            f_out.write(f"Iteracao\t\t x\n")
            f_out.write(f"{0}\t\t{(a + b) / 2:.8f}\n")

    # Checando intervalo
    if f(a) * f(b) > 0:
        print("Intervalo inválido. Tente novamente.")
        with open(filename, "w") as f_out:
            f_out.write("Intervalo inválido. Tente novamente.")
        return

    # Inicializando ponto medio
    c = (a + b) / 2
    n_iter = 0

    # Loopando ate tolerância ser encontrada ou numero maximo de iteracoes alcancado
    while abs(f(c)) > tol and n_iter < max_it:
        # Atualizando a e b baseado no sinal de f(c)
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        # Atualizando ponto medio e iteracoes
        c = (a + b) / 2
        n_iter += 1

        # Adicionando à tabela
        with open(filename, "a") as f_out:
            f_out.write(f"{n_iter+1}\t\t{c:.8f}\n")

        # Retornando raiz aproximada
    return c


def MIL(f, x0, tol, max_it, filename):
    x = x0

    # Iniciando tabela
    if filename is not None:
        with open(filename, "w") as f_out:
            f_out.write(f"Iteracao\t\t x\n")
            f_out.write(f"{0}\t\t{x:.8f}\n")

    # Itera a funcao no maximo max_it vezes
    for n in range(max_it):
        try:
            x_new = f(x)
        except OverflowError:
            print("O metodo tendeu ao infinito.")
            with open(filename, "a") as f_out:
                f_out.write(
                    f"O metodo tendeu ao infinito.\n"
                )
            return
        else:
            if abs(x_new - x) < tol:
                return x_new
            x = x_new
            # Adicionando à tabela
            if filename is not None:
                with open(filename, "a") as f_out:
                    f_out.write(f"{n+1}\t\t{x:.8f}\n")

    if filename is not None:
        with open(filename, "a") as f_out:
            f_out.write(
                f"O metodo nao convergiu dentro do numero maximo de iteracoes.\n"
            )
    print("O metodo nao convergiu dentro do numero maximo de iteracoes.")


def newton_raphson(f, df, x0, tol, max_it, filename):

    x = x0

    # Iniciando tabela
    if filename is not None:
        with open(filename, "w") as f_out:
            f_out.write(f"Iteracao\t\t x\n")
            f_out.write(f"{0}\t\t{x:.8f}\n")

    # Itera a funcao no maximo max_it vezes
    for n in range(max_it):
        fx = f(x)
        if abs(fx) < tol:
            return x
        dfx = df(x)
        if dfx == 0:
            if filename is not None:
                with open(filename, "a") as f_out:
                    f_out.write(f"Derivada zero. O metodo nao convergiu.\n")
            raise ValueError("Derivada zero. O metodo nao convergiu.")
        x -= fx / dfx

        # Adicionando à tabela
        if filename is not None:
            with open(filename, "a") as f_out:
                f_out.write(f"{n+1}\t\t{x:.8f}\n")

    if filename is not None:
        with open(filename, "a") as f_out:
            f_out.write(
                f"O metodo nao convergiu dentro do numero maximo de iteracoes.\n"
            )
    raise ValueError("O metodo nao convergiu dentro do numero maximo de iteracoes.")


def secante(f, x0, x1, tol, max_it, filename):

    f0 = f(x0)
    f1 = f(x1)
    iter_num = 0
    with open(filename, "w") as f_out:
        f_out.write("Iteracao\t\tX\n")
        while abs(f1) > tol and iter_num < max_it:
            delta_x = f1 * (x1 - x0) / (f1 - f0)
            x = x1 - delta_x
            iter_num += 1
            f_out.write("{0}\t\t\t{1}\n".format(iter_num, x))
            x0, x1 = x1, x
            f0, f1 = f1, f(x1)
        if iter_num >= max_it:
            f_out.write("Numero maximo de iteracoes excedido.")
            print("Numero maximo de iteracoes excedido.")
        return x


def regula_falsi(f, a, b, tol, max_it, filename):
    fa = f(a)
    fb = f(b)
    iter_num = 0
    with open(filename, "w") as f_out:
        f_out.write("Iteracao\t\tX\n")
        while abs(fb) > tol and iter_num < max_it:
            x = (a * fb - b * fa) / (fb - fa)
            fx = f(x)
            iter_num += 1
            f_out.write("{0}\t\t\t{1}\n".format(iter_num, x))
            if fa * fx < 0:
                b = x
                fb = fx
            else:
                a = x
                fa = fx
        if iter_num >= max_it:
            f_out.write("Numero maximo de iteracoes excedido.")
            print("Numero maximo de iteracoes excedido.")
        return x


now = datetime.now()

filename = "Resultados"


def f(x):
    return 6 * x**2 - 5 * x + 1


def df(x):
    return 12 * x - 5


while True:
    print("Bem vindo. Selecione o metodo desejado.\n")
    print("[1]: Bisseccao\n")
    print("[2]: MIL (Ponto Fixo)\n")
    print("[3]: Newton-Raphson\n")
    print("[4]: Secante\n")
    print("[5]: Regula-Falsi\n")
    print("[6]: Parar execucao\n")

    choice = input("Digite sua escolha (1-6): ")
    if choice == "1":
        print("Bisseccao")
        a = float(input("Valor de a: "))
        b = float(input("Valor de b: "))
        tol = float(input("Precisao: "))
        max_it = int(input("Maximo de iteracoes: "))
        print(bisection(f, a, b, tol, max_it, filename))
        print("\n\n\n")

    elif choice == "2":
        print("MIL")
        x = float(input("Chute inicial: "))
        tol = float(input("Precisao: "))
        max_it = int(input("Maximo de iteracoes: "))
        print(MIL(f, x, tol, max_it, filename))
        print("\n\n\n")

    elif choice == "3":
        print("Newton-Raphson")
        x = float(input("Chute inicial: "))
        tol = float(input("Precisao: "))
        max_it = int(input("Maximo de iteracoes: "))
        print(newton_raphson(f, df, x, tol, max_it, filename))
        print("\n\n\n")

    elif choice == "4":
        print("Secante")
        x0 = float(input("x0: "))
        x1 = float(input("x1: "))
        tol = float(input("Precisao: "))
        max_it = int(input("Maximo de iteracoes: "))
        print(secante(f, x0, x1, tol, max_it, filename))
        print("\n\n\n")

    elif choice == "5":
        print("Regula-Falsi")
        a = float(input("a: "))
        b = float(input("b: "))
        tol = float(input("Precisao: "))
        max_it = int(input("Maximo de iteracoes: "))
        print(regula_falsi(f, a, b, tol, max_it, filename))
        print("\n\n\n")

    elif choice == "6":
        print("Execucao encerrada.")
        break

    else:
        print("Escolha invalida. Tente novamente.")
