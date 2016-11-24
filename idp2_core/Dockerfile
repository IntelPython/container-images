FROM continuumio/miniconda3:4.1.11

MAINTAINER Robert Cohn <Robert.S.Cohn@intel.com>

ENV ACCEPT_INTEL_PYTHON_EULA=yes

RUN conda config --add channels intel \
    && conda create -y -q -n idp intelpython2_core=2017.0.1 python=2

ENV PATH /opt/conda/envs/idp/bin:$PATH
