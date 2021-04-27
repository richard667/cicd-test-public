FROM 1234qweraz/nginx
MAINTAINER richard

COPY . .
RUN touch index.html
RUN echo '<h1>Hello, Docker!</h1>' > index.html
RUN rm /usr/share/nginx/html/index.html
RUN mv index.html /usr/share/nginx/html/

