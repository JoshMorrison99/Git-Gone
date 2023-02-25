import requests
import json
import re
import argparse

# This is the index that the word will match with {-25}SECRET{+50}
START=25 # This number will always be negative
END=50
def search(url, token, searchTerm):
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {token}',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    with open('gitgone.json', 'w') as f:
        json.dump(data, f)

    feed = []
    item_feed = {}
    for item in data['items']:
        url = item['html_url'].replace('/blob', '').replace('https://github.com', 'https://raw.githubusercontent.com')
        item_feed['url'] = url
        item_feed['name'] = item['name']
        item_feed['extension'] = item['name'].split('.')[1]
        item_feed['extracted'] = []
        response = requests.get(url)
        text = response.text
        matches = re.findall(f'{searchTerm}', text, re.IGNORECASE)
        secrets = []
        if(matches):
            occurance = 0
            for match in matches:
                match_index = text.lower().find(match.lower(), occurance) # find the index of the match, case-insensitive
                occurance = match_index + 1
                secret_extracted = text[max(match_index-START, 0):match_index+END ].replace('\n','')
                secrets.append(secret_extracted)
            item_feed['extracted'].append(secrets)
        feed.append(item_feed)
    return(feed)

def main():
    parser = argparse.ArgumentParser(description="Automated GitHub Secret Detection",
    usage="python3 gitgone.py -u [target] -t [token]")

    parser.add_argument('-t', metavar='-target', help="Specify the target (shelled.io)", required=True)
    parser.add_argument('-a', metavar='-api-token', help="Specify your GitHub API token", required=True)

    args = parser.parse_args()
    
    feed = {}

    # GitHub Search for "secret"
    searchTerm = 'secret'
    url = f'https://api.github.com/search/code?q="{args.t}"+{searchTerm}'
    results = search(url, args.a, searchTerm)
    feed[searchTerm] = []
    feed[searchTerm].append(results)

    # GitHub Search for "password"
    searchTerm = 'password'
    url = f'https://api.github.com/search/code?q="{args.t}"+{searchTerm}'
    results = search(url, args.a, searchTerm)
    feed[searchTerm] = []
    feed[searchTerm].append(results)

    print(feed)
    

main()
