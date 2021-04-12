import argparse
import requests
import time 

URL = 'https://google.gr'

def main(args):
    initial_time = time.time()
    tmp_url = URL
    fetched_urls = 0

    for req_num in range(0, args.req_number):
        response = requests.get(tmp_url)
        print(response)
        fetched_urls += 1
       
    print("Fetched " + str(fetched_urls) +' urls' + ' in ' + str(time.time() - initial_time) + " seconds")

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Simple script making synchronous requests')
    parser.add_argument(action="store", dest="req_number",type=int, help='Number of requests')
    args = parser.parse_args()
   
    main(args)