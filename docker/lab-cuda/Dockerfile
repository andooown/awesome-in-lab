FROM nvidia/cuda:9.0-cudnn7-runtime
LABEL maintainer "andooown <andooown.dev@gmail.com>"

RUN apt-get update -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        sudo git make build-essential \
        python-dev python-pip python-setuptools \
        libssl-dev zlib1g-dev libbz2-dev \
        libreadline-dev libsqlite3-dev curl

ENV USER_NAME=developer \
    USER_ID=7283 \
    GROUP_ID=72

RUN groupadd -g $GROUP_ID $USER_NAME && \
    useradd -d /home/$USER_NAME -m -s /bin/bash -u $USER_ID -g $GROUP_ID $USER_NAME
USER ${USER_NAME}
ENV HOME=/home/${USER_NAME}
WORKDIR ${HOME}

CMD ["bash"]
