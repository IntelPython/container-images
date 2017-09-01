Docker images for [Intel Distribution for Python](https://software.intel.com/en-us/intel-distribution-for-python)

The image defaults to starting with a bash shell. Intel Python is on the path. There is 1 image for every install configuration.

Images:

* intelpython2_core
* intelpython2_full
* intelpython3_core
* intelpython3_full

You usually want the 'latest' tag, but the docker image tag can be used to request a specific package. For example:

        docker pull intelpython2_core:2017.0.3-1

Will get an image that uses the conda package: intelpython3_core-2017.0.3-1

Tags:

* 2018.0.0-0, 2018.0.0, latest
* 2017.0.3-3, 2017.0.3, latest
* 2017.0.3-1
* 2017.0.3-0
* 2017.0.2-0, 2017.0.2
* 2017.0.1-1, 2017.0.1
* 2017.0.0-2, 2017.0.0



