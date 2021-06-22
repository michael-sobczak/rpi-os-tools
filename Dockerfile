FROM python:3.8-slim-buster

ARG OS_IMAGE_DIR=/images/release
ARG IMAGE_OUTPUT_DIR=/images/custom
#ARG VERSION
#ARG RELEASE

RUN mkdir -p ${OS_IMAGE_DIR}
RUN mkdir -p ${IMAGE_OUTPUT_DIR}
RUN mkdir -p /workspace
RUN mkdir -p /workspace/rpios_tools
COPY dist/*.whl /workspace/rpios_tools/
RUN pip install /workspace/rpios_tools/*.whl

COPY ./entrypoint.sh /workspace/
RUN chmod a+x /workspace/entrypoint.sh

WORKDIR /workspace


ARG VERSION
ENV raspios_version=${VERSION}

ARG RELEASE
ENV raspios_release=${RELEASE}

ENV image_dir=${OS_IMAGE_DIR}
ENV output_dir=${IMAGE_OUTPUT_DIR}

ENTRYPOINT ./entrypoint.sh ${raspios_version} ${raspios_release} ${image_dir} ${output_dir}

