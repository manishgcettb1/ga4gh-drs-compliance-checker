# ga4gh-drs-compliance-checker
Python project to verify the compliance of the GA4GH DRS Starter Kit's *GET /objects/{object_id}* endpoint to the DRS v1.2.0 specification.
 ## About repository
 - conf.ini -> Configuration file to configure the DRS URL(update this url if DRS API is not running on http://localhost:5000/ga4gh/drs/v1/ )
 - drs_compliance_runner.py -> Contains main method. Execute all methods that validates the DRS API specification. It call methods from drs_specification.py and drs_object_ep_value_specification.py
 - /drs_compliance/api/drs_specification.py -> It  make http call to DRS and verify the specification. E.g- Verify all mandatory fields to be available in response, Id, check checksums response in correct format or not..etc
 - /drs_compliance/api/drs_object_ep_value_specification.py -> It make http calls and verify the value for some drs_object(it may fail if DRS objects are different from given in this assignment)
 - /drs_compliance/api/utl.py - Have util methods
## About GA4GH-Data Repository Service (DRS) v1.2.0
- **Data Repository Service (DRS) v1.2.0**: https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.2.0/docs/
- **GA4GH Starter Kit DRS website:** https://starterkit.ga4gh.org/docs/starter-kit-apis/drs/drs_overview
- **GA4GH Starter Kit DRS Github:** https://github.com/ga4gh/ga4gh-starter-kit-drs

# About me(author)
I am Manish, have 11 years of experience in Software development. I have been working majorly in Java-SpringBoot based enterprise application but also acquired working 
experience in Python(2 & 3). I gained python experience currently working on few python projects in my EMBL-EBI work.

# Prerequisite
This application make http call to DRS application deployed locally on URL: http://localhost:5000/ga4gh/drs/v1. It is assumed that you have DRS API running on your machine.
If it's not running on your machine then need to change the URL drs_url = http://localhost:5000/ga4gh/drs/v1/ under conf.ini file.
## To install   (DRS) v1.2.0 
Follow steps at https://github.com/ga4gh/ga4gh-starter-kit-drs

# Install and run on local machine
1. checkout the code
2. make sure you have python installed on your machine.
3. Run the DRS api locally (see above ) or update the drs_url
4. Install the requirement.txt by running pip install -r requirements.txt
5. execute drs_compliance_runner.py

# Deploy using docker 
1. Build a Docker image for your Python application using the  command: docker build -t myrepo/ga4gh-drs-compliance-checker:latest. (Replace the 'myrepo' as required)
2. Push the Docker image to your Docker registry using the following command: docker push myrepo/ga4gh-drs-compliance-checker:latest
3. Run the docker image docker run myrepo/ga4gh-drs-compliance-checker:latest python3 
4. Above command will log the all specification test cases in terminal
5. To run docker run myrepo/ga4gh-drs-compliance-checker:latest


# Deploy to kubernetes cluster using k8s.yml
1. Build the Docker image for the ga4gh-drs-compliance-checker application using the Dockerfile provided. 
2. Run the following command in the directory containing the Dockerfile: docker build -t <name_of_repo>/ga4gh-drs-compliance-checker:latest .
3. Replace name_of_repo with the name of your Docker repository where you want to store the image. Push the Docker image to your Docker registry using the following command: docker push myrepo/ga4gh-drs-compliance-checker:latest
4. Create a Kubernetes deployment for the ga4gh-drs-compliance-checker application using the k8s.yml file. Run the following command in the directory containing the k8s.yml file:kubectl apply -f k8s.yml
5. Verify that the deployment was successful by checking the status of the deployment:kubectl get deployments

# Next step
1. Use of pytest test suite to execute the all specifications methods
2. Extend to deployment on cloud
3. Can be added to CI/CD pipeline (To add .gitlab.yml)

# Feedback
If you have any feedback or need help on this application, please feel free to drop a mail to manishgcettb@gmail.com
