FROM continuumio/miniconda3:4.1.11

MAINTAINER Robert Cohn <Robert.S.Cohn@intel.com>

ENV ACCEPT_INTEL_PYTHON_EULA=yes

RUN conda config --add channels intel \
    && conda create -y -q -n idp intelpython3_core=2017.0.1 python=3

ENV PATH /opt/conda/envs/idp/bin:$PATH
