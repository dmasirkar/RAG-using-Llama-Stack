# RAG-using-Llama-Stack

In this example we will learn how build, deploy a Retrieval augmented generation (RAG) using llama stack, Ollama and Retrieval augmented generation (RAG) tool.

**We need RAG To overcome following limitations:**
    - Outdated Information
    - Limited Context
    - Hallucinations

**When to Choose RAG:**
    - Frequently changing information
    - Need for transparent sources
    - Limited specialized training data

**Whats Next ?**
    https://llama-stack.readthedocs.io/en/latest/getting_started/detailed_tutorial.html#step-4-run-the-demos
    https://llama-stack.readthedocs.io/en/latest/building_applications/rag.html

**Setup:**
**Environment Specifications**
    - 1 x RHEL 9.4 VM with NVIDIA GPU and CUDA
    - Python 3.11
    - NVIDIA drivers and CUDA pre-installed
    - NVIDIA L4 GPU

**Installation of Ollama**
   $ curl -fsSL https://ollama.com/install.sh | sh
   $ ollama run granite3.3:latest --keepalive 600m
   $ ollama ps
   NAME                ID          SIZE      PROCESSOR    UNTIL             
  granite3.3:latest    fd429f23b909    7.3 GB    100% CPU     10 hours from now 

**Installation of Llama Stack And Llama Stack client**

**Install uv**
  $ curl -LsSf https://astral.sh/uv/install.sh | sh

**Setup python virtual environment**
  $ uv venv myenv --python 3.12
  $ source myenv/bin/activate

**Install llama stack and llama stack client**
$ uv pip install llama-stack

**Now let’s build and run the Llama Stack config for Ollama.** 
    $ INFERENCE_MODEL=llama3.2:3b llama stack build --template ollama --image-type venv --run

**You will see output like below:**
  INFO:     Application startup complete.
  INFO:     Uvicorn running on http://['::', '0.0.0.0']:8321 (Press CTRL+C to quit)

**To run demo example refer following**

(rag-demo) $ python rag-tool-demo.py 
rag_tool> Ingesting document: https://llama-stack.readthedocs.io/en/latest/index.html

**Inputs:**
    [UserMessage(content='What does llama stack provides?', role='user', context=None)]
**Output:**
    'Llama Stack is a unified API layer for Inference, RAG, Agents, Tools, Safety, Evals, and Telemetry. It provides a plugin architecture to support various environments like local development, on-premises, cloud, and mobile. Llama Stack also offers prepackaged verified distributions which can be used quickly and reliably in any environment. The tool provides multiple developer interfaces like CLI and SDKs for Python, Node, iOS, and Android, as well as standalone applications to build production-grade AI applications.'


 
**References**
    [API Reference for the Llama Stack API specification](https://llama-stack.readthedocs.io/en/latest/references/api_reference/index.html)
    [Python SDK Reference](https://llama-stack.readthedocs.io/en/latest/references/python_sdk_reference/index.html)
    [Llama Stack  Documentation ](https://llama-stack.readthedocs.io/en/latest/index.html)

