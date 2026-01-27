# Chapter 1 – Understanding LLM Twin Architecture

**Source:**  
*LLM Engineer’s Handbook*  
Paul Iusztin & Maxime Labonne  

> ⚠️ Disclaimer  
> These are my personal study notes and summaries created for learning and future reference.  
> All concepts and ideas belong to the original authors.

---

### What is an LLM Twin?

An **LLM Twin** is an AI character that incorporates your writing style, voice, and personality into a large language model (LLM).

Instead of a generic LLM trained on the entire internet, an LLM Twin is **fine-tuned on data from a single individual**, creating a digital version of that person.

This works because an LLM reflects the data it is trained on:
- Train it on Shakespeare → it writes like Shakespeare  
- Train it on your writing → it writes like *you*

This phenomenon is known as **style transfer**, and it is also common in image generation models.

---

## Planning the MVP of an LLM Twin Product

An **MVP (Minimum Viable Product)** is the simplest version of a product that allows you to:
- Attract early users
- Validate the product idea
- Collect real-world feedback

### Why MVPs are powerful

- **Accelerated time-to-market**  
  Launch quickly and gain early traction

- **Idea validation**  
  Test with real users before heavy investment

- **Market research**  
  Learn what resonates with your target audience

- **Risk minimization**  
  Reduce wasted time and resources on unproven ideas

---

## Building Production-Ready ML Systems

Training a model is often the *easiest* part of building an ML system.

The real complexity lies in engineering reliable **data, training, and inference pipelines**.

### Key considerations

- Ingesting, cleaning, and validating fresh data
- Separating training and inference setups
- Computing and serving features correctly
- Serving models in a cost-effective manner
- Versioning and tracking datasets and models
- Monitoring infrastructure and model performance
- Deploying on scalable infrastructure
- Automating training and deployment workflows

# ML Pipelines for ML Systems

The solution is based on creating a clear and straightforward mind map that any team or person can follow to compute the features, train the model, and make predictions. Based on these three critical steps that any ML system requires, the pattern is known as the FTI pipeline.  

The pattern suggests that any ML system can be boiled down to these three pipelines: feature, training, and inference (similar to the DB, business logic, and UI layers from classic software). This is powerful, as we can clearly define the scope and interface of each pipeline. Also, it’s easier to understand how the three components interact.  

---

## The Feature Pipeline

The feature pipeline takes raw data as input, processes it, and outputs the features and labels required by the model for training or inference. Instead of directly passing them to the model, the features and labels are stored inside a feature store. Its responsibility is to store, version, track, and share the features. By saving the features in a feature store, we always have a state of our features. Thus, we can easily send the features to the training and inference pipelines.  

---

## The Training Pipeline

The training pipeline takes the features and labels from the features stored as input and outputs a train model or models. The models are stored in a model registry. Its role is similar to that of feature stores, but this time, the model is the first-class citizen. Thus, the model registry will store, version, track, and share the model with the inference pipeline.  

---

## The Inference Pipeline

The inference pipeline takes as input the features and labels from the feature store and the trained model from the model registry. With these two, predictions can be easily made in either batch or real-time mode. As this is a versatile pattern, it is up to you to decide what you do with your predictions. If it’s a batch system, they will probably be stored in a DB. If it’s a real-time system, the predictions will be served to the client who requested them. Additionally, the features, labels, and models are versioned. We can easily upgrade or roll back the deployment of the model. For example, we will always know that model v1 uses features F1, F2, and F3, and model v2 uses F2, F3, and F4. Thus, we can quickly change the connections between the model and features.  

---

## Benefits of the FTI Architecture

- As you have just three components, it is intuitive to use and easy to understand.  
- Each component can be written into its tech stack, so we can quickly adapt them to specific needs, such as big or streaming data. Also, it allows us to pick the best tools for the job.  
- As there is a transparent interface between the three components, each one can be developed by a different team (if necessary), making the development more manageable and scalable.  
- Every component can be deployed, scaled, and monitored independently.  

The final thing you must understand about the FTI pattern is that the system doesn’t have to contain only three pipelines. In most cases, it will include more. For example, the feature pipeline can be composed of a service that computes the features and one that validates the data. Also, the training pipeline can be composed of the training and evaluation components.  

---

## Listing the Technical Details of the LLM Twin Architecture

### The Requirements of the ML System from a Purely Technical Perspective

#### On the Data Side, We Have to Do the Following:

- Collect data from LinkedIn, Medium, Substack, and GitHub completely autonomously and on a schedule  
- Standardize the crawled data and store it in a data warehouse  
- Clean the raw data  
- Create instruct datasets for fine-tuning an LLM  
- Chunk and embed the cleaned data. Store the vectorized data into a vector DB for RAG.  

#### For Training, We Have to Do the Following:

- Fine-tune LLMs of various sizes (7B, 14B, 30B, or 70B parameters)  
- Fine-tune on instruction datasets of multiple sizes  
- Switch between LLM types (for example, between Mistral, Llama, and GPT)  
- Track and compare experiments  
- Test potential production LLM candidates before deploying them  
- Automatically start the training when new instruction datasets are available.  

#### The Inference Code Will Have the Following Properties:

- A REST API interface for clients to interact with the LLM Twin  
- Access to the vector DB in real time for RAG  
- Inference with LLMs of various sizes  
- Autoscaling based on user requests  
- Automatically deploy the LLMs that pass the evaluation step.  

