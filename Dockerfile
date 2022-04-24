FROM alpine:3.15
#ENV PROJECT_DIR = /src
WORKDIR /src
COPY batchSch.py batchSch.py


#COPY src/requirements.txt requirements.txt
#COPY src/main.py main.py

#RUN pip install --no-cache-dir -r requirements.txt
#ENTRYPOINT ["./src/main.py"]

CMD [ "python", "batchSch.py"]
#CMD ["echo", "hello-world"]
