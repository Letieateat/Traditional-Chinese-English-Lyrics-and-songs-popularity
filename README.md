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

## Get your necessary Genius and Spotify API keys

To use Spotipy and LyricsGenius, you'll need to obtain your own Genius and Spotify API keys. 
You may refer to the tutorials on Genius and Spotify for more information:
- `Genius`: https://docs.genius.com/
- `Spotify`: https://developer.spotify.com/documentation/web-api

## References 

Agatha, H., Putri, F., & Suryadibrata, A. (2024). Sentiment Analysis on Song Lyrics for Song Popularity Prediction Using BERT. Ultimatics : Jurnal Teknik Informatika, 15(2), 99-105. https://doi.org/10.31937/ti.v15i2.3420

AndyChiangSH. (2021). kkbox_crawler. GitHub. https://github.com/AndyChiangSH/2021-IT-30days/blob/main/Projects/05_AJAX_KKBOX/kkbox_crawler.py

APCLab. (2017). jieba-tw. GitHub.https://github.com/APCLab/jieba-tw

Biancofiore, G. M., Di Noia, T., Di Sciascio, E., Narducci, F., & Pastore, P. (2022). Aspect based sentiment analysis in music: A case study with Spotify. In Proceedings of the 37th ACM/SIGAPP Symposium on Applied Computing (SAC '22) (pp. 696–703). Association for Computing Machinery. https://doi.org/10.1145/3477314.3507092

Bryan Wu.  (2022). Traditional-Chinese-Stopwords-and-Punctuations-Library. GitHub.
https://github.com/bryanchw/Traditional-Chinese-Stopwords-and-Punctuations-Library/tree/main

Cozar, M. (2022, November 20). Predicting song popularity based on lyrics. LatinXinAI. https://medium.com/latinxinai/predicting-song-popularity-based-on-lyrics-fee599165be0

Jain, P. (2021, May 24). Basics of CountVectorizer. Towards Data Science. https://towardsdatascience.com/basics-of-countvectorizer-e26677900f9c

Luna, F. (2023, May 30). UMAP: An alternative dimensionality reduction technique. MCD-UNISON. https://medium.com/mcd-unison/umap-an-alternative-dimensionality-reduction-technique-7a5e77e80982

Watts, C. (2021, December 17). Extracting Song Data From the Spotify API Using Python. Towards Data Science.
https://towardsdatascience.com/extracting-song-data-from-the-spotify-api-using-python-b1e79388d50


## Author

👤 **Ling Yan Li and Stephen Buttner**

* Github: [@Leticiaeat](https://github.com/Leticiaeat)
* Github: [@sbuttner](https://github.com/sbuttner)
  
## 📝 License

Copyright © 2024 <br />
This project is [MIT](https://opensource.org/license/mit) licensed.
