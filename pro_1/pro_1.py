

import os

path='/Users/Shared/pycharm'

files = os.listdir(path)

print(files)

for f in files:
    if 'DA' in f and f.endswith('A'):
        print('Found it! ' + f)
