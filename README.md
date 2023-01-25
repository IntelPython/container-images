# DISCONTINUATION OF PROJECT #
This project will no longer be maintained by Intel.
Intel has ceased development and contributions including, but not limited to, maintenance, bug fixes, new releases, or updates, to this project.
Intel no longer accepts patches to this project.
# container-images

[![.github/workflows/ci.yml](https://github.com/IntelPython/container-images/actions/workflows/ci.yml/badge.svg)](https://github.com/IntelPython/container-images/actions/workflows/ci.yml)

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

## Publishing a new release (Internal Use Only)

Disclaimer: Do NOT do this unless all packages for upcoming release have been
uploaded to Intel channel on Anaconda Cloud. Best time to do this is right before
FCS when all packages have automatically been uploaded and validated.

If we are publishing 2017.0.0 build number 2, then the docker image will have 3
tags: 2017.0.0-2, 2017.0.0, latest. Github Actions will create a Docker image
after a PR is merged. The following steps are all that is needed to update our
Dockerhub with our latest IntelPython.

* Change update_number & build_number in images.py. Most of the time, the build number
  remains the same (#0) and the minor version is incremented (e.g. 2021.1.0 -> 2021.2.0)
* Regenerate the READMEs and Dockerfiles for the individual images by running the following
  command

        python images.py --gen all

* Create branch and commit changes
* Tag with the release name

        git tag -a 2022.0.0-0 -m '2022.0.0-0 release'
        git push origin update/2022.0.0-0
        git push origin 2022.0.0-0

* Create PR, check that tests pass, and then merge PR. Github actions has been setup to
  automatically build the Docker image and push it to Dockerhub afterwards.
