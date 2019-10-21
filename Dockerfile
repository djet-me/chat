### Build and install packages
FROM python:3.7 as build-python

# Install Python dependencies
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

### Build static assets
FROM node:10 as build-nodejs

ARG STATIC_URL
ENV STATIC_URL ${STATIC_URL:-/static/}

# Install node_modules
#COPY webpack.config.js package.json package-lock.json /app/
#WORKDIR /app
#RUN npm install
#
#COPY ./frontend /app/frontend/
#RUN npm run build

### Final image
FROM python:3.7-slim

ARG STATIC_URL
ENV STATIC_URL ${STATIC_URL:-/static/}

COPY . /app
COPY --from=build-python /usr/local/lib/python3.7/site-packages/ /usr/local/lib/python3.7/site-packages/
COPY --from=build-python /usr/local/bin/ /usr/local/bin/
#COPY --from=build-nodejs /app/assets /app/assets
WORKDIR /app

RUN SECRET_KEY=dummy STATIC_URL=${STATIC_URL} python manage.py collectstatic --no-input

RUN python manage.py migrate
RUN python manage.py loaddata fixtures/users.json
RUN python manage.py loaddata fixtures/messages.json

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]