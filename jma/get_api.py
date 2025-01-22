import requests

# 例：東京の地域コード（130000）
region_code = '130000'

# URLを構築
url = f'https://www.jma.go.jp/bosai/forecast/data/forecast/{region_code}.json'

response = requests.get(url)

# ステータスコードを確認
print("Status Code:", response.status_code)

# レスポンスの内容をテキスト形式で表示
print("Response Text:", response.text)

# ステータスコードが200の場合にJSONデータを取得して表示
if response.status_code == 200:
    try:
        data_json = response.json()
        print("JSON Data:", data_json)
    except requests.exceptions.JSONDecodeError:
        print("Error: Received data is not JSON")
else:
    print("Error: ", response.text)