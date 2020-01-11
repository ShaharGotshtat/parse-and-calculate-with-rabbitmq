FROM python:3.6

WORKDIR /calculator

COPY ./calculator/requirements.txt /calculator
RUN pip install -r requirements.txt

COPY ./calculator/calculator.py /calculator
COPY ./calculator/output.txt /calculator
COPY rabbitmq_utils.py /calculator
COPY consts.py /calculator

CMD python calculator.py