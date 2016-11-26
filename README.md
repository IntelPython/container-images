# container-images
Dockerfiles for building docker images

There is 1 subdirectory for every image to build.

## testing

        python -m pytest tests

Will build every image. Look at the test for example command lines.

## Adding an image

* copy one of the the existing directories
* See .travis.yml & images.py for directions on adding a new configuration
* create a new automated build on docker hub, copying build setting of existing image

## Publishing a new release

* Change release name in images.py
* Commit changes
* Tag with the release name

        git tag -a 2017.0.0 -m 'new release'

* Push changes, this will trigger testing on travis-ci

        git push

* When travis-ci testing completes, push the tag

        git push origin 2017.0.0

* Check later that all builds have completed on docker hub
