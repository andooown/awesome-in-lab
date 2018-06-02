#!/bin/bash -e

USER_ID=$(id -u)
GROUP_ID=$(id -g)

if [ x"$GROUP_ID" != x"0" ]; then
    groupadd -g $GROUP_ID $USER_NAME
fi
if [ x"$USER_ID" != x"0" ]; then
    useradd -d /home/$USER_NAME -m -s /bin/bash -u $USER_ID -g $GROUP_ID $USER_NAME
fi
if [ -e /home/$USER_NAME ]; then
    sudo chown $USER_ID:$GROUP_ID /home/$USER_NAME
fi
# パーミッションを元に戻す
sudo chmod u-s /usr/sbin/useradd
sudo chmod u-s /usr/sbin/groupadd

git clone git://github.com/yyuu/pyenv.git ${HOME}/.pyenv
export PYENV_ROOT=${HOME}/.pyenv
export PATH=${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${PATH}

exec $@
