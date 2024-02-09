FROM opentensorfdn/bittensor:6.6.0


COPY ./api /app/api
COPY app.py /app/app.py
COPY .env /app/.env

WORKDIR /app


# install python, build essentials
RUN pip install -r api/requirements.txt
RUN pip install uvicorn[standard]

EXPOSE 8000

#add your flag commands
CMD [ "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--loop", "asyncio", "--workers", "12" ]