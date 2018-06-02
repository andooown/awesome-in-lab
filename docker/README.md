# Docker for lab
研究室で利用するための`Dockerfile`置き場

- [lab-cuda](https://hub.docker.com/r/andooown/lab-cuda/)
    - `nvidia/cuda:9.0-cudnn7-runtime`をベースにしたイメージ
    - nvidia-docker2
        ```
        $ docker run -it --runtime=nvidia -u $(id -u):$(id -g) -v $(pwd):/home/developer/work andooown/lab-cuda:9.0-cudnn7-runtime
        ```
    - nvidia-docker(in Lab)
        ```
        $ nvidia-docker run -it -u `id -u`:`id -g` -v `pwd`:/home/developer/work andooown/lab-cuda:9.0-cudnn7-runtime
        ```