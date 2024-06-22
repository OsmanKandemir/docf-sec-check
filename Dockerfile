# Labels and Credits
LABEL \
    name="DocF-Sec-Check" \
    author="Osman Kandemir" \
    description="DockF-Sec-Check helps to make you Dockerfile commands more secure."

FROM python:3.11-slim
LABEL Maintainer="OsmanKandemir"
COPY . /app
WORKDIR /app
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip --no-cache-dir install -r requirements.txt
ENTRYPOINT ["python", "docf-checker.py"]

#Usage Will Write.