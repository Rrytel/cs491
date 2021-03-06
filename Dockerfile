FROM buildpack-deps:buster
ENV PATH /usr/local/bin:$PATH
#ENV PROJECT_DIR = /src
#WORKDIR /src
RUN set -eux; \
	apt-get update; \
	apt-get install -y --no-install-recommends \
		libbluetooth-dev \
		tk-dev \
		uuid-dev \
	; \
	rm -rf /var/lib/apt/lists/*

#COPY src/requirements.txt requirements.txt
#COPY src/main.py main.py
COPY batchSch.py batchSch.py
COPY batch.txt batch.txt
#RUN pip install --no-cache-dir -r requirements.txt
#ENTRYPOINT ["./src/main.py"]python3 batchSch.py batch.txt FCFS
CMD ["python3","batchSch.py", "batch.txt","FCFS"]
#CMD ["echo", "hello-world"]
