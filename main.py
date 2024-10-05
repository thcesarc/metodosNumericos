from simpson import simpson as s
def teste_valores_definidos():
    intervalo = 1, 10
    imagem = 4, 33.25, 103
    return s.simpson(intervalo, y=imagem)
def teste_limites_polinomio():
    intervalo = 1, 10
    polinomio = 3,0,1
    return s.simpson(intervalo, polinomio=polinomio)

def main():
    #teste do módulo para valores definidos (x,f(x)) fornecidos pelo usuário
    print("Resultado do algorítmo: ", teste_valores_definidos())
    print('Valor analítico esperado: integral de 1 a 10 de x^2 + 3 = 360')

    #teste do módulo para limites e polinomio definido
    print("Resultado do algorítmo: ", teste_limites_polinomio())
    print('Valor analítico esperado: integral de 1 a 10 de x^2 + 3 = 360')






if __name__ == '__main__':
    main()
