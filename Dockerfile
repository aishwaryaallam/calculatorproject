FROM python:3

ARG add_file="Unit Test Addition.csv"
ARG sub_file="Unit Test Subtraction.csv"
ARG mul_file="Unit Test Multiplication.csv"
ARG div_file="Unit Test Division.csv"
ARG sqr_file="Unit Test Square.csv"
ARG root_file="Unit Test Square Root.csv"

ADD ${add_file} /
ADD ${sub_file} /
ADD ${mul_file} /
ADD ${div_file} /
ADD ${sqr_file} /
ADD ${root_file} /

ADD main.py /


RUN pip install unittest2

CMD [ "python", "./main.py" ]