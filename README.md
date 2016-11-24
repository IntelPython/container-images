# container-images
Dockerfiles for building docker images

There is 1 subdirectory for every image to build. They share a README by symlinking to docker_repo.README.md.

## testing

    python -m pytest tests

Will build every image.

## Adding an image

* copy one of the the existing directories
* edit the dockerfile
* add the directory name in test/test_build.py
* create a new automated build on docker hub, copying build setting of existing image

## Publishing a new release

* Edit the Dockerfiles to refer to the new release
* Commit changes
* Tag with the release name
    git tag -a 2017.0.0 -m 'new release'
* On dockerhub, edit build settings for all repos to change build rule that generates the image with the latest tag
* Push changes and tag
    git push
    git push origin 2017.0.0
* Check later that all builds have completed on docker hub
