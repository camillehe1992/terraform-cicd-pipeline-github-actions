# CICD Setup

Automate, customize, and execute your software development workflows right in your repository with GitHub Actions. You can discover, create, and share actions to perform any job you'd like, including CI/CD, and combine actions in a completely customized workflow.

The pipeline executes terraform scripts in container, which provide Terraform execution environment and providers pre-installed. The docker image is located in AWS ECR. You can use the official [image from Hashicorp](https://hub.docker.com/r/hashicorp/terraform/), but sometimes it’s wise to maintain your own Docker images with additional tools you may need. If you decided to use the official image, skip `ecr_login.sh` and replace environment variable `TF_IMAGE` with `hashicorp/terraform`.

## Deploy/Destroy a specific Component

## Deploy all Components

## Reference

- https://docs.github.com/en/actions