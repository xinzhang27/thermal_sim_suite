import asyncio

from nicegui import ui
import requests

username = 'tlaplace'
password = 'oLbQ8Z6AMUEaXyENbo5W'


def content() -> None:
    ui.label("使用标准API接口实现热管理材料数据的查询、上传和更新等功能")
    # Define your username and password

    # Define the API endpoint URL
    api_url = f'http://{username}:{password}@60.204.217.253/datamanage/material'

    # Create a httpx client session with basic authentication

    response = requests.get(api_url)
    data: dict = response.json()

    # ui.button('查询', on_click)

    @ui.refreshable
    def material_table() -> None:
        columns = [
            {'name': 'name', 'label': '热管理材料', 'field': 'name', 'required': True, 'align': 'left'},
            {'name': 'density', 'label': '密度/gcm^{-3}', 'field': 'density', 'sortable': True},
            {'name': 'thermal_conductivity', 'label': '热导率/Wm^{-1}K^{-1}', 'field': 'thermal_conductivity',
             'sortable': True},
            {'name': 'thermal_expansion', 'label': '热膨胀系数/ppmK^{-1}', 'field': 'thermal_expansion',
             'sortable': True},
        ]
        rows = [
            {'name': data['results'][i]['name'],
             'density': data['results'][i]['density'],
             'thermal_conductivity': data['results'][i]['thermal_conductivity'],
             'thermal_expansion': data['results'][i]['thermal_expansion_coefficient']} for i in
            range(len(data['results']))
        ]
        ui.table(columns=columns, rows=rows, row_key='name')

    def add_number() -> None:
        data = requests.get(api_url).json()
        print(data)
        material_table.refresh()

    material_table()
    ui.button('查询数据', on_click=add_number)
