FROM python:2.7

ENV PYTHONIOENCODING UTF-8

EXPOSE 8000

# install requirements - https://support.aptible.com/topics/paas/how-to-set-up-pip-caching/
ADD requirements.txt /app/

WORKDIR /app/
RUN pip install -r requirements.txt && rm -rf /root/.cache

ADD . /app/

ENTRYPOINT ["/app/docker-entrypoint.sh"]