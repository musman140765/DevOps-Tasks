## CI/CD Pipeline with GitHub Actions

This project includes a GitHub Actions workflow that runs nightly to:

- Lint the Python code using flake8
- Run unit tests using pytest
- Build a Docker image of the app
- Push the image to Docker Hub

### Manual Run
You can also trigger the workflow manually from the Actions tab in GitHub.

### Docker Hub Credentials
Make sure to add the following GitHub secrets to your repository:
- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

