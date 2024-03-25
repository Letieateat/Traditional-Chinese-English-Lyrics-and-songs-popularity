<h1 align="center">Welcome to Traditional-Chinese-English-Lyrics-and-songs-popularity 👋</h1>
<p>
  <a href="https://opensource.org/license/mit" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>

> Our project examines Traditional Chinese lyrics, comparing them to English lyrics in terms of semantics and sentiment analysis. We also investigate the relationship between lyrics and a song's popularity.


## Project Dependencies
First, make sure you have Python 3.10.12 installed. You can download it from the [Python website](https://www.python.org/downloads/) or install it via a package manager like [Anaconda](https://www.anaconda.com/products/distribution).
To run the code in this project, you'll need to install several Python libraries. 

### Installation Instructions

- `Python 3.10.12` or higher (You'll need to set up a virtual environment to run Lyricsgenius in python 3.7)
- `Jieba-tw`: Library for tokenization in Traditional Chinese.
- `TCSP`: Library for Traditional Chinese text processing, providing stopwords list.
- `Umap-learn`: Library for dimension reduction.
- `Spotipy`: Library for interacting with the Spotify API.
- `Lyricsgenius`: Library for fetching lyrics from the Genius website.  (You'll need to set up a virtual environment to run Lyricsgenius in python 3.7)
- `SpaCy`: Library for NLP（tokenization) tasks.
- `NLTK`: Library for getting stop words list in English.
- `Sentence-transformers`: Library for computing dense vector representations of sentences or paragraphs.
- `Kaleido`: Library for static image export from plotly figures.

Once Python is installed, you can install the other dependencies using pip.

```bash
!pip install git+https://github.com/APCLab/jieba-tw.git
!pip install TCSP
!pip install umap-learn
!pip install spotipy --upgrade
!pip install lyricsgenius
!pip install spaCy
python -m spacy download en_core_web_sm
!pip install nltk
!pip install sentence-transformers
!pip install -U kaleido
```

## Setting Up a Virtual Environment with conda

To manage dependencies and ensure compatibility, it's recommended to set up a virtual environment with Python 3.7 when using Lyricsgenius.
For more information on managing environments with conda, refer to the "Managing environments" on conda: 
https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment

## References 



## Author

👤 **Ling Yan Li and Stephen Buttner**

* Github: [@Leticiaeat](https://github.com/Leticiaeat)
* Github: [@sbuttner](https://github.com/sbuttner)
  
## 📝 License

Copyright © 2024 <br />
This project is [MIT](https://opensource.org/license/mit) licensed.
