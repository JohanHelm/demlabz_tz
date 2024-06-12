FROM python:3.11

WORKDIR /backend/
COPY requirements.txt /backend/
RUN  pip install --upgrade pip \
    && pip install -r requirements.txt \
    && alembic init alembic

COPY main.py /backend/   
COPY .env /backend/ 
COPY alembic.ini /backend/alembic.ini
COPY alembic/env.py /backend/alembic/env.py
COPY app/ /backend/app/   
    
EXPOSE 8066

CMD ["python", "main.py"]

