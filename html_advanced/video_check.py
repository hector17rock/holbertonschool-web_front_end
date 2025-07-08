#!/usr/bin/env python3

with open('38-styleguide.html', 'r') as f:
    content = f.read()

url = ('https://intranet-projects-files.s3.amazonaws.com/webstack/'
       'BigBuckBunny.mp4')
if url in content:
    print('video has correct source')
