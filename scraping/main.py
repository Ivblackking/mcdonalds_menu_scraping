from scrapers import McMenuScarper


def main():
    mc_scraper = McMenuScarper()
    mc_scraper.run_scraping()


if __name__ == "__main__":
    main()