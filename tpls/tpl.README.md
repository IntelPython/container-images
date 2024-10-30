Docker images for [Intel Distribution for Python](https://www.intel.com/content/www/us/en/developer/tools/oneapi/distribution-for-python.html)

The image defaults to starting with a bash shell. Intel Python is on the path. There is 1 image for every install configuration.

Images:

* intelpython3_full

You usually want the 'latest' tag, but the docker image tag can be used to request a specific package. For example:

        docker pull intelpython3_full:2017.0.3-1

Will get an image that uses the conda package: intelpython3_full-2017.0.3-1

Tags:

* 2020.0
* 2019.5
* 2019.4
* 2019.3
* 2019.1-0
* 2019.0.0-0b, 2019.0.0-0a, 2019.0.0-0, 2019.0.0
* 2018.0.3
* 2018.0.2
* 2018.0.1-0, 2018.0.1
* 2018.0.0-0, 2018.0.0
* 2017.0.3-3, 2017.0.3
* 2017.0.3-1
* 2017.0.3-0
* 2017.0.2-0, 2017.0.2
* 2017.0.1-1, 2017.0.1
* 2017.0.0-2, 2017.0.0

LEGAL NOTICE: By accessing, downloading or using this software and any required dependent software (the "Software Package"), you agree to the terms and conditions of the software license agreements for the Software Package, which may also include notices, disclaimers, or license terms for third party software included with the Software Package. Please refer to the "third-party-programs.txt" or other similarly-named text file for additional details.
