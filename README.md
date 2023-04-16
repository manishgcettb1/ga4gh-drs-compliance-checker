# ga4gh-drs-compliance-checker
Python project to check compliance for ga4gh drs kit.

# About me(author)


# Deploy using docker (AWS, Microsoft Azure, or Google Cloud Platform (GCP), or deploying them on Docker clusters such as Kubernetes or Docker Swarm clusters)
1. Build a Docker image for your Python application using the  command: docker build -t myrepo/ga4gh-drs-compliance-checker:latest. (Replace the 'myrepo' as required)
2. Push the Docker image to your Docker registry using the following command: docker push myrepo/ga4gh-drs-compliance-checker:latest
3. Run the docker image docker run myrepo/ga4gh-drs-compliance-checker:latest python3 
4. Above command will log the all specification test cases in terminal


# Deploy to kubernetes cluster using k8s.yml
1. Build the Docker image for the ga4gh-drs-compliance-checker application using the Dockerfile provided. 
2. Run the following command in the directory containing the Dockerfile: docker build -t <name_of_repo>/ga4gh-drs-compliance-checker:latest .
3. Replace name_of_repo with the name of your Docker repository where you want to store the image. Push the Docker image to your Docker registry using the following command: docker push myrepo/ga4gh-drs-compliance-checker:latest
4. Create a Kubernetes deployment for the ga4gh-drs-compliance-checker application using the k8s.yml file. Run the following command in the directory containing the k8s.yml file:kubectl apply -f k8s.yml
5. Verify that the deployment was successful by checking the status of the deployment:kubectl get deployments

# Suggestion(Possible enhancement) to this application
