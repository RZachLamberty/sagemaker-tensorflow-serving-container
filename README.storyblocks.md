# storyblocks `bert-dl` development

## setup

you need to download the `model.tar.gz` file and unzip it into the path 
`test/resources_bertdl/models/`. execute

```shell script
./scripts/storyblocks-init.sh
```

to do this


## running or development?

I'm assuming you want to do one of two things:

1. run a local instance of the `bert-dl` `sagemaker` endpoint
1. develop custom pre- or post-processing scripts for deployment on `sagemaker`

whichever of the two you are looking to do, skip to the corresponding section 
below


### run a local instance of the `bert-dl` `sagemaker` endpoint

you're ready to go; just run

```shell script
./scripts/start-bertdl.sh --version 1.14 --arch cpu
```

to verify that this worked, you can run either

```shell script
./scripts/curl-bertdl.sh
```

or

```shell script
./scripts/requests-bertdl.py
```

for both, expected behavior is to print out `json` records of the format

```
{"outputs": [0.8566522, ...]}
```

and / or `csv` records (just the probabilities in `outputs` above separated by
newlines)

you can also review the log messages that are written out to `log.txt` in the 
top level directory.

at any time you can stop this container via

```shell script
# note: no stop-bertdl; stop is the same script regardless of model
./scripts/stop.sh --version 1.14 --arch cpu
```
 

### develop custom pre- or post-processing scripts for deployment on `sagemaker`

simply edit the code in `test/resources_bertdl/models/code`. if you make any 
changes this way, you will need to commit them to the main repo
[here](https://github.com/Footage-Firm/machine-learning/tree/feature/zach/multitoken-research/python/multitoken-research/bert).

note that while the code is mounted directly into the container (so edits on 
your local machine are seen immediately inside the container), the server code 
isn't hot-reloading it -- if you want your changes to take affect, you need to 
kill and re-start the container. I found the following command useful for doing 
just that:

```shell script
./scripts/stop.sh --version 1.14 --arch cpu && ./scripts/start-bertdl.sh --version 1.14 --arch cpu && sleep 4
```  