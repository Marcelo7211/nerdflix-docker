# Imagem do front-end: Nginx entregando HTML, CSS e JS
FROM nginx:1.27-alpine

COPY frontend/ /usr/share/nginx/html/

EXPOSE 80
