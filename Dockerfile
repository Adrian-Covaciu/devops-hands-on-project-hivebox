FROM python:3.13-alpine@sha256:452682e4648deafe431ad2f2391d726d7c52f0ff291be8bd4074b10379bb89ff
RUN addgroup hivebox && adduser -G hivebox -D hivebox
USER hivebox
EXPOSE 5000
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python3", "application/main.py"]
