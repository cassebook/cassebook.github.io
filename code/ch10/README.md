# Chapter 10: Sound sharing and retrieval

Below are the instructions to run the example code that complements Chapter 10.


* 1) Checkout the book companion website code repository
```
git clone https://github.com/ffont/cassebook.github.io.git
cd cassebook.github.io/code/ch10/
```

* 2) Create python 3 virtual enviornment and activate it
```
python3 -m venv env
source env/bin/activate
```

* 3) Install requirements
```
pip install -r requirements.txt
```

* 4) Get a Freesound API key: Go to [https://freesound.org/apiv2/apply/](https://freesound.org/apiv2/apply/) (requires a Freesound account) and register a new set of API credentials. Copy the alphanumeric *Client secret/Api key* value generated after requesting the credentials and paste it in the file `freesound_apikey.example.py`. Rename `freesound_apikey.example.py` to `freesound_apikey.py`.

* 5) Run Jupyter notebook
```
jupyter notebook
```

Within the Jupyter notebook's interface you should first open and run the [Create Audio Database](https://github.com/ffont/cassebook.github.io/tree/master/code/ch10/create_audio_database.ipynb) notebook to build a local sound database. The created database will then be used in the [Metadata-based retrieval](https://github.com/ffont/cassebook.github.io/tree/master/code/ch10/metadata-based_retrieval.ipynb) and [Audio-based retrieval](https://github.com/ffont/cassebook.github.io/tree/master/code/ch10/audio-based_retrieval.ipynb) notebooks.