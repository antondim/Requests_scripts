import argparse
import time 
import aiohttp
import asyncio

URL = 'https://google.gr'

async def fetch_url(session, url):
    async with session.get(url) as resp:
        if resp.ok: # Not 200 OK
            response = await resp.text()
            return True
        else:
            return False

async def main(args):
    initial_time = time.time()

    async with aiohttp.ClientSession() as session:
       
        reqs = []
        tmp_url = URL

        for req_number in range(0, args.req_number):
            reqs.append(asyncio.ensure_future(fetch_url(session, tmp_url)))

        mass_responses = await asyncio.gather(*reqs)

    print("Fetched " + str(mass_responses.count(True)) +' urls' + ' in ' + str(time.time() - initial_time) + " seconds")


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Simple script making asynchronous requests concurrently')
    parser.add_argument(action="store", dest="req_number",type=int, help='Number of requests')
    args = parser.parse_args()
   
    eloop = asyncio.get_event_loop()
    eloop.run_until_complete(main(args))