---

## The System Will Support the Following LLMOps Features

- Instruction dataset versioning, lineage, and reusability  
- Model versioning, lineage, and reusability  
- Experiment tracking  
- Continuous training, continuous integration, and continuous delivery (CT/ CI/CD)  
- Prompt and system monitoring  

---

## Design the LLM Twin Architecture Using the FTI Pipeline Design

## LLM Twin Architecture (FTI Pattern)

flowchart LR

%% --------------------
%% Data Collection Pipeline
%% --------------------
subgraph DCP["Data Collection Pipeline"]
    DS1[Medium]
    DS2[LinkedIn]
    DS3[GitHub]
    ETL[ETL]
    DW[(NoSQL DB)]

    DS1 --> ETL
    DS2 --> ETL
    DS3 --> ETL
    ETL --> DW
end

%% --------------------
%% Feature Pipeline
%% --------------------
subgraph FP["Feature Pipeline"]
    A1[Articles]
    A2[Posts]
    A3[Code]

    CLEAN[Clean]
    CHUNK[Chunk]
    EMBED[Embed]

    A1 --> CLEAN
    A2 --> CLEAN
    A3 --> CLEAN
    CLEAN --> CHUNK
    CHUNK --> EMBED
end

DW --> A1
DW --> A2
DW --> A3

%% --------------------
%% Logical Feature Store
%% --------------------
subgraph LFS["Logical Feature Store"]
    IDS[(Instruct Dataset)]
    VDB[(Vector DB)]
    RC[Retrieval Client]

    IDS --- VDB
    RC --> VDB
end

EMBED --> IDS
EMBED --> VDB

%% --------------------
%% Training Pipeline
%% --------------------
subgraph TP["Training Pipeline"]
    FT[LLM Fine-tuning]
    EXP[Experiment Tracker]
    TEST[Test LLM Candidate]
end

IDS -->|Fine-tuning Data| FT
FT --> TEST
FT --> EXP

%% --------------------
%% Model Registry
%% --------------------
MR[(Model Registry)]
TEST -->|LLM Production Candidate| MR

%% --------------------
%% Inference Pipeline
%% --------------------
subgraph IP["Inference Pipeline"]
    DEPLOY[Deploy]
    LLM[LLM Twin]
    RC2[Retrieval Client]
    API[REST API]
    MON[Prompt & System Monitoring]
end

MR -->|Accepted LLM| DEPLOY
DEPLOY --> LLM

VDB -->|RAG Data| RC2
RC2 --> LLM

LLM --> API
LLM --> MON


### Data Collection Pipeline

The data collection pipeline involves crawling your personal data from Medium, Substack, LinkedIn, and GitHub. As a data pipeline, we will use the extract, load, transform (ETL) pattern to extract data from social media platforms, standardize it, and load it into a data warehouse. The output of this component will be a NoSQL DB, which will act as our data warehouse. As we work with text data, which is naturally unstructured, a NoSQL DB fits like a glove.  

The collected digital data is binned into three categories:  

- Articles (Medium, Substack)  
- Posts (LinkedIn)  
- Code (GitHub)  

---

### Feature Pipeline

The feature pipeline’s role is to take raw articles, posts, and code data points from the data warehouse, process them, and load them into the feature store.  

It processes three types of data differently: articles, posts, and code  

It contains three main processing steps necessary for fine-tuning and RAG: cleaning, chunking, and embedding  

It creates two snapshots of the digital data, one after cleaning (used for fine-tuning) and one after embedding (used for RAG)  

It uses a logical feature store instead of a specialized feature store  

The system uses a vector database as a logical feature store, avoiding the need for a separate specialized feature store. Although the vector DB lacks native training dataset concepts, it can function as a NoSQL database, allowing direct access to data points via IDs and collections without vector search. Retrieved data is wrapped into versioned, trackable artifacts for offline training, while the inference pipeline queries the vector DB online using vector search for additional context. This setup works well because artifacts suit training workflows and vector databases are optimized for real-time inference. By focusing on a clean interface and hiding system complexity, the design aligns neatly with the FTI pattern.  

---

### Training Pipeline

The training pipeline consumes instruct dataset artifacts from the feature store to fine-tune an LLM and store the resulting weights in a model registry. Initially, data scientists run multiple experiments, tracking metrics and hyperparameters with an experiment tracker to select the best production candidate. Once optimal hyperparameters are identified, the process becomes fully automated through continuous training.  

A testing pipeline then evaluates the candidate model against stricter criteria, followed by a recommended manual approval step before production deployment. Using an ML orchestrator, the system can automatically trigger data collection, feature processing, training, and deployment pipelines as new data becomes available.  

---

### Inference Pipeline

The inference pipeline loads a fine-tuned LLM from the model registry and uses the logical feature store’s vector database to perform RAG for incoming REST API queries. It combines user queries with retrieved context to generate responses using the LLM. All queries, enriched prompts, and outputs are sent to a prompt monitoring system for analysis, debugging, and alerting. While the interface follows the FTI architecture, the pipeline includes LLM-specific components such as vector retrieval clients, prompt templates, and prompt monitoring tools.

## Personal Takeaways

- Vector databases can double as logical feature stores for LLM systems  
- The FTI pattern maps cleanly to LLM + RAG architectures  
- Prompt monitoring is a first-class LLMOps concern  
- Continuous training enables scalable personalization