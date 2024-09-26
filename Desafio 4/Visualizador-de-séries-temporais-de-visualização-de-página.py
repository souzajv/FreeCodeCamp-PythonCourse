import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def draw_line_plot():
    df = pd.read_csv("fcc-forum-pageviews.csv")
    
    limite_inferior = df['value'].quantile(0.025)
    limite_superior = df['value'].quantile(0.975)
    df_limpo = df[(df['value'] >= limite_inferior) & (df['value'] <= limite_superior)]
    
    plt.figure(figsize=(10, 5))
    plt.plot(df_limpo.index, df_limpo['value'], color='blue')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('date')
    plt.ylabel('page views')
    plt.xticks(rotation=45) 
    plt.tight_layout() 
    plt.savefig('line_plot.png') 
    plt.show()  

def draw_bar_plot():
    df = pd.read_csv("fcc-forum-pageviews.csv", index_col='date', parse_dates=True)
    
    limite_inferior = df['value'].quantile(0.025)
    limite_superior = df['value'].quantile(0.975)
    df_limpo = df[(df['value'] >= limite_inferior) & (df['value'] <= limite_superior)]
    
    df_limpo['ano'] = df_limpo.index.year
    df_limpo['mes'] = df_limpo.index.month_name()
    
    df_media = df_limpo.groupby(['ano', 'mes'])['value'].mean().unstack()
    
    plt.figure(figsize=(10, 5))
    df_media.plot(kind='bar', ax=plt.gca())
    plt.title('Average Page Views per Month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    plt.tight_layout()  
    plt.savefig('bar_plot.png')  
    plt.show()  

def draw_box_plot():
    df = pd.read_csv("fcc-forum-pageviews.csv", index_col='date', parse_dates=True)
    
    limite_inferior = df['value'].quantile(0.025)
    limite_superior = df['value'].quantile(0.975)
    df_limpo = df[(df['value'] >= limite_inferior) & (df['value'] <= limite_superior)]
    
    df_limpo['ano'] = df_limpo.index.year
    df_limpo['mes'] = df_limpo.index.month

    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    sns.boxplot(x='ano', y='value', data=df_limpo)
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')

    plt.subplot(1, 2, 2) 
    sns.boxplot(x='mes', y='value', data=df_limpo)
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    
    plt.tight_layout() 
    plt.savefig('box_plot.png') 
    plt.show()  

draw_line_plot()
draw_bar_plot()
draw_box_plot()
