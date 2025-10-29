# Churn Prediction Service with Scikit-Learn, Flask, and Docker

This project demonstrates how to deploy a scikit-learn churn prediction model as a web service using Flask, served by Gunicorn, and containerized with Docker.

## Project Overview

The primary goal of this project is to provide a simple yet complete example of a machine learning model deployment pipeline. It includes scripts for training a model, a Flask application to serve predictions, and a Dockerfile to package the entire service for easy deployment.

The model predicts whether a customer is likely to churn based on their account information.

## Technologies Used

*   **Python 3.13**: The core programming language.
*   **Scikit-learn**: For training and using the logistic regression model.
*   **Flask**: A lightweight web framework to create the prediction API endpoint.
*   **Gunicorn**: A robust WSGI HTTP server to run the Flask application in production.
*   **Docker**: For containerizing the application and its dependencies, ensuring a consistent and reproducible environment.
*   **uv**: A fast Python package installer used for dependency management.

## Project Structure

Here's a breakdown of the key files in this repository:

*   `Dockerfile`: Defines the steps to build a Docker image for the application. It sets up the Python environment, installs dependencies, and configures the container to run the web service.
*   `pyproject.toml` & `uv.lock`: Project configuration and dependency management files.
*   `train.py`: A script to train the logistic regression model using a sample dataset and save the trained model and data vectorizer to a file (`model_C=1.0.bin`).
*   `predict_flask.py`: The Flask application that loads the trained model and exposes a `/predict` endpoint to serve predictions.
*   `model_C=1.0.bin`: The pre-trained scikit-learn model and data vectorizer, saved using pickle.
*   `test.py`: An example script demonstrating how to send a request to the prediction service.

## How to Use

Follow these steps to build and run the churn prediction service.

### 1. Build the Docker Image

From the root directory of the project, run the following command to build the Docker image. This will create an image named `predict-churn`.

```bash
docker build -t predict-churn .
```

### 2. Run the Docker Container

Once the image is built, you can run it as a container. This command starts the container, maps port 9696 on your local machine to port 9696 inside the container, and runs the service in the foreground.

```bash
docker run -it --rm -p 9696:9696 predict-churn
```

You should see output from Gunicorn indicating that the server is running and listening for requests.

### 3. Send a Prediction Request

With the container running, you can send a `POST` request to the `/predict` endpoint to get a churn prediction. Here is an example using `curl`:

```bash
curl -X POST -H "Content-Type: application/json" -d '{
    "gender": "female",
    "seniorcitizen": 0,
    "partner": "yes",
    "dependents": "no",
    "phoneservice": "no",
    "multiplelines": "no_phone_service",
    "internetservice": "dsl",
    "onlinesecurity": "no",
    "onlinebackup": "yes",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "no",
    "streamingmovies": "no",
    "contract": "month-to-month",
    "paperlessbilling": "yes",
    "paymentmethod": "electronic_check",
    "tenure": 24,
    "monthlycharges": 29.85,
    "totalcharges": 716.4
}' http://localhost:9696/predict
```

The service will respond with a JSON object containing the churn probability and the prediction:

```json
{
  "churn": false,
  "churn_probability": 0.412
}
```

## Acknowledgements

This project is based on the code and concepts taught in the [Machine Learning Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp) by DataTalksClub. A big thank you to the authors and community for providing excellent educational materials.
