import samino
from threading import Thread

client = samino.Client("")

counter = 0

for ulink in open("links.txt").read().split():
	uid=client.get_from_link(ulink).objectId
	for _ in range(25):
		client.watch_ad(uid)
		print(f"Claim {_}")
	counter+=1
	print(f"Done {1}")
