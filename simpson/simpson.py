#escravos
def adiciona_ponto_medio(intervalo:tuple[float,float])->tuple[float,float,float]:
    ponto_medio = (intervalo[0]+intervalo[1]) / 2
    return intervalo[0],ponto_medio, intervalo[1]
def calcula_numero(number,polinomio):
    """
    calcula p(xi), baseado na tupla de coeficientes do polinomio 'polinomio'
    """
    return sum([coeficiente * number**indice for indice,coeficiente in enumerate(polinomio)])
def calcula_polinomio(polinomio:tuple, intervalo:tuple[float,float,float]) -> tuple:
    """
    recebe tupla coeficientes do pol p(x); tupla limites x1, x_med, x2.
    retorna uma tupla de três posições: (p(x1), p(x_med), p(x2))
    """
    return tuple(calcula_numero(numero,polinomio) for numero in intervalo)
#mestre
def simpson(intervalo: tuple[float, float], y=tuple(), polinomio=tuple()) -> float:
    """
    :param intervalo: tuple(float, float). Intervalo de integração no eixo x
    :param y: tuple(float,float,float). Imagem da função no ponto médio e limites
    :param polinomio: tuple(*float). Recebe os coeficientes do pol p(x)
    :return: área da curva.
    """
    intervalo = adiciona_ponto_medio(intervalo)
    assert type(polinomio) == tuple, 'argumento polinomio deve ser tipo tupla';
    if polinomio:
        y = calcula_polinomio(polinomio,intervalo)

    h     = (intervalo[2] - intervalo[0]) / 2
    area  = (h/3) * (y[0] + 4*y[1] + y[2])

    return area
