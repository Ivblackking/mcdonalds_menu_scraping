import json
import requests
import aiohttp
import asyncio
from bs4 import BeautifulSoup


class BaseScraper:
    menu_url = "https://www.mcdonalds.com/ua/uk-ua/eat/fullmenu.html"
    
    def __init__(self, size:int|None = None):
        self.size = size

    def get_item_url(self, item_id:str):
        return f"https://www.mcdonalds.com/dnaapp/itemDetails?country=UA&language=uk&showLiveData=true&item={item_id}"

    def get_item_ids(self):
        item_ids = []
        menu_page = requests.get(self.menu_url)
        menu_soup = BeautifulSoup(menu_page.content, 'html.parser')

        item_selector = "#maincatcontent ul.cmp-category__row li"
        items = menu_soup.select(item_selector)

        for item in items:
            item_id = item.get("data-product-id")
            item_ids.append(item_id)
        
        return item_ids
    
    def get_item_details_from_data(self, data:dict):
        details = {}
        item = data["item"]

        details["name"] = item["item_name"]
        details["description"] = item["description"]

        extra_fields = {
            2: "calories",
            3: "fats",
            5: "carbs",
            7: "proteins",
            4: "unsaturated fats",
            6: "sugar",
            8: "salt"
        }

        for index, field in extra_fields.items():
            obj = item["nutrient_facts"]["nutrient"][index]
            details[field] = f'{obj["value"]} {obj["uom"]} ({obj["adult_dv"]} % DV)'

        portion_obj = item["nutrient_facts"]["nutrient"][0]
        details["portion"] = f'{portion_obj["value"]} {portion_obj["uom"]}'

        return details


class McMenuScraper(BaseScraper):    
    def get_item_details(self, item_id:str):
        item_url = self.get_item_url(item_id)
        response = requests.get(item_url)
        data:dict = json.loads(response.content)
        details = self.get_item_details_from_data(data)
        return details
    
    def get_all_items(self):
        all_items = []
        item_ids = self.get_item_ids()
        item_ids = item_ids[:self.size] if self.size else item_ids

        for i, item_id in enumerate(item_ids):
            item = self.get_item_details(item_id)
            all_items.append(item)
            # print(f"{i+1} item: ", item_id)

        return all_items
    
    def run_scraping(self):
        all_items = self.get_all_items()
        with open("mc_menu_data.json", "w", encoding="utf8") as file:
            json.dump(all_items, file, indent=4, ensure_ascii=False)


class AsyncMcMenuScraper(BaseScraper):
    async def aget_item_details(self, item_id:str):
        details = {}
        item_url = self.get_item_url(item_id)
        async with aiohttp.ClientSession() as session:
            async with session.get(item_url) as resp:
                data = await resp.json()
                details = self.get_item_details_from_data(data)
                # print(f"item: ", item_id)
                return details
    
    async def aget_all_items(self):
        item_ids = self.get_item_ids()
        item_ids = item_ids[:self.size] if self.size else item_ids

        item_tasks = []
        for item_id in item_ids:
            task = asyncio.create_task(self.aget_item_details(item_id))
            item_tasks.append(task)
        all_items = await asyncio.gather(*item_tasks)

        return all_items
    
    async def arun_scraping(self):
        all_items = await self.aget_all_items()
        with open("mc_menu_data.json", "w", encoding="utf8") as file:
            json.dump(all_items, file, indent=4, ensure_ascii=False)
