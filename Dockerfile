FROM python:2.7
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD sketchcase /code/
ADD settings.cfg /code/
ENV SKETCHCASE_SETTINGS=/code/settings.cfg
