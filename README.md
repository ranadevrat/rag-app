# rag-app
Chatbot powered by opensource LLM and RAG


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies.

```bash
pip install -r requirements.txt
```

Goto /data directory

Update dataprovider.py by add your Hugginging face key and OpenAI key for 
```python
key = ''
hg_key =""
```
### If you want to deploy mistral LLM locally on your machine for Chatbot, Goto rag_app.py file and open in code editor 
goto code line 30:

```python
    llm = GPT4All(model=r'C:\Users\91941\.cache\gpt4all\mistral-7b-openorca.gguf2.Q4_0.gguf'), #Replace this path with your model path
```
1. if you want to use opensource LLM mistral 7b through gpt4all
  Run below python file to download gpt4all model locally
```python
Python download_gpt4all_model.py
```
4. then you need to comment existing huggingfacehub llm codeline 18 to 28:
```python
llm = HuggingFaceHub(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    model_kwargs={
        "max_new_tokens": 512,
        "top_k": 30,
        "temperature": 0.1,
        "repetition_penalty": 1.03,
    },
    huggingfacehub_api_token= hg_key,# Replace with your actual huggingface token
)
```
   
   

## Usage of Project

Run below python file to productionize Chatbot powered by opensource LLM and RAG with llama index and flask
```python
Python rag_app.py
```
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[GNU](https://choosealicense.com/licenses/gpl-3.0/)


