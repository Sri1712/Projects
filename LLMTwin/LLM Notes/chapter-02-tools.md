# CHAPTER - 02 : TOOLS

## Python ecosystem and project installation

## MLOps and LLMOps tooling

## Databases for storing unstructured and vector data

## Preparing for AWS

---

## MLOps and LLMOps Tooling:

### Hugging Face: model registry

A model registry is a centralized repository that manages ML models throughout their lifecycle. It stores models along with their metadata, version history, and performance metrics, serving as a single source of truth. In MLOps, a model registry is crucial for tracking, sharing, and documenting model versions, facilitating team collaboration. Also, it is a fundamental element in the deployment process as it integrates with continuous integration and continuous deployment (CI/CD) pipelines.

Using Hugging Face as the model registry, we can leverage its ecosystem to easily share our fine-tuned LLM Twin models with anyone. Also, by following the Hugging Face model registry interface, we can easily integrate the model with all the frameworks around the LLMs ecosystem, such as Unsloth for fine-tuning and SageMaker for inference.

---

### ZenML: orchestrator, artifacts, and metadata

ZenML acts as the bridge between ML and MLOps. Thus, it offers multiple MLOps features that make ML pipeline traceability, reproducibility, deployment, and maintainability easier. At its core, it is designed to create reproducible workflows in machine learning.

It addresses the challenge of transitioning from exploratory research in Jupyter notebooks to a production-ready ML environment. It tackles production-based replication issues, such as versioning difficulties, reproducing experiments, organizing complex ML workflows, bridging the gap between training and deployment, and tracking metadata. Thus, ZenML’s main features are orchestrating ML pipelines, storing and versioning ML pipelines as outputs, and attaching metadata to artifacts for better observability.

Instead of being another ML platform, ZenML introduced the concept of a stack, which allows you to run ZenML on multiple infrastructure options. A stack will enable you to connect ZenML to different cloud services, such as:

* An orchestrator and compute engine (for example, AWS SageMaker or Vertex AI)
* Remote storage (for instance, AWS S3 or Google Cloud Storage buckets)
* A container registry (for example, Docker Registry or AWS ECR)

ZenML acts as a glue that brings all your infrastructure and tools together in one place through its stack feature, allowing you to quickly iterate through your development processes and easily monitor your entire ML system.

The beauty of this is that ZenML doesn’t vendor-lock you into any cloud platform. It completely abstracts away the implementation of your Python code from the infrastructure it runs on. For example, in our LLM Twin use case, we used the AWS stack:

* SageMaker as our orchestrator and compute
* S3 as our remote storage used to store and track artifacts
* ECR as our container registry

However, the Python code contains no S3 or ECR particularities, as ZenML takes care of them. Thus, we can easily switch to other providers, such as Google Cloud Storage or Azure.

---

### Orchestrator

An orchestrator is a system that automates, schedules, and coordinates all your ML pipelines. It ensures that each pipeline—such as data ingestion, preprocessing, model training, and deployment - executes in the correct order and handles dependencies efficiently. By managing these processes, an orchestrator optimizes resource utilization, handles failures gracefully, and enhances scalability, making complex ML pipelines more reliable and easier to manage.

How does ZenML work as an orchestrator? It works with pipelines and steps. A pipeline is a high-level object that contains multiple steps. A function becomes a ZenML pipeline by being decorated with @pipeline, and a step when decorated with @step. This is a standard pattern when using orchestrators: you have a high-level function, often called a pipeline, that calls multiple units/steps/tasks.

Pipelines call multiple steps, forming a DAG (directed acyclic graph) of execution. Each step runs modular logic (e.g., fetch user, crawl links) and can run on different machines in the cloud. ZenML tracks every run, step, output, and log in a dashboard for debugging and monitoring. Outputs of steps become artifacts that are versioned and can store metadata. To stay flexible, core logic is kept outside ZenML so the orchestrator can be swapped later.

---

### Artifacts and metadata

ZenML transforms any step output into an artifact. First, let’s quickly understand what an artifact is. In MLOps, an artifact is any files produced during the machine learning lifecycle, such as datasets, trained models, checkpoints, or logs. Artifacts are crucial for reproducing experiments and deploying models.

We can transform anything into an artifact. For example, the model registry is a particular use case for an artifact. Thus, artifacts have these unique properties: they are versioned, sharable, and have metadata attached to them to understand what’s inside quickly. For example, when wrapping your dataset with an artifact, you can add to its metadata the size of the dataset, the train-test split ratio, the size, types of labels, and anything else useful to understand what’s inside the dataset without actually downloading it.

---

### Comet ML: experiment tracker

Training ML models is an entirely iterative and experimental process. Unlike traditional software development, it involves running multiple parallel experiments, comparing them based on predefined metrics, and deciding which one should advance to production. An experiment tracking tool allows you to log all the necessary information, such as metrics and visual representations of your model predictions, to compare all your experiments and quickly select the best model.

Other popular experiment trackers are W&B, MLflow, and Neptune. We’ve worked with all of them and can state that they all have mostly the same features, but Comet ML differentiates itself through its ease of use and intuitive interface.

---

### Opik: Prompt Monitoring

When working with LLM applications, standard logging tools are not sufficient because prompts are not simple text entries—they are complex, chained interactions where each prompt and response depends on previous ones. These interactions form traces rather than isolated logs. To debug and monitor this behavior effectively, a specialized dashboard is needed to group and visualize entire prompt traces. For this reason, the authors use Opik, an open-source tool developed by Comet. It follows Comet’s philosophy of simplicity and ease of use, which is still uncommon in the LLM tooling ecosystem. Although alternatives such as Langfuse, Galileo, and LangSmith exist, they were found to be more cumbersome to implement and use. Opik also offers a free, open-source and serverless option, giving full control over prompt monitoring.

---

## Databases for storing unstructured and vector data

MongoDB is a NoSQL database because it is fast, flexible, widely adopted, and integrates well with major cloud platforms like AWS, GCP, and Azure. It is used to store raw, unstructured text data collected from the internet before further processing. MongoDB’s popularity among large companies suggests it will remain a long-term, reliable choice.

They use Qdrant as their vector database to store processed data in embedding form for GenAI use. Qdrant is lightweight, high-performance, and widely adopted by major tech companies, making it a future-proof option. Compared to alternatives like Milvus, Pinecone, or Weaviate, Qdrant offered the best balance between speed, latency, and indexing performance for their needs.

---

## SageMaker: training and inference compute

SageMaker is an ML platform used to train and deploy ML models. An official definition is as follows: AWS SageMaker is a fully managed machine learning service by AWS that enables developers and data scientists to build, train, and deploy machine learning models at scale. It simplifies the process by handling the underlying infrastructure, allowing users to focus on developing high-quality models efficiently.

We will use SageMaker to fine-tune and operationalize the training pipeline on clusters of GPUs and to deploy our custom LLM Twin model as a REST API that can be accessed in real time from anywhere in the world.

---

## Why AWS SageMaker

Amazon Bedrock and AWS SageMaker are compared to explain their choice. Bedrock is a serverless, easy-to-use option for deploying LLMs using pre-trained models via simple API calls. It requires no infrastructure management, offers predictable per-API-call pricing, and is great for fast prototyping or teams with limited ML expertise. However, it provides only limited model choices and very little customization, since users are restricted to the models and APIs Amazon exposes.

In contrast, SageMaker is a full ML platform for building, training, and deploying custom models. It offers deep flexibility and control, making it suitable for data scientists and ML engineers who want to customize training, inference, and deployment workflows. The downside is cost and operational complexity: users pay for compute, storage, and deployed resources even when endpoints are idle, so autoscaling and cleanup are necessary to control expenses.

In this book, SageMaker is used and they wanted to expose all the underlying engineering work that tools like Bedrock abstract away. SageMaker strikes a practical balance between full control and managed convenience - more flexible than Bedrock, but simpler than fully self-managed options like EKS or ECS.
