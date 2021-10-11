FROM python:latest
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . /code/
COPY init.sql /docker-entrypoint-initdb.d/

RUN useradd -ms /bin/bash admin
RUN chown -R admin:admin /code
RUN chmod 755 /code
USER admin

EXPOSE 8000

CMD ["sh", "scripts/launch.sh"]
