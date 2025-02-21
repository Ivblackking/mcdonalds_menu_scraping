## The idea of the solution
The McDonald's menu https://www.mcdonalds.com/ua/uk-ua/eat/fullmenu.html has a hidden API.<br />
It is https://www.mcdonalds.com/dnaapp/itemDetails?country=UA&language=uk&showLiveData=true&item={item_id}<br />
We can find it by opening the dev tools in the browser and look at the Network tab. If we check the json responses we can find that API.<br />
So if we collect all ids of the menu items from the main page of the menu we will be able to collect information about each item using that API.

## Run with docker
### Requirements
- Docker (https://www.docker.com/)
### Scraping
Run the terminal in the root directory of the project and execute the next commands: <br />
`cd scraping`<br />
`docker build -t scrape .`<br />
`docker run -v .:/app scrape`<br />
The result will be stored in the file `mc_menu_data_for_api.json"`. <br />
To try the async version of the scraper comment line 8 and uncomment line 9 in the appropriate Dockerfile and rebuild the docker image.

### Api
Run the terminal in the root directory of the project and execute next commands: <br />
`cd api`<br />
`docker build -t api .`<br />
`docker run -p 8000:8000 api`<br />
After that the api will be available by the address `http://127.0.0.1:8000` or `http://127.0.0.1:8000/docs`

## Run without docker
### Requirements
- Python 3.11 (https://www.python.org/)
- OS Windows 11 (recommended)
### Running instruction
1. Create virtual env: `py -3.11 -m virtualenv venv` (for Linux the command will be different)
2. Install required packeges: `pip install -r requirements.txt`
3. Run sync version of the scraper: `cd scraping` and `python main.py`
4. To run async version of the scraper do: `cd scraping` and `python async_main.py`
5. To run the api: `cd api` and `uvicorn main:app --reload`
6. The api will be available by the address `http://127.0.0.1:8000`
