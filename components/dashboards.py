from dash import html, dcc
from dash.dependencies import Input, Output, State
from datetime import date, datetime, timedelta
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import calendar
from globals import *
from app import app

card_icon = {
    'color':'white',
    'textAlign': 'center',
    'fontSize': 30,
    'margin': 'auto'
}

# =========  Layout  =========== #
layout = dbc.Col([
        # Saldo / Receita / Despesa        
        dbc.Row([
            # Saldo
            dbc.Col([
                dbc.CardGroup([
                    dbc.Card([
                        html.Legend('Saldo'),
                        html.H5('R$ 5.000', id='p-saldo-dashboards', style={})
                    ], style={'padding-left': '20px', 'padding-top': '10px'}),
                    dbc.Card(
                        html.Div(className='fa fa-university', style=card_icon),
                        color='warning',
                        style={'maxWidth': 75, 'height': 100, 'margin-left': '-10px'}
                    )
                ])
            ], width=4),

            # Receita
            dbc.Col([
                dbc.CardGroup([
                    dbc.Card([
                        html.Legend('Receita'),
                        html.H5('R$ 15.000', id='p-receita-dashboards', style={})
                    ], style={'padding-left': '20px', 'padding-top': '10px'}),
                    dbc.Card(
                        html.Div(className='fa fa-smile-o', style=card_icon),
                        color='success',
                        style={'maxWidth': 75, 'height': 100, 'margin-left': '-10px'}
                    )
                ])
            ], width=4),

            # Despesa
            dbc.Col([
                dbc.CardGroup([
                    dbc.Card([
                        html.Legend('Despesa'),
                        html.H5('R$ 10.000', id='p-despesa-dashboards', style={})
                    ], style={'padding-left': '20px', 'padding-top': '10px'}),
                    dbc.Card(
                        html.Div(className='fa fa-meh-o', style=card_icon),
                        color='danger',
                        style={'maxWidth': 75, 'height': 100, 'margin-left': '-10px'}
                    )
                ])
            ], width=4)
        ], style={'margin-top': 30}),

        # Filtro de Lançamento
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    html.Legend('Filtrar Lançamentos', className='card-title'),

                    # Receitas
                    html.Label('Categoria das Receitas'),
                    html.Div(
                        dcc.Dropdown(
                            id='dropdown-receita',
                            clearable=False,
                            style={'width': '100%'},
                            persistence=True,
                            persistence_type='session',
                            multi=True
                        )
                    ),

                    # Despesas
                    html.Label('Categoria das Despesas'),
                    html.Div(
                        dcc.Dropdown(
                            id='dropdown-despesas',
                            clearable=False,
                            style={'width': '100%'},
                            persistence=True,
                            persistence_type='session',
                            multi=True
                        )
                    ),

                    # Período de Análise
                    html.Legend("Período de Análise", style={"margin-top": "10px"}),    
                    dcc.DatePickerRange(
                        month_format='Do MMM, YY',
                        end_date_placeholder_text='Data...',
                        start_date=datetime.today(),
                        end_date=datetime.today() + timedelta(days=31),
                        with_portal=True,
                        updatemode='singledate',
                        id='date-picker-config',
                        style={'z-index': '100'}
                    ),
                ])
            ], width=4)
        ])
    ])



# =========  Callbacks  =========== #
