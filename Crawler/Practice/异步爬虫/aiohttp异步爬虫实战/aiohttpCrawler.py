# -*- coding: utf-8 -*-
# @Time    : 2021/10/14 14:49
# @Author  : wanghc
# @File    : aiohttpCrawler.py
# @Software: PyCharm

import aiohttp
import asyncio
import logging
import json
from motor.motor_asyncio import AsyncIOMotorClient

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
INDEX_URL = 'https://dynamic5.scrape.center/api/book/?limit=18&offset={offset}'
DETAIL_URL = 'https://dynamic5.scrape.center/api/book/{id}'
PAGE_SIZE = 18
PAGE_NUMBER = 10
CONCURRENCY = 5

semaphore = asyncio.Semaphore(CONCURRENCY)
MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'books'
MONGO_COLLECTION_NAME = 'books'
client = AsyncIOMotorClient(MONGO_CONNECTION_STRING)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]


async def scrape_api(url):
    '''
    :param url: url
    :return: 返回json对象
    '''
    async with semaphore:
        try:
            logging.info('scraping %s', url)
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    return await response.json()
        except aiohttp.ClientError:
            logging.error('error occurred while scraping %s', url)


async def scrape_index(page):
    '''
    :param page: 列表页的页数
    :return: 列表页返回的json对象
    '''
    url = INDEX_URL.format(offset=PAGE_SIZE * (page - 1))
    return await scrape_api(url)


async def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    data = await scrape_api(url)
    await save_data(data)


async def save_data(data):
    '''
    :param data:
    :return: 将data存储到mongodb
    '''
    logging.info('saving data %s', data)
    if data:
        return await collection.update_one(
            {'id': data.get('id')}, {'$set': data}, upsert=True
        )


async def main():
    scrape_index_tasks = [asyncio.ensure_future(scrape_index(page)) for page in range(1, PAGE_NUMBER + 1)]
    results = await asyncio.gather(*scrape_index_tasks)
    # logging.info('results', json.dumps(results, ensure_ascii=False, indent=2))
    ids = []
    for index_data in results:
        if not index_data: continue
        for item in index_data.get('results'):
            ids.append(item.get('id'))
    scrape_detail_tasks = [asyncio.ensure_future(scrape_detail(id)) for id in ids]
    await asyncio.wait(scrape_detail_tasks)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
