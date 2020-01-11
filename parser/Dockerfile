FROM python:3.6

WORKDIR /parser

COPY ./parser/requirements.txt /parser
RUN pip install -r requirements.txt

COPY ./parser/parser.py /parser
COPY ./parser/input.txt /parser
COPY rabbitmq_utils.py /parser
COPY consts.py /parser

CMD python parser.py