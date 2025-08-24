FROM python:3.13

WORKDIR /code

#COPY ./requirements.txt /code/requirements.txt
#RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock* ./
RUN poetry install --only=main --no-cache

COPY ./app /code/app

CMD ["fastapi", "run", "app/main.py", "--port", "80"]