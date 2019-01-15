FROM nginx
RUN ln -snf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' > /etc/timezone
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY / /usr/share/nginx/html
