FROM python:3.11

WORKDIR /backend/
COPY app/ /backend/app/
COPY main.py /backend/
COPY requirements.txt /backend/
COPY .env /backend/
RUN  pip install --upgrade pip \
    && pip install -r requirements.txt \
    && alembic init alembic
    
COPY alembic.ini /backend/alembic.ini
COPY alembic/env.py /backend/alembic/env.py
    
    
EXPOSE 8066

CMD ["python", "main.py"]

