import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.express as px
import seaborn as sns
import base64
from io import BytesIO

def plot_to_base64(plt):
    '''Funció per convertir els gràfics en format base64 per a la visualització a la web'''
    img = BytesIO()
    plt.savefig(img, format='png')
    # plt.close()
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode()

def __draw_plot():
    '''Transforma el gràfic en una imatge.'''
    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return plot_url


def demo_plot():
    '''Carrega un gràfic de prova del dataframe del Titanic. '''
    titanic_df = sns.load_dataset("titanic")
    print(titanic_df.head())
    # Another way to visualize the data is to use FacetGrid to plot multiple kedplots on one plot
    fig = sns.FacetGrid(titanic_df, hue="sex", aspect=4)
    fig.map(sns.kdeplot, 'age', fill=True)
    new_plot = titanic_df['age'].max()
    fig.set(xlim=(0, new_plot))
    fig.add_legend()
    plot_url = __draw_plot()
    return plot_url


def map1(df):
    '''Gràfic mapa.'''
    # Seleccionem els casos de xarampió = MEASLES.
    df_map = df.query("DISEASE == 'MEASLES'")
    df_map = df_map.sort_values(by=['YEAR','INCIDENCE_RATE'], ascending = [True, False])
    

    # Crea el mapa de cloropets
    fig = px.choropleth(df_map,
                        locations='CODE',  # Nom del país
                        locationmode='ISO-3',  # Mode de localització per noms de país [ISO-3, country names]
                        hover_name='NAME',  # Informació que apareixerà en la caixa d'eines en fer hover
                        color='INCIDENCE_RATE',  # Variable a representar amb colors
                        color_continuous_scale=px.colors.sequential.Reds,
                        animation_frame='YEAR',
                        title='Mapa casos de Xarampió als països'
                    )

    # Mostra el mapa
    fig.update_layout(margin=dict(l=20,r=0,b=0,t=70,pad=0),paper_bgcolor="white",height= 700,font_size=18)
    return fig