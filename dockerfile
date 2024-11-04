FROM mcr.microsoft.com/playwright/python:v1.47.0-jammy

RUN pip install pytest-playwright && \
    pip install pytest-html && \
    playwright install

WORKDIR  /app

COPY .   /app

CMD ["bash", "-c"]

