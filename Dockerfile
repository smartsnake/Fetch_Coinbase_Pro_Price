FROM python:3

ADD main.py /
ADD config.json /
ADD requirments.txt /

RUN pip3 install -r requirments.txt

CMD ["python3","-u","./main.py"]