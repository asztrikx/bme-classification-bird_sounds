FROM pytorch/pytorch:2.5.1-cuda11.8-cudnn9-runtime

RUN mkdir /app
WORKDIR /app

# Data
RUN mkdir data
COPY data/train_spectrogram data/train_spectrogram

# Requirements
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip     pip install  --no-cache-dir  -r requirements.txt
	# https://docs.docker.com/build/cache/optimize/#use-cache-mounts

# Misc
COPY .env ./
COPY data/train_metadata_updated.csv data/
COPY data/train_spectrogram.csv data/

# Main
COPY main.ipynb ./
RUN jupyter nbconvert --to script main.ipynb --output /app/main
 	# .py extension is added by default

ENTRYPOINT [ "export IN_DOCKER=1 && ipython /app/main.py" ]