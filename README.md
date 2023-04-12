# nlp_Q1

## Installation

```
docker build -t <image_name> . --no-cache
```

## Usage

```
docker run -it -v <dataset_dir>:/dataset --name nlp_test <image_name> /bin/bash

python main.py
```

## Output
The output seed_list will be in `/workspace/seed_file.txt` like

*seed_file*, *number*
```
0000af9a6531d4b967b28186ab063fd0.txt, 200
00012de69ef822c4ae3b769d297281b8.txt, 200
0002b6c5981fd7995659c451563b1d64.txt, 200
0002bc1d5025187056b179afeb11bec3.txt, 200
000375bc279c5ef855921de182d77b2a.txt, 200
0004ffc6a3972a16aa0017c6feeb9578.txt, 200
00053a61200ca931c22be2f8d3bbf477.txt, 200
0005d69229fdadd70809b5e5aac4d412.txt, 200
000669713c5b8e5b49841fe94d59d566.txt, 200
000784e342d496de27adb3b489683c26.txt, 200
...
```