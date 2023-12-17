FROM python:3.10.9
ENV APP_HOME /socket_app
EXPOSE 3001
EXPOSE 5000
WORKDIR $APP_HOME
COPY . .
RUN pip install poetry
# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install
CMD ["python", "main.py"]