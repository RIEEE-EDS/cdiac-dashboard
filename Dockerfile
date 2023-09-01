FROM python:3

WORKDIR /usr/src/app

EXPOSE 8050

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

CMD [ "gunicorn", "dashboard:server", "--bind", "0.0.0.0:8050", "--access-logfile", "-" ]
