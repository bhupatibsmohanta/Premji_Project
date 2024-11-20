docker build -t img1084 .
echo "Image build img1084"

docker run img1084
echo "Image run img1084"

docker-compose run webserver airflow users create     --username abc     --password abc     --firstname abc     --lastname abc     --role Admin     --email abc@gmail.com
echo "docker compose run img1084"

docker-compose up -d
echo "docker compose up"


# To stop the services: docker-compose down
# To view logs: docker-compose logs -f