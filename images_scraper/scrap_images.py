"""Artists and songs images scraper"""

import random
import time

import requests
from bs4 import BeautifulSoup
from PIL import Image
from rembg import remove

headers = {
    "authority": "yandex.com",
    "method": "GET",
    "path": "/images/",
    "scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,ru;q=0.8",
    "cache-control": "max-age=0",
    "cookie": "mda=0; yandex_gid=10262; is_gdpr=0; is_gdpr_b=CIG7UxCPqAEoAg==; yandexuid=6924657541677069694; yuidss=6924657541677069694; i=hdSix32uBMFPgRwHxKStd8tNIRTOqiCv+YWMO3KX8NRr6B5RV8qDIm5NxmUd5j6DeS408TseIHouImjXLkZ4ALdZAxM=; yashr=6138973001677069694; my=YwA=; gdpr=0; _ym_uid=1677069697888978309; _ym_d=1677069697; ymex=1992429699.yrts.1677069699; _ym_isad=2; _yasc=yvv5DiUSNyJnPXE2EIqQK91hFq2nqbUTnFoniO9LDZl0DJF0olXvSXV6aNI5pZ2ZAmQnoKac; yp=1677674500.szm.1_25:1536x864:431x754#1679661695.ygu.1; cycada=cEwZ/ky3pU1SIEo1xN2eMohTtNKhRMFxV5MAhmKrsdE=",
    "device-memory": "8",
    "downlink": "10",
    "dpr": "1.25",
    "ect": "4g",
    "referer": "https://yandex.com/",
    "rtt": "50",
    "sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    "sec-ch-ua-arch": "x86",
    "sec-ch-ua-bitness": "64",
    "sec-ch-ua-full-version": "110.0.5481.104",
    "sec-ch-ua-full-version-list": '"Chromium";v="110.0.5481.104", "Not A(Brand";v="24.0.0.0", "Google Chrome";v="110.0.5481.104"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "Windows",
    "sec-ch-ua-platform-version": "5.0.0",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "viewport-width": "431",
}


def remove_background_image(input_path, name, count):
    """Removed Background"""

    output_path = f"media/images/{name}_{count}.png"
    input_ = Image.open(input_path)
    output = remove(input_)
    output.save(output_path)


def save_image(img_url, name, count, img_for):
    """Saved Image"""

    bytes_obj = requests.get(img_url)
    img_url = f'media/output/{name}_{count}.jpg'
    with open(img_url, 'wb') as image_f:
        image_f.write(bytes_obj.content)

    if img_for == "singer":
        remove_background_image(img_url, name, count)


def scrap_image(name, count, img_for):
    """Scraps Image"""
    
    name = name.replace(" ", "_")
    url = f'https://yandex.com/images/search?text={name}'
    time.sleep(random.randint(5, 15))
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    img_ = soup.find_all('img')
    if len(img_) >= 1:
        image = f"https:{soup.find_all('img')[1]['src']}"
    else:
        image = "https://avatars.mds.yandex.net/i?id=0112d8e2b4239d6701c8a6bea8309169d8fd7195-7598369-images-thumbs&n=13"

    save_image(image, name, count, img_for)
