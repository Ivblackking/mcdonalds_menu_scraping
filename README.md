## Run with docker
### Scraping
`cd scraping`<br />
`docker build -t scrape .`<br />
`docker run -v .:/app scrape`<br />

### Api
`cd api`<br />
`docker build -t api .`<br />
`docker run -p 8000:8000 api`<br />