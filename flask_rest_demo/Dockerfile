FROM python:3.8-slim
WORKDIR /code
COPY . /code
RUN  pip install -r ./requirements.txt -i https://pypi.doubanio.com/simple && /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  && rm -rf /var/lib/apt/lists/*
EXPOSE 5000
CMD  gunicorn  -c  gunicorn_config.py --log-level=debug   run:app
