#!/usr/bin/env python3
import os
import sys
import requests

def read_message():
    path = os.environ.get('MESSAGE_FILE')
    if path and os.path.isfile(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    return os.environ.get('MESSAGE', '')

def main():
    base = os.environ.get('MASTODON_BASE_URL')
    token = os.environ.get('MASTODON_TOKEN')
    if not base or not token:
        print('MASTODON_BASE_URL or MASTODON_TOKEN not set; skipping')
        return
    message = read_message()
    if not message:
        print('No message found; skipping')
        return
    url = base.rstrip('/') + '/api/v1/statuses'
    headers = {'Authorization': f'Bearer {token}'}
    data = {'status': message}
    try:
        resp = requests.post(url, headers=headers, data=data, timeout=15)
        resp.raise_for_status()
        print('Posted to Mastodon')
    except Exception as e:
        print('Error posting to Mastodon:', e)
        sys.exit(1)

if __name__ == '__main__':
    main()
