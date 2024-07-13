import requests

NOTION_TOKEN = 'secret_i1TUDwEmdNO1bxWidMi2RIJzdo9qfUEVp8E6NtMX7dk'
DATABASE_ID = ''

url = f'https://api.notion.com/v1/blocks/6f5322e3c1a44b22832bffe39d83e75e/children'
headers = {
    'Authorization': f'Bearer {NOTION_TOKEN}',
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28',
}

notion_data = {
	"children": [
		{
			"object": "block",
			"type": "paragraph",
			"paragraph": {
				"rich_text": [
					{
						"type": "text",
						"text": {
							"content": "Hello World"
						}
					}
				]
			}
		}
	]
}

response = requests.patch(url, headers=headers, json=notion_data)

if response.status_code == 200:
    print("Страница успешно создана в Notion!")
else:
    print(f"Ошибка при создании страницы. Код ответа: {response.status_code}, Текст ответа: {response.text}")
    