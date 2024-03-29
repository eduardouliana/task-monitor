FROM python:3

ENV TZ="America/Sao_Paulo"

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "main.py" ]