# Simple Dagit Deployment using Docker

## Prereqs

1. Install Docker. 
2. Install docker-compose.

If you're on a mac or windows docker-compose is bundled with your docker install. If you're on Linux you might have to install
docker-compose separately. 

## Startup

Run `docker-compose up -d`

Navigate to http://localhost:3000

## Pipelines 

All pipelines are loaded in via a `volume mount` through the `pipelines` directory. 

Add any new files configs etcc you want there. Just make sure to update the `repository.yml` file. 

Dagit/Dagster should automatically pick up the changes. Refresh your browser to view the new pipelines. 
