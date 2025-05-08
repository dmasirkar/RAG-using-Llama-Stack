## RAG-using-Llama-Stack

In this example we will learn how to build, deploy a Retrieval augmented generation (RAG) Application using **llama stack** and **Ollama**.

**We need RAG To overcome following limitations:**
    - 

1.   Outdated Information
2.   Limited Context
3.   Hallucinations


**When to Choose RAG:**
1. Frequently changing information
2. Need for transparent sources
3. Limited specialized training data


**Setup:**
**Environment Specifications**
    1. 1 x RHEL 9.4 VM with NVIDIA GPU and CUDA
    2. Python 3.11
    3. NVIDIA drivers and CUDA pre-installed
    4. NVIDIA L4 GPU

**Installation of Ollama**
   1. $ curl -fsSL https://ollama.com/install.sh | sh
   2. $ ollama run granite3.3:latest --keepalive 600m
   3. $ ollama ps
   4. NAME                ID          SIZE      PROCESSOR    UNTIL             
   5. granite3.3:latest    fd429f23b909    7.3 GB    100% CPU     10 hours from now 

**Installation of Llama Stack And Llama Stack client**

**Install uv**
  1. $ curl -LsSf https://astral.sh/uv/install.sh | sh

**Setup python virtual environment**
  1. $ uv venv myenv --python 3.12
  2. $ source myenv/bin/activate

**Install llama stack and llama stack client**
  1. $ uv pip install llama-stack

**Now let’s build and run the Llama Stack config for Ollama.** 
  1.  $ INFERENCE_MODEL=llama3.2:3b llama stack build --template ollama --image-type venv --run

**You will see output like below:**
  1. INFO:     Application startup complete.
  2. INFO:     Uvicorn running on http://['::', '0.0.0.0']:8321 (Press CTRL+C 3. to quit)

**To run demo example refer following**

1. (rag-demo) $ python rag-tool-demo.py 
2. rag_tool> Ingesting document: https://llama-stack.readthedocs.io/en/latest/index.html

**Inputs:**
   1.  [UserMessage(content='What does llama stack provides?', role='user', context=None)]
**Output:**
    1. 'Llama Stack is a unified API layer for Inference, RAG, Agents, Tools, Safety, Evals, and Telemetry. It provides a plugin architecture to support various environments like local development, on-premises, cloud, and mobile. Llama Stack also offers prepackaged verified distributions which can be used quickly and reliably in any environment. The tool provides multiple developer interfaces like CLI and SDKs for Python, Node, iOS, and Android, as well as standalone applications to build production-grade AI applications.'

**Whats Next ?**
    1. https://llama-stack.readthedocs.io/en/latest/getting_started/detailed_tutorial.html#step-4-run-the-demos
    2. https://llama-stack.readthedocs.io/en/latest/building_applications/rag.html
 
**References**
    1. [API Reference for the Llama Stack API specification](https://llama-stack.readthedocs.io/en/latest/references/api_reference/index.html)
    2. [Python SDK Reference](https://llama-stack.readthedocs.io/en/latest/references/python_sdk_reference/index.html)
    3. [Llama Stack  Documentation ](https://llama-stack.readthedocs.io/en/latest/index.html)

