FROM alpine:3.15
ENV PYTHON_VERSION 3.11.0a7
#ENV PROJECT_DIR = /src
#WORKDIR /src
COPY batchSch.py batchSch.py


#COPY src/requirements.txt requirements.txt
#COPY src/main.py main.py

#RUN pip install --no-cache-dir -r requirements.txt
#ENTRYPOINT ["./src/main.py"]
ENTRYPOINT [ "python3" ]
CMD [ "python3", "batchSch.py"]
#CMD ["echo", "hello-world"]
