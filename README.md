# Civil-civic

CivilCivic is an AI-driven Retrieval-Augmented Generation (RAG) application designed to be your go-to resource for all civil engineering queries. Unlike generic search engines, CivilCivic provides expert guidance, specifically tailored to the practical aspects of civil engineering, delivering insights that are often unavailable on conventional platforms like Google.

# Why CivilCivic?
CivilCivic is not just another search tool. It’s designed to address the unique challenges of civil engineering by providing:

Practical Guidance: Our model is trained on real-world instructions and practical advice from experienced civil engineering professors, making it the perfect companion for students, professionals, and researchers.
Expert Knowledge: The data in CivilCivic comes from validated, high-quality sources, ensuring you get accurate and up-to-date answers to your civil engineering questions.
Comprehensive Coverage: From construction techniques to material properties, structural design, surveying, and project management, CivilCivic covers a wide array of topics.

# How CivilCivic Works
CivilCivic employs the latest Retrieval-Augmented Generation (RAG) model, which combines a retrieval system and a powerful language model to deliver precise and contextually relevant answers:

Query Processing: Enter your question or query on any civil engineering topic.
Retrieval: CivilCivic searches through a vast database of civil engineering documents, practical instructions, and professor-verified notes.
Generation: Using the RAG model, it provides an answer that combines retrieved data with the expertise encoded in the language model.

``` wsl/linux
git clone https://github.com/vardahkhalid/Civil-civic
```
Navigate to civil civic
``` wsl/linux
cd examples/pipelines/demo-questuion-answering/civilcivic
```
create you gemini-apikey and paste it in .env file

Build the Docker Image
```wsl/linus
docker build -t rag .
```

Run the Docker Container
```wsl/linux
docker run -v "$(pwd)/data:/app/data" -p 8000:8000 --env-file .env rag
```
install streamlit
```wsl/linux
pip-install streamlit
```
navigate to ui directory and run streamlit and run streamlitweb.py
``` wsl/linux
cd examples/pipelines/demo-question-answering/ui/streamlit run streamlitweb.py
```
get to streamlit web page via link given on wsl and just ask query there.

now setup is completed and you can just ask question there webpage

Here below is demo video of it working
[Watch the demo video](https://drive.google.com/drive/home?dmr=1&ec=wgc-drive-globalnav-goto)
