# My Blog

This is my blog

## Deploy

### How to deploy Django with Apache2 and mod_wsgi

https://medium.com/saarthi-ai/ec2apachedjango-838e3f6014ab

### Upload and download sqlite DB 

`scp -i ./secrets/django-server.pem ./mysite/db.sqlite3 ubuntu@ec2-3-17-138-175.us-east-2.compute.amazonaws.com:~/djangoblog/mysite`

### Download and update local sqlite DB
`scp -i ./secrets/django-server.pem ubuntu@ec2-3-17-138-175.us-east-2.compute.amazonaws.com:~/djangoblog/mysite ./db.sqlite3`