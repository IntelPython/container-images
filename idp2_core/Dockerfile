FROM continuumio/miniconda3:4.111

MAINTAINER Robert Cohn <Robert.S.Cohn@intel.com>

RUN conda config --add channels intel \
    && conda create -n idp intelpython2_core=2017.0.0 python=2

ENV PATH /opt/conda/envs/idp/bin:$PATH
