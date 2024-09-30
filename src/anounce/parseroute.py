
# Standard Library
from os import getenv

# Third Party Stuff
import requests

# My Stuff
from src.anounce.parse_result import ParseResult


class NotionDataFetcher:
    def __init__(self, api_token, database_id):
        self.api_token = api_token
        self.database_id = database_id
        self.base_url = f"https://api.notion.com/v1/databases/{self.database_id}/query"
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }

    def fetch_data(self)-> list:
        # Фильтрация по непустым датам
        payload = {
            "filter": {
                "property": "Date",
                "date": {
                    "is_not_empty": True  # Фильтрация на непустые даты
                }
            },
            "sorts": [
                {
                    "property": "Date",
                    "direction": "ascending"  # Сортировка по дате
                }
            ]
        }

        response = requests.post(self.base_url, headers=self.headers, json=payload)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data: {response.status_code} - {response.text}")


        # json to dict
        response_dict = response.json()
        calendar_records = response_dict.get("results", [])
        for calendar_record in calendar_records:
            props = calendar_record.get("properties", {})
            start_date = props.get("Date", {}).get("date", {}).get("start")



        ParseResult = self.extract_links(response.json())
        return ParseResult    

    def extract_links(self, data: dict) -> list: 
        links = []
        for result in data.get("results", []):
            # Извлекаем ссылку из результат а
            links.append(result['url'])  # Получаем ссылку на страницу
        return links

def parse_route(route):
    api_token = getenv('NOTION_API_TOKEN')
    database_id = getenv('NOTION_DATABASE_ID')
    fetcher = NotionDataFetcher(api_token, database_id)
    route_data = fetcher.fetch_data()
    return route_data

