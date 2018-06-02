FROM nvidia/cuda:9.0-cudnn7-runtime
LABEL maintainer "andooown <andooown.dev@gmail.com>"

ENV USER_NAME=developer

RUN apt-get update -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        sudo git make \
        build-essential python-dev python-pip \
        libssl-dev zlib1g-dev libbz2-dev \
        libreadline-dev libsqlite3-dev curl

RUN echo "${USER_NAME} ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
# 一般ユーザがユーザ・グループを追加できるようにする
RUN chmod u+s /usr/sbin/useradd && \
    chmod u+s /usr/sbin/groupadd

USER ${USER_NAME}
ENV HOME=/home/${USER_NAME}

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["bash"]
