import argparse
import time 
import aiohttp
import asyncio

URL = 'https://google.gr'

async def main(args):
    initial_time = time.time()
    fetched_urls = 0

    async with aiohttp.ClientSession() as session:

        tmp_url = URL
        print(tmp_url)
        for req_number in range(0, args.req_number):
            async with session.get(tmp_url) as resp:
                print("Status code: " + str(resp.status))
                response = await resp.text()
                fetched_urls += 1

    print("Fetched " + str(fetched_urls) +' urls' + ' in ' + str(time.time() - initial_time) + " seconds")


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Simple script making asynchronous requests')
    parser.add_argument(action="store", dest="req_number",type=int, help='Number of requests')
    args = parser.parse_args()
   
    eloop = asyncio.get_event_loop()
    eloop.run_until_complete(main(args))
