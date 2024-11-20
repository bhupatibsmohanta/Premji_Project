# Pipelines
<!-- bIIZnCR-Z0dboHfaVICowg5yOrqQAqZfnCKlbQgipG0= -->


The assignment is to create 2 pipelines, one with automated scrapping based on ticker in instructions, the second one based on static input.

Prerequisites:
- Python
- Docker

Steps to run:

1. Execute run.sh shell script to build & start docker instance
    ./run.sh
   
2. Run command: "docker ps" to list all running docker daemon processes
    and copy the container id of apache/airflow instance (e.g. 89fd07ff8f11)

3. Run command: "docker exec -it 89fd07ff8f11 bash" to initialize airflow server on port: 8080

4. Open url: http://localhost:8080/home on web browser & login to airflow with username: abc & password: abc





