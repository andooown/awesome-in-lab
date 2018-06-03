# Docker for lab
研究室で利用するための`Dockerfile`置き場

- [lab-cuda](https://hub.docker.com/r/andooown/lab-cuda/)
    - `nvidia/cuda:9.0-cudnn7-runtime`をベースにしたイメージ
    - 起動方法
        ```
        $ nvidia-docker run -it -v `pwd`:/opt/work --name andooown-docker andooown/lab-cuda:9.0-cudnn7-runtime
        ```
