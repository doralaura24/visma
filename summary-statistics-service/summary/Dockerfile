FROM python:3.7.5

WORKDIR /summary
RUN python -m pip install --upgrade pip
ADD . /summary
RUN python -m pip install -r summary/requirements.txt


EXPOSE 50052
ENTRYPOINT [ "python", "summary/server.py" ]