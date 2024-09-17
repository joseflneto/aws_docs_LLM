# AWS Documentation Query using a Large Language Model (LLM)

This project demonstrates how to query AWS documentation using a Large Language Model (LLM). The entire solution was developed in the AWS environment, utilizing SageMaker notebooks for model training and experimentation. The application has been containerized in Docker to facilitate future deployments.

## Getting Started

To run this project, ensure you have Docker installed, then use the following commands:

docker build -t llm-app .
docker run -p 5000:5000 llm-app

> **Note:** The application might take a few minutes to start due to the instantiation of the LLM.

## How to Use

To interact with the application, send a payload containing your query in the `query` field, as shown in the example below:

{
  "query": "What is SageMaker?"
}

The application will respond with two fields:
- `answer`: The answer to your query.
- `source_documents`: A list of documents used to generate the answer.

### Example Response

{
  "answer": "Use the following pieces of context to answer the question at the end. Please follow these rules:\n1. If you don't know the answer, don't try to make one up. Just say 'I can't find the final answer, but you may want to check the following links.'\n2. If you find the answer, provide a concise response in no more than five sentences.\n\nWhat is SageMaker?\n\nSageMaker is a fully managed machine learning service that allows data scientists and developers to quickly build and train machine learning models. It provides an integrated Jupyter notebook environment and facilitates the deployment of models into a production-ready environment.\n\nHelpful Answer:\nSageMaker is a fully managed machine learning service enabling users to build and train models using a Jupyter notebook. It integrates tools to manage the machine learning lifecycle from data preparation to deployment.",
  "source_documents": [
    "sagemaker_documentation/sagemaker-projects-whatis.md",
    "sagemaker_documentation/integrating-sagemaker.md",
    "sagemaker_documentation/deeplens-getting-started-launch-sagemaker.md"
  ]
}

In this response:
- The first part of the answer is the system prompt.
- The actual model response comes after the `Helpful Answer` label.

## Project Structure

- **`sagemaker_documentation/`**: Contains all the documents used for model training.
- **`model_development.ipynb`**: Jupyter notebook detailing the steps for model development and training.
- **`deploy.ipynb`**: Jupyter notebook with deployment testing procedures.

## Key Features

- Fully developed in the AWS environment, utilizing **SageMaker** notebooks.
- Packaged in Docker for ease of deployment.
- Allows querying of AWS documentation with responses sourced from preloaded documents.
