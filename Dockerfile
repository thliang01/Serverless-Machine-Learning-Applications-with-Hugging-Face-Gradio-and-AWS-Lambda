# Dockerfile
FROM public.ecr.aws/docker/library/python:3.8.12-slim-buster
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.6.4 /lambda-adapter /opt/extensions/lambda-adapter
WORKDIR /var/task

COPY requirements.txt  ./requirements.txt
RUN python -m pip install -r requirements.txt

COPY app.py  ./
COPY cheetah.jpg  ./cheetah.jpg
COPY lion.jpg  ./lion.jpg
CMD ["python3", "app.py"]
