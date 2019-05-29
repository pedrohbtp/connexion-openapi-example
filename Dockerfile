FROM python:3.6
WORKDIR /usr/app
ADD . /usr/app
RUN pip install virtualenv
RUN virtualenv -p python3.6 ./zappa_env3
RUN /usr/app/zappa_env3/bin/pip install -r requirements.txt
# Appends the python path to the beginning so we wouldn't need to activate it
ENV PATH /usr/app/zappa_env3/bin:$PATH

