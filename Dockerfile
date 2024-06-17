FROM python

WORKDIR /

COPY ./src/resultcheck.py .

LABEL authors="Buy"

EXPOSE 8076

ENTRYPOINT ["python", "resultcheck.py"]
