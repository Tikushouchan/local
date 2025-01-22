import flet as ft
import requests
import json

# JSONデータをファイルから読み込む
with open('jma/areas.json', 'r', encoding='utf-8') as f:
    data_json = json.load(f)

# 天気情報表示用のラベル（グローバルスコープで定義）
weather_label = ft.Text()

class CustomExpansionTile(ft.UserControl):
    def __init__(self, title, area_code=None, children=None):
        super().__init__()
        self.title = title
        self.area_code = area_code
        self.children = children if children else []
        self.expanded = False

    def build(self):
        self.children_column = ft.Column(
            controls=self.children,
            visible=self.expanded
        )
        self.expand_icon = ft.Icon(ft.icons.EXPAND_MORE)

        list_tile = ft.ListTile(
            title=ft.Text(self.title),
            trailing=self.expand_icon,
            on_click=self.toggle_expand,
            data=self.area_code
        )

        return ft.Column(
            controls=[
                list_tile,
                self.children_column
            ]
        )

    def toggle_expand(self, e):
        self.expanded = not self.expanded
        self.children_column.visible = self.expanded
        self.expand_icon.name = ft.icons.EXPAND_LESS if self.expanded else ft.icons.EXPAND_MORE
        self.update()
        if not self.expanded:
            on_office_click(e, self.area_code)

def fetch_weather(area_code):
    url = f'https://www.jma.go.jp/bosai/forecast/data/forecast/{area_code}.json'
    response = requests.get(url)

    # デバッグのためリクエストURLとステータスコードを出力
    print(f'Request URL: {url}')
    print(f'Status Code: {response.status_code}')

    if response.status_code == 200:
        try:
            data_json = response.json()
            forecast = data_json[0]['timeSeries'][0]['areas'][0]['weathers'][0]
            return forecast
        except (IndexError, KeyError, json.JSONDecodeError):
            return "Error: Invalid JSON structure"
    else:
        return f"Error: {response.status_code} - {response.text}"

def on_office_click(e, area_code=None):
    if area_code is None:
        area_code = e.control.data
    weather = fetch_weather(area_code)
    weather_label.value = weather
    weather_label.update()

def build_tiles(root_code, all_areas):
    stack = [(root_code, None, None)]  # (current_code, parent_tile, child_controls)
    tiles = []

    while stack:
        current_code, parent_tile, children = stack.pop()
        current_data = all_areas[current_code]
        children_controls = []

        # Create the tile for the current area
        tile = CustomExpansionTile(
            title=current_data['name'],
            area_code=current_code
        )

        tile_control = tile.build()
        list_tile = tile_control.controls[0]
        list_tile.on_click = on_office_click
        
        # Stack children to be processed
        for child_code in reversed(current_data.get('children', [])):
            if child_code in all_areas:
                stack.append((child_code, tile_control, children_controls))

        if parent_tile:
            parent_tile.controls[1].controls.append(tile_control)
        else:
            tiles.append(tile_control)

    return tiles

def main(page: ft.Page):
    area_tiles = []

    # すべての地域データを統合
    all_areas = data_json.get('offices', {})
    all_areas.update(data_json.get('classes10s', {}))
    all_areas.update(data_json.get('classes20s', {}))

    # centersの情報を基に親タイルを作成し、それに直属のareasを子タイルとして含める
    centers_data = data_json.get('centers', {})
    
    for center_code, center_data in centers_data.items():
        tiles = build_tiles(center_code, all_areas)
        area_tiles.extend(tiles)

    # デバッグのためにタイル名を表示
    for t in area_tiles:
        print(t.controls[0].title.value)

    # ListViewでスクロール可能にする
    scrollable_list = ft.ListView(controls=area_tiles, expand=True)

    # ページに天気情報表示ラベルを追加
    page.add(scrollable_list)
    page.add(weather_label)

# Fletアプリケーションを実行
ft.app(target=main)