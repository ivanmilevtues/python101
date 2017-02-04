import json 
from sys import stdout
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup
import requests


MAIN_URL = "http://register.start.bg/"

src = requests.get(MAIN_URL).text


def take_links():
    soup = BeautifulSoup(src)
    links = []
    for link in soup.findAll('a'):
        curr_link = link.get('href')
        if curr_link and curr_link[0] != '#':
            if 'link' in curr_link:
                curr_link = MAIN_URL + curr_link
            links.append(curr_link)
    return links


def take_header(links):
    web_headers = {}
    print('---------------------------------------')
    for link in links:
        print('.')
        try:
            server = requests.get(link).headers['Server']
            if server in web_headers:
                web_headers[server] += 1
            else:
                web_headers[server] = 0
        except requests.exceptions.InvalidSchema:
            print('Invalid Schema!')
        except requests.exceptions.MissingSchema:
            print('Missing Schema!')
        except requests.exceptions.TooManyRedirects:
            print('Too many refirects!')
        except KeyError:
            print('No Key')
        except Exception:
            print('FeelsBadMan')
    return web_headers


def take_only_server_type(data):
    server_data = {}
    for k, v in data.items():
        key = k.split('/')[0]
        if key in server_data.keys():
            server_data[key] += v + 1
        else:
            server_data[key] = v + 1

    print(server_data)
    return server_data


def main():
    # links = take_links()
    # headers = take_header(links)
    # with open('data.json', 'w') as fp:
    #     json.dump(headers, fp)
    # print(headers)
    with open('data.json', 'r') as fp:
        data = json.load(fp)
    chart_data = take_only_server_type(data)
    print(chart_data)
    plt.bar(range(len(chart_data)), chart_data.values(), align='center')
    plt.xticks(range(len(chart_data)), chart_data.keys())
    plt.show()


if __name__ == '__main__':
    main()
