import pandas as pd

def analisador_dados_demograficos():
    df = pd.read_csv("xxx")

    # Quantas pessoas de cada raça estão representadas neste conjunto de dados? (coluna raça)
    contagem_racas = df['race'].value_counts()

    # Qual é a idade média dos homens?
    idade_media_homens = df[df['sex'] == 'Male']['age'].mean()

    # Qual é a porcentagem de pessoas que possuem diploma de bacharel?
    porcentagem_bacharelado = (df['education'] == 'Bachelors').mean() * 100

    # Qual a porcentagem de pessoas com educação avançada (Bachelors, Masters, ou Doctorate) que ganham mais de 50 mil?
    educacao_avancada = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    ricos_educacao_avancada = (df[educacao_avancada & (df['salary'] == '>50K')].shape[0] / educacao_avancada.sum()) * 100

    # Qual a porcentagem de pessoas sem educação avançada que ganham mais de 50 mil?
    educacao_baixa = ~educacao_avancada
    ricos_educacao_baixa = (df[educacao_baixa & (df['salary'] == '>50K')].shape[0] / educacao_baixa.sum()) * 100

    # Qual é o número mínimo de horas que uma pessoa trabalha por semana?
    min_horas_trabalho = df['hours-per-week'].min()

    # Qual a porcentagem de pessoas que trabalham o número mínimo de horas por semana e têm um salário de mais de 50 mil?
    num_trabalhadores_minimos = df[df['hours-per-week'] == min_horas_trabalho]
    porcentagem_ricos = (num_trabalhadores_minimos[num_trabalhadores_minimos['salary'] == '>50K'].shape[0] / num_trabalhadores_minimos.shape[0]) * 100

    # Qual país tem a maior porcentagem de pessoas que ganham >50 mil e qual é essa porcentagem?
    pais_ricos = df[df['salary'] == '>50K'].groupby('native-country').size()
    total_pais = df.groupby('native-country').size()
    pais_maior_renda = (pais_ricos / total_pais * 100).idxmax()
    porcentagem_maior_renda_pais = (pais_ricos / total_pais * 100).max()

    # Identifique a ocupação mais popular para aqueles que ganham >50 mil na Índia.
    ocupacao_india = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    return {
        'contagem_racas': contagem_racas,
        'idade_media_homens': round(idade_media_homens, 1),
        'porcentagem_bacharelado': round(porcentagem_bacharelado, 1),
        'ricos_educacao_avancada': round(ricos_educacao_avancada, 1),
        'ricos_educacao_baixa': round(ricos_educacao_baixa, 1),
        'min_horas_trabalho': min_horas_trabalho,
        'porcentagem_ricos': round(porcentagem_ricos, 1),
        'pais_maior_renda': pais_maior_renda,
        'porcentagem_maior_renda_pais': round(porcentagem_maior_renda_pais, 1),
        'ocupacao_india': ocupacao_india
    }

resultado = analisador_dados_demograficos()
print(resultado)
