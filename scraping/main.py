from scrapers import McMenuScraper
from utils import time_delta


@time_delta
def main():
    mc_scraper = McMenuScraper()
    mc_scraper.run_scraping()


if __name__ == "__main__":
    main()