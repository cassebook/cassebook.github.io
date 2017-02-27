---
title: Sound sharing and retrieval
authors: Frederic Font, Gerard Roma, Xavier Serra
category: Chapter 10
order: 1
---

In Chapter 10 of *Computational Analysis of Sound Scenes and Events*, we give an overview of different ways to approach nowadays **sound sharing and retrieval** challenges. We describe how to build an audio database by outlining different aspects to be taken into account. We discuss metadata-based descriptions of audio content and different searching and browsing techniques that can be used to navigate the database. In addition to metadata, we show sound retrieval techniques based on the extraction of audio features from (possibly) unannotated audio. We end the chapter by discussing advanced approaches to sound retrieval and by drawing some conclusions about present and future of sound sharing and retrieval.

Here, we provide example code that illustrate some of the concepts discussed in the chapter's main text and which provides a basis for further experimentation. The code examples and written using the [Python programming language](http://python.org) and based on open source technologies. For convenience and ease of use, code examples are provided as [Jupyter notebooks](http://jupyter.org). That facilitates modification and experimentation with the code.

You'll find the code in the corresponding [Chapter 10 code](https://github.com/cassebook/cassebook.github.io/tree/master/code/ch10) directory of Computational Analysis of Sound Scenes and Events companion website [Github repository](https://github.com/cassebook/cassebook.github.io). To run the code, please open a terminal and follow the instructions below:


* **Checkout the book companion website code repository, cd to Chapter's 10 code directory**
```
git clone https://github.com/cassebook/cassebook.github.io
cd cassebook.github.io/code/ch10/
```

* **Create python 3 virtual enviornment and activate it**
```
python3 -m venv env
source env/bin/activate
```

* **Install requirements in created environment**
```
pip install -r requirements.txt
```

* **Get a Freesound API key**. Go to [https://freesound.org/apiv2/apply/](https://freesound.org/apiv2/apply/) (requires a Freesound account) and register a new set of API credentials. Copy the alphanumeric *Client secret/Api key* value generated after requesting the credentials and paste it in the file `freesound_apikey.example.py`. Rename `freesound_apikey.example.py` to `freesound_apikey.py`.

* **Run Jupyter notebook**
```
jupyter notebook
```

Within the Jupyter notebook's interface, you should first open and run the [`create_audio_database.ipynb`](https://github.com/cassebook/cassebook.github.io/tree/master/code/ch10/create_audio_database.ipynb) notebook. This will build a local audio database of animal sounds. The created database will then be used in the [`metadata-based_retrieval.ipynb`](https://github.com/cassebook/cassebook.github.io/tree/master/code/ch10/metadata-based_retrieval.ipynb) and [`audio-based_retrieval.ipynb`](https://github.com/cassebook/cassebook.github.io/tree/master/code/ch10/audio-based_retrieval.ipynb) notebooks. You can modify the code to create other databases and experiment.
