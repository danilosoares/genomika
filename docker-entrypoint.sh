#!/bin/bash

if [ "$1" != "" ]; then
    exec "$@"
    exit
fi


# collect statics
python manage.py collectstatic --noinput -v 0

# compress statics
#python parceiros/manage.py compress -f

# send static to s3
# s4cmd sync --recursive parceiros/assets s3://$AWS_BUCKET_NAME/static & > /dev/null

if [ "$ENVIRONMENT" = "PRODUCTION" ]; then
	exec gunicorn --bind 0.0.0.0:8000 --workers 4 --timeout 300
else
    exec gunicorn --bind 0.0.0.0:8000 --timeout 300
fi
