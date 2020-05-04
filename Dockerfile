FROM python:3.7

RUN pip install apache-airflow[postgres,kubernetes]

CMD airflow version
