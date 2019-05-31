# container-images

Dockerfiles and build contexts for building docker images

There is 1 subdirectory for every image to build. Dockerfiles and build
contexts are generated from jinja2 templates in tpls directory. The images.py
script generates the files, and can also be used to build docker images and to
test them. To see more info do:

        python images.py --help

## testing

        python -m pytest tests

Will build every image. Look at the test for example command lines.

## Adding an image

* copy one of the the existing directories
* See images.py for directions on adding a new configuration
* create a new automated build on docker hub, copying build setting of existing image

## Publishing a new release

If we are publishing 2017.0.0 build number 2, then the docker image will have 3
tags: 2017.0.0-2, 2017.0.0, latest. An automated build on docker hub is
triggered by pushing a tag to this repo. The tag has the form 2017.0.0-2.

* Change update_number & build_number in images.py, and add it to tpls/tpl.README.md. Build number is the third argument in all_confs
* Regenerate the READMEs and Dockerfiles for the individual images

        python images.py --gen all

* Commit changes
* Tag with the release name

        git tag -a 2017.0.0-2 -m '2017.0.0-2 release'
        git push
        git push origin 2017.0.0-2

* Check later that all builds have completed on docker hub

## dockerhub config

We use the dockerhub autotesting to test every pull request. When you
push a tag, it will build, test, and publish a new container with a
corresponding tag.

Dockerhub build rule:

source type: tag
source: /.*/
docker tag {sourceref}
dockerfile location: configs/intelpython2_core
