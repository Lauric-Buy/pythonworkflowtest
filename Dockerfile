FROM python

WORKDIR /

COPY pythonworkflowtest/ .

LABEL authors="Buy"

EXPOSE 8076

ENTRYPOINT ["python", "pythonstart.py"]
