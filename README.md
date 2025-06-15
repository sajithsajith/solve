# AI-Powered Math Problem Solver

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)

An efficient AI-powered application that solves complex math problems directly from screenshots. It leverages a multi-LLM "self-correction" pipeline to ensure high accuracy and provides detailed, step-by-step solutions.

## Overview

This project tackles the challenge of automated math problem-solving by utilizing the unique strengths of multiple large language models (LLMs). The core idea is that different LLMs, trained on diverse datasets, approach problems in unique ways. This application orchestrates them in a two-stage process:

1.  **Parallel Solving:** A math problem from a screenshot is sent to multiple AI models (OpenAI GPT, Google Gemini, Anthropic Claude) simultaneously.
2.  **Iterative Validation:** The initial, often varied, answers from all models are collected and fed back into each model as context. This "feedback loop" prompts the models to re-evaluate the problem, consider alternative solutions, and converge on a single, validated, and correct answer.

This iterative validation mechanism has proven to be highly effective, turning divergent initial outputs into a consistent and accurate final solution.

## Key Features

- **Solve from Screenshots:** Simply drop a PNG screenshot of a math problem into a folder.
- **Multi-LLM Parallel Processing:** Utilizes OpenAI GPT, Google Gemini, and Anthropic Claude (via AWS Bedrock) for robust and diverse problem-solving approaches.
- **Iterative Feedback & Validation:** A unique pipeline that uses the initial answers as feedback to achieve a validated consensus on the correct solution.
- **Step-by-Step Explanations:** Delivers clear, detailed steps for understanding how the final answer was derived.
- **Automated File Management:** Processed screenshots are automatically moved to a `completed` folder to keep the input directory clean.

## How It Works

The application follows a sophisticated workflow to ensure accuracy:

1.  **Ingestion:** The application monitors a specified directory for new PNG screenshots.
2.  **Parallel Processing (Round 1):** The extracted math problem is sent in parallel to all configured AI pipelines.
3.  **Response Aggregation:** The application gathers the independent, step-by-step solutions from each model.
4.  **Feedback & Validation (Round 2):** A special "conclusion prompt" is constructed, containing the original problem and all the different answers from Round 1. This prompt is sent back to all the models.
5.  **Consensus & Final Answer:** With the context of other proposed solutions, the models re-evaluate their work, leading to a convergence on the correct answer.
6.  **Cleanup:** The final, validated solution is returned, and the processed screenshot is moved to a `completed` folder with a randomized filename.

## Project Structure

```
.
├── prompt/
│   └── prompts.py           # Stores the base and conclusion prompts for AI models.
├── service/
│   ├── solve.py             # Main orchestration logic for running AI pipelines.
│   ├── azure_openai.py      # Integration with Azure OpenAI GPT models.
│   ├── bedrock_anthropic.py # Integration with Anthropic Claude via AWS Bedrock.
│   └── google_gemini.py     # Integration with Google Gemini models.
├── utils/
│   └── file_utils.py        # Utilities for file handling and image processing.
├── .env.example             # Example environment variables file.
├── requirements.txt         # Project dependencies.
└── test.ipynb               # Jupyter Notebook for demonstrating the workflow.
```

## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

- Python 3.12 or higher
- API keys and credentials for:
  - Azure OpenAI
  - AWS (for Bedrock)
  - Google Cloud (for Gemini)

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Set Up a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
# Create a virtual environment
python -m venv venv

# Activate it
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root of the project by copying the example file.

```bash
cp .env.example .env
```

Now, open the `.env` file and add your API keys and other configuration details.

```ini
# .env

#Azure
AZURE_API_KEY="YOUR_AZURE_OPENAI_API_KEY"
AZURE_API_VERSION="YOUR_AZURE_OPENAI_API_VERSION"
AZURE_ENDPOINT="YOUR_AZURE_OPENAI_ENDPOINT"

#AWS
BEDROCK_REGION="YOUR_AWS_BEDROCK_REGION"
BEDROCK_ACCESS_KEY_ID="YOUR_AWS_ACCESS_KEY_ID"
BEDROCK_SECRET_ACCESS_KEY="YOUR_AWS_SECRET_ACCESS_KEY"

#Google
GEMINI_API_KEY="YOUR_GOOGLE_GEMINI_API_KEY"
```

## Usage

1.  **Place Screenshots:** Add one or more PNG files containing math problems into the designated input directory (e.g., `screenshots/`).
2.  **Run the Workflow:** Open and execute the cells in the `test.ipynb` notebook. The notebook guides you through the process of loading an image, running the solving pipeline, and viewing the results.
3.  **Review the Solution:** The final, validated step-by-step solution will be printed in the notebook's output.
4.  **Check Processed Files:** The original screenshot will be moved from the input directory to the `completed/` directory.

## Example Prompts

The system uses two main types of prompts to orchestrate the solution process.

> **Base Prompt (Round 1):** > _"Please solve this math question. Give the correct option with answer first and then give the step by step clear explanation."_

> **Conclusion Prompt (Round 2):** > _"These are the answers given by different people for the same problem. Please, think step by step, find out the answer for the question and analyze which answer is correct and provide the answer first, followed by the explanation."_

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
