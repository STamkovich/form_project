FROM python3.9-alpine

WORKDIR /usr/src/form_project

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD [ "python", "manege.py", "ranserver", "0.0.0.0:8080" ]

