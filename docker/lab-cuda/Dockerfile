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

RUN git clone https://github.com/pyenv/pyenv.git ${HOME}/.pyenv && \
    echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ${HOME}/.bash_profile
ENV PYENV_ROOT=${HOME}/.pyenv
ENV PATH=${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${PATH}
RUN pyenv install 2.7.15 && pyenv global 2.7.15 && pyenv rehash

RUN pip install pipenv && \
    echo 'eval "$(pipenv --completion)"' >> ${HOME}/.bash_profile
ENV PIPENV_VENV_IN_PROJECT=true

CMD ["bash"]
