import asyncio
from scrapers import AsyncMcMenuScraper
from utils import time_delta


@time_delta
def async_main():
    amc_scraper = AsyncMcMenuScraper()
    asyncio.run(amc_scraper.arun_scraping())


if __name__ == "__main__":
    async_main()