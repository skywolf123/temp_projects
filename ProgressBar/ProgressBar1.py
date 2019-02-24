from time import sleep
from tqdm import tqdm, trange

for i in trange(100):
    sleep(0.01)

pbar = tqdm(['a', 'b', 'c', 'd'])
for char in pbar:
    pbar.set_description('Processing %s' % char)
    sleep(1)
