FROM python:3.8-slim



RUN python3 -m pip install --no-cache-dir \
        matplotlib  \
        mplcyberpunk\
        pandas \
        numpy \
        jupyter_contrib_nbextensions \
        # Workflow
        Pillow \
        requests \
        SQLAlchemy \
        psycopg2 \
        pymysql \
        jupyter \
        # Telegram
        python-telegram-bot \
        # Google Excel
        google-api-python-client \
        google-auth-httplib2 \
        google-auth-oauthlib

RUN python3 -m pip install --upgrade pip

RUN jupyter notebook --generate-config
RUN jupyter contrib nbextension install --user
RUN mkdir /root/.jupyter/custom/ -p
RUN mkdir /root/.jupyter/nbconfig/ -p

COPY custom.css /root/.jupyter/custom/
COPY notebook.json /root/.jupyter/nbconfig/notebook.json

USER root

RUN mkdir /usr/share -p
WORKDIR /usr/share

CMD ["jupyter", "notebook", "--config=/root/.jupyter/nbconfig/", "--ip=0.0.0.0", "--port=8888", "--allow-root"]
