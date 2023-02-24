"""Artists and songs scraper"""


from singer.models import Singer
from music.models import Music
from images_scraper.scrap_images import scrap_image
import asyncio
import aiohttp
from pprint import pprint
from bs4 import BeautifulSoup
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "play_project.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"


django.setup()


class Scraper:
    """Scraps information from site."""

    COUNT = 0

    def __init__(self, url):
        self.url = url
        self.event_loop = asyncio.new_event_loop()
        self.tasks = [self.event_loop.create_task(self.async_parse())]
        self.event_loop.run_until_complete(asyncio.wait(self.tasks))

    async def async_parse(self):
        """Sends a request to the site."""

        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as req:
                data = await req.text()
                self.async_parse_data(data)

    def async_parse_data(self, data):
        """Gets an artist"""

        soup = BeautifulSoup(data, 'lxml')
        table = soup.find('table', {'class': 'music'})
        table_tr = table.find_all('tr', {'class': ''})

        td_list = [tr.find_all('td')[1:] for tr in table_tr]

        for td in td_list[241:]:
            audio = f'https://cs.uwaterloo.ca/~dtompkin/music{td[0].find("audio")["src"][2:]}'
            artist_name = td[1].text
            song_name = td[2].text
            song_year = td[5].text
            song_genre = td[6].text

            Scraper.COUNT += 1

            scrap_image(artist_name, Scraper.COUNT, "singer")
            scrap_image(f'{artist_name} {song_name}', Scraper.COUNT, "song")

            singer = Singer.objects.create(
                name=f"{artist_name}", image=f"images/{artist_name}_{Scraper.COUNT}.png")
            music = Music.objects.create(name=f"{song_name}", genre=f"{song_genre}", audio=f"{audio}", year=int(
                song_year), image=f"output/{artist_name}_{song_name}_{Scraper.COUNT}.jpg")
            music.singer.add(singer)


def main():
    scraper = Scraper(
        'https://cs.uwaterloo.ca/~dtompkin/music/list/Best5.html')


if __name__ == "__main__":
    main()
