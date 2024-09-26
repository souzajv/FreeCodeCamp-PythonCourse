import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np  

df = pd.read_csv('medical_examination.csv')

df['sobrepeso'] = (df['weight'] / ((df['height'] / 100) ** 2)) > 25
df['sobrepeso'] = df['sobrepeso'].astype(int)
df['colesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['glicose'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

def desenhar_grafico_categoria():
    df_categoria = pd.melt(df, id_vars=["cardio"], value_vars=["colesterol", "glicose", "fumar", "alco", "atividade", "sobrepeso"])
    
    df_categoria = df_categoria.groupby(["cardio", "variavel", "valor"]).size().reset_index(name='contagem')
    
    df_categoria.rename(columns={"valor": "condicao"}, inplace=True)
    
    fig = sns.catplot(data=df_categoria, x="condicao", y="contagem", hue="variavel", col="cardio", 
                      kind="bar", height=4, aspect=.7)
    
    return fig

df_matriz = df[
    (df['ap_lo'] <= df['ap_hi']) &
    (df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] <= df['height'].quantile(0.975)) &
    (df['weight'] >= df['weight'].quantile(0.025)) &
    (df['weight'] <= df['weight'].quantile(0.975))
]

corr = df_matriz.corr()

mask = np.triu(np.ones_like(corr, dtype=bool))

plt.figure(figsize=(12, 8))

sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})


plt.show()

if __name__ == "__main__":
    desenhar_grafico_categoria()
