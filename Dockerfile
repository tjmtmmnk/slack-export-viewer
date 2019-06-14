FROM python:3.6

RUN mkdir /var/www

WORKDIR /var/www

COPY requirements.txt ./

RUN pip install -r ./requirements.txt

RUN /bin/bash -c "source /var/www/prod_env.sh"

CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]
