#Use official NGINX Image
FROM nginx:latest

#Remove default nginx web content
RUN rm -rf /usr/share/nginx/html/*

#Copy static website files to Nginx html directory
COPY . /usr/share/nginx/html/

#Copy custom nginx config
COPY default.conf /etc/nginx/conf.d/default.conf

#Expose port 80
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
