#!/usr/bin/env python3

import os, json, sys

def create_item(title, arg, icon):
	item = {
		"title": title,
		"subtitle": title,
		"arg": arg,
		"icon": {
			"type": ".png",
			"path": icon
		}
		
	}
	return item

icons_file = os.getenv('icons_filepath')
for dirpath, dirname, files in os.walk(icons_file):
	break;

items = []

item = {
	"title": "All Icons",
	"subtitle": "Replace All Icons",
	"arg": "all",
	"icon": {
		"type": ".png",
		"path": "AppIcon.icns"
	}
}

items.append(item)

for file in files:
	if file != ".DS_Store":
		path = dirpath + file
		if file != ".DS_Store" and (file.endswith(".png") or file.endswith(".PNG") or file.endswith(".icns") or file.endswith(".ICNS")):
			if len(sys.argv) > 1 and file.lower().find(sys.argv[1]) == -1:
				continue
			else:
				path = dirpath + file
				title = file
				arg = file
				item = create_item(title, arg, path)
				items.append(item)
				
results = {
	"items": items
}
print(json.dumps(results))			