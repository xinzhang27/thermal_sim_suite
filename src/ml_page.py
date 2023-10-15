from nicegui import ui
from random import random


def content() -> None:
    with ui.grid(columns=2):
        ui.upload(label="Input Data")
        echart = ui.echart({
            'xAxis': {'type': 'value'},
            'yAxis': {'type': 'category', 'data': ['A', 'B'], 'inverse': True},
            'legend': {'textStyle': {'color': 'gray'}},
            'series': [
                {'type': 'bar', 'name': 'Alpha', 'data': [0.1, 0.2]},
                {'type': 'bar', 'name': 'Beta', 'data': [0.3, 0.4]},
            ],
        })

        def update():
            echart.options['series'][0]['data'][0] = random()
            echart.update()

    with ui.row():
        with ui.column():
            ui.label('Supervised Learning')
            ui.radio(['Linear Regression', 'Logistic Regression', 'SVM', 'Decision Tree', 'Random Forest'],
                     value='Linear Regression')
        with ui.column():
            # data analysis methods
            ui.label('Unsupervised Learning')
            ui.radio(['K-means', 'DBSCAN', 'Hierarchical Clustering'], value='K-means')
        with ui.column():
            # data analysis methods
            ui.label('Cross Validation')
            ui.radio(['K-fold', 'Leave One Out', 'Leave P Out'], value='K-fold')

    ui.button('Train', on_click=update)
    ui.button('Show Result', on_click=update)
