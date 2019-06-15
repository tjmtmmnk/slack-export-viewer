FROM nginx

WORKDIR /opt

COPY auth.htpasswd  /etc/nginx/

RUN sed -i -e 's/^root::/root:!:/' /etc/shadow

CMD ["nginx", "-g", "daemon off;","-c","/etc/nginx/nginx.conf"]