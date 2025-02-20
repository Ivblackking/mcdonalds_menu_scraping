from scrapers import McMenuScarper


def main():
    mc_scraper = McMenuScarper(size=5)
    mc_scraper.run_scraping()


if __name__ == "__main__":
    main()