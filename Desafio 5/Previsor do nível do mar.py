import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def prever_nivel_do_mar():
    dados = pd.read_csv("epa-sea-level.csv")

    plt.figure(figsize=(10, 6))  
    plt.scatter(dados['Year'], dados['CSIRO Adjusted Sea Level'], color='blue', label='Dados de Nível do Mar')  # Gráfico de dispersão

    regressao_total = linregress(dados['Year'], dados['CSIRO Adjusted Sea Level'])
    inclinação_total = regressao_total.slope 
    intercepto_total = regressao_total.intercept  

    anos_totais = pd.Series(range(1880, 2051))  
    niveis_totais = inclinação_total * anos_totais + intercepto_total  

    plt.plot(anos_totais, niveis_totais, color='red', label='Linha de Melhor Ajuste Total')  

    dados_2000 = dados[dados['Year'] >= 2000]  
    regressao_2000 = linregress(dados_2000['Year'], dados_2000['CSIRO Adjusted Sea Level'])
    inclinação_2000 = regressao_2000.slope  
    intercepto_2000 = regressao_2000.intercept  

    anos_2000 = pd.Series(range(2000, 2051)) 
    niveis_2000 = inclinação_2000 * anos_2000 + intercepto_2000  

    plt.plot(anos_2000, niveis_2000, color='green', label='Linha de Melhor Ajuste a Partir de 2000') 

    plt.title('Aumento do Nível do Mar')  
    plt.xlabel('Ano')  
    plt.ylabel('Nível do Mar (polegadas)') 
    plt.legend()  

    plt.savefig('nivel_do_mar.png')  
    plt.show()  

if __name__ == "__main__":
    prever_nivel_do_mar()
