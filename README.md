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
### Choose LLM for Chatbot, Goto advance_rag_app.py file and open in code editor 
goto code line 68:

```python
index = build_sentence_window_index(
    [document],
    #llm=OpenAI(model="gpt-3.5-turbo", temperature=0.1,api_key=key),
    #llm = GPT4All("mistral-7b-openorca.gguf2.Q4_0.gguf"),
    llm = GPT4All(model=r'C:\Users\91941\.cache\gpt4all\mistral-7b-openorca.gguf2.Q4_0.gguf'), #Replace this path with your model path
    save_dir="./sentence_index",
)
```
1. if you want to use OpenAI LLM then uncomment code line 70 and comment 72 line
2. if you want to use opensource LLM mistral 7b through gpt4all
  Run below python file to download gpt4all model locally
```python
Python download_gpt4all_model.py
```
4. then you need to update path for model in code line 72 as per your machine path
   
   

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


