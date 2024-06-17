FROM python

WORKDIR /

COPY ./src/pythonstart.py .

LABEL authors="Buy"

EXPOSE 8076

ENTRYPOINT ["python", "pythonstart.py"]
