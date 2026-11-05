# CS 621 — Data Analytics

Ball State University · Instructor: Fu-Shing Sun  
Student work by Leo Newton

A software-focused survey of the data science pipeline: ingest data, engineer and clean it, compute analytics and models, and visualize results. Coursework is implemented primarily in Python with Jupyter notebooks, following [*Python for Data Analysis*](https://wesmckinney.com/book/) by Wes McKinney.

---

## Table of Contents

- [Overview](#overview)
- [Repository Layout](#repository-layout)
- [Environment Setup](#environment-setup)
- [Tech Stack](#tech-stack)
- [Course Pipeline](#course-pipeline)
- [Modules](#modules)
  - [Module 1 — Introduction to Data Analytics](#module-1--introduction-to-data-analytics)
  - [Module 2 — Python & Pandas Foundations](#module-2--python--pandas-foundations)
  - [Module 3 — Data Structures](#module-3--data-structures)
  - [Module 4 — Data Ingestion](#module-4--data-ingestion)
  - [Module 5 — Data Engineering](#module-5--data-engineering)
  - [Module 6 — Numerical Data](#module-6--numerical-data)
  - [Module 7 — Non-Numerical / Categorical Data](#module-7--non-numerical--categorical-data)
  - [Module 8 — Time Series Data](#module-8--time-series-data)
  - [Module 9 — Spatial Data](#module-9--spatial-data)
  - [Module 10 — Web & Social Network Data](#module-10--web--social-network-data)
  - [Module 11 — Text Processing](#module-11--text-processing)
  - [Module 12 — Text Analytics & Project Planning](#module-12--text-analytics--project-planning)
  - [Module 13 — Sentiment Analysis & Dashboards](#module-13--sentiment-analysis--dashboards)
  - [Module 14 — Machine Learning Classification](#module-14--machine-learning-classification)
  - [Module 15 — Linear Regression & MapReduce](#module-15--linear-regression--mapreduce)
- [Peer-Reviewed Project Plans](#peer-reviewed-project-plans)
- [Textbook & References](#textbook--references)
- [Utilities](#utilities)

---

## Overview

CS 621 approaches big data and analytics from a computer-science perspective: volume, velocity, and variety (and often value and veracity) create new software challenges around scalable ingestion, cleaning, modeling, and presentation.

Work in this repository covers:

| Theme | What was done |
| --- | --- |
| Foundations | Big data concepts, data types/formats, and the four-stage analytics pipeline |
| Core Python | Lists, dicts, sets, tuples, NumPy arrays, Pandas Series/DataFrames |
| Ingestion | MySQL, CSV, JSON, XML, TinyDB (NoSQL) |
| Engineering | Missing values, duplicates, concat/merge |
| Analytics by data type | Numerical, categorical, time series, spatial, web/social, text |
| NLP | Tokenization, stop words, stemming/lemmatization, POS tagging, word clouds, lexicon sentiment, spaCy NER |
| ML | Decision-tree digit classification; linear regression with MAE/MSE |
| Systems | MapReduce-style word count; Streamlit text dashboard |
| Capstone planning | Peer-reviewed data analytics project plans |

---

## Repository Layout

```
CS_621_Data_Analytics/
├── Module_1/ … Module_15/   # Lecture slides, notebooks, datasets, homework
├── project_plans/           # Peer-reviewed project plan PDFs
├── src/                     # Package skeleton (uv project)
├── html_to_ipynb.py         # Convert exported notebook HTML → .ipynb
├── pyproject.toml           # Dependencies (managed with uv)
└── README.md
```

Each `Module_N/` folder typically contains lecture PDFs/PPTX, HTML notebook exports, Jupyter notebooks (`.ipynb`), sample datasets, and short supplemental reading notes.

---

## Environment Setup

This project uses [uv](https://github.com/astral-sh/uv) and Python ≥ 3.13.

```bash
# Install dependencies into the local environment
uv sync

# Launch JupyterLab
uv run jupyter lab

# Or run a Streamlit demo (Module 13)
uv run streamlit run Module_13/streamlit_dashboard_demo.py
```

Optional: convert an HTML notebook export to `.ipynb`:

```bash
uv run python html_to_ipynb.py path/to/export.html path/to/output.ipynb
```

---

## Tech Stack

| Area | Libraries / tools |
| --- | --- |
| Core | Python 3.13, Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly, Folium, WordCloud |
| NLP | NLTK, spaCy, emoji |
| ML | scikit-learn |
| Web / docs | Beautiful Soup, lxml |
| Apps | Streamlit |
| Notebooks | JupyterLab / ipykernel |
| Packaging | uv (`pyproject.toml`) |

---

## Course Pipeline

The course is organized around a standard data science pipeline:

1. **Data sources** — databases, files, APIs, web pages, free corpora (e.g. Kaggle, Project Gutenberg)
2. **Data ingestion** — load into program-friendly structures
3. **Data engineering** — validate, clean, handle nulls/duplicates, reshape
4. **Analytics / modeling** — statistics, grouping, NLP, ML, MapReduce-style aggregation
5. **Visualization & delivery** — charts, maps, dashboards, reports, software artifacts

---

## Modules

### Module 1 — Introduction to Data Analytics

**Focus:** Why data analytics matters; big data (3Vs / 5Vs); data domains and formats; the analytics pipeline.

#### Table of Contents

1. [Course introduction & big data motivation](#m1-intro)
2. [Challenges, 3Vs / 5Vs, and who works with data](#m1-challenges)
3. [Data domains, storage, and formats](#m1-formats)
4. [Structured, semi-structured, and unstructured data](#m1-structure)
5. [Data science pipeline](#m1-pipeline)
6. [Supplemental materials](#m1-suppl)

<a id="m1-intro"></a>
**1. Course introduction** — Class framing (data analytics / data science / big data / business analytics); scale examples (social media, e-commerce, video upload rates).

<a id="m1-challenges"></a>
**2. Challenges & Vs** — Volume, velocity, variety (+ value, veracity); need for scalable, distributed software and multidisciplinary teams.

<a id="m1-formats"></a>
**3. Domains & formats** — Business, science, healthcare, web/social; storage in SQL, XML/JSON, CSV/text, multimedia (MP3/MP4/JPEG/PNG); numerical, text, temporal, spatial, binary/network/streaming views of data.

<a id="m1-structure"></a>
**4. Structure levels** — Structured (RDBMS + SQL), semi-structured (XML/JSON/CSV), unstructured (books, logs, web pages, media) and the need to engineer before analytics.

<a id="m1-pipeline"></a>
**5. Pipeline stages** — Ingestion → engineering (validation, nulls, ranges, duplicates, outliers) → analytics/modeling → visualization → deliverables (reports, software, or inputs to another pipeline).

<a id="m1-suppl"></a>
**6. Supplemental materials** — Oracle / IBM / Wikipedia big-data and data-science definitions; School of Data handbook; Kaggle; Anaconda / Jupyter install links.

**Key files:** `cs621_module_1_introduction.pdf`, `cs621_module_1_data.pdf`, `cs621_module_1_pipeline.pdf`, lecture subtitle transcripts, `Supplmental Materials.txt`

---

### Module 2 — Python & Pandas Foundations

**Focus:** First hands-on Python list work and a Pandas smoke test.

#### Table of Contents

1. [List homework — numeric summaries](#m2-lists)
2. [Categorical list work](#m2-cats)
3. [Pandas DataFrame smoke test](#m2-pandas)

<a id="m2-lists"></a>
**1. Numeric lists** — Count, sort, and range over integer samples (`homework.ipynb`).

<a id="m2-cats"></a>
**2. Categorical lists** — Frequency-style work over string categories (fruit labels).

<a id="m2-pandas"></a>
**3. Pandas intro** — Build and display a small DataFrame (`Pandas_Test.ipynb`).

**Key files:** `homework.ipynb`, `Pandas_Test.ipynb`, `sample_input.txt`

---

### Module 3 — Data Structures

**Focus:** Python and Pandas structures used throughout the rest of the course.

#### Table of Contents

1. [Lists](#m3-lists)
2. [Dictionaries](#m3-dicts)
3. [Sets](#m3-sets)
4. [Tuples](#m3-tuples)
5. [NumPy arrays](#m3-numpy)
6. [Pandas Series](#m3-series)
7. [Pandas DataFrames](#m3-df)

<a id="m3-lists"></a>
**1. Lists** — Traversal, append, `pop`.

<a id="m3-dicts"></a>
**2. Dictionaries** — Key/value access, insert, update, `.keys()` / `.values()`.

<a id="m3-sets"></a>
**3. Sets** — Uniqueness, unordered membership, union / intersection / difference.

<a id="m3-tuples"></a>
**4. Tuples** — Immutable sequences.

<a id="m3-numpy"></a>
**5. NumPy arrays** — Homogeneous typed arrays vs heterogeneous lists.

<a id="m3-series"></a>
**6. Series** — Label + integer indexing; construction from lists/dicts.

<a id="m3-df"></a>
**7. DataFrames** — Columnar tables; `head`, `iloc` / `loc`, row/column Series views, slicing.

**Key files:** `cs621_module_3_data_structures.pdf`, `module3_data_structures.html`

---

### Module 4 — Data Ingestion

**Focus:** Loading structured and semi-structured data from multiple sources; intro to document NoSQL via TinyDB.

#### Table of Contents

1. [MySQL / relational ingestion](#m4-mysql)
2. [CSV loading](#m4-csv)
3. [JSON loading](#m4-json)
4. [XML parsing](#m4-xml)
5. [TinyDB (NoSQL)](#m4-tinydb)
6. [Textbook reference](#m4-book)

<a id="m4-mysql"></a>
**1. MySQL** — Connect, cursor, `SELECT`, collect rows into Python lists/tuples.

<a id="m4-csv"></a>
**2. CSV** — Manual line parsing and `pandas.read_csv` (with and without headers).

<a id="m4-json"></a>
**3. JSON** — `json` module and `pandas.read_json`; nested student records → dicts/DataFrames.

<a id="m4-xml"></a>
**4. XML** — Parse tree, walk elements, cast text fields to integers.

<a id="m4-tinydb"></a>
**5. TinyDB** — Insert, query, update, remove; flexible document schema demo (`cs621_tinydb.html`, `cs621_nosql.pptx`).

<a id="m4-book"></a>
**6. Reference** — McKinney Ch. 6 (*Data Loading, Storage, and File Formats*).

**Key files:** `cs621_module_4_data_ingestion.pdf/.html`, `cs621_tinydb.html`, `cs621_nosql.pptx`, `iris.json`, `ris.csv`, `Data Loading and Storage Reference.txt`

---

### Module 5 — Data Engineering

**Focus:** Cleaning and preparing data before analytics.

#### Table of Contents

1. [Missing values (`None` / `NaN`)](#m5-missing)
2. [Detecting and filling nulls in Pandas](#m5-nulls)
3. [Duplicates](#m5-dupes)
4. [Concatenation and merges](#m5-combine)
5. [Textbook reference](#m5-book)

<a id="m5-missing"></a>
**1. Missingness** — `None`, `math.nan`, NumPy/Pandas NaN semantics and comparison pitfalls.

<a id="m5-nulls"></a>
**2. Null handling** — `isna` / `isnull` / `notnull`; fill defaults; drop rows with empties.

<a id="m5-dupes"></a>
**3. Duplicates** — `duplicated`, `drop_duplicates` (full-row and column-subset), `inplace` tradeoffs.

<a id="m5-combine"></a>
**4. Combine** — Row/column `concat`, index cleanup, `merge` of related frames.

<a id="m5-book"></a>
**5. Reference** — McKinney Ch. 7 (*Data Cleaning and Preparation*).

**Key files:** `cs621_module_5_data_engineering.pdf/.html`, `test.csv`, `Data Cleaning and Preparation Reference.txt`

---

### Module 6 — Numerical Data

**Focus:** Descriptive statistics and charts for numeric columns.

#### Table of Contents

1. [Custom mean / median](#m6-stats)
2. [Series / DataFrame describe APIs](#m6-describe)
3. [Box plots and outliers](#m6-box)
4. [Scatter, line, area charts](#m6-charts)
5. [Histograms & life-expectancy data](#m6-hist)
6. [Homework](#m6-hw)

<a id="m6-stats"></a>
**1. From scratch** — Implement `min`/`max`/mean/median over integer lists.

<a id="m6-describe"></a>
**2. Pandas stats** — `describe`, `median`, column sums, `idxmax` / `idxmin`.

<a id="m6-box"></a>
**3. Box plots** — From lists, Series, and DataFrame columns; outlier visibility.

<a id="m6-charts"></a>
**4. Relationship charts** — Scatter, line, area, stacked area.

<a id="m6-hist"></a>
**5. Distributions** — Gaussian simulation histogram; life-expectancy CSV histogram after NaN drop.

<a id="m6-hw"></a>
**6. Homework** — Iris workbook: load, describe, duplicates, boxplots (`Module 6 Homework.ipynb`).

**Key files:** `cs621_module_6_numerical_data.pdf`, `cs621_module_numerical_data.html`, `iris.csv`, `life_expectancy.csv`, `Module 6 Homework.ipynb`

---

### Module 7 — Non-Numerical / Categorical Data

**Focus:** Counting categories, grouping, and categorical visualization (including Seaborn).

#### Table of Contents

1. [Category frequencies with dicts](#m7-freq)
2. [Bar, pie, and donut charts](#m7-charts)
3. [Pandas `value_counts` and Series plots](#m7-vc)
4. [GroupBy aggregations](#m7-groupby)
5. [Sorting (single and multi-level)](#m7-sort)
6. [Tips dataset + Seaborn plots](#m7-tips)

<a id="m7-freq"></a>
**1. Frequencies** — Distinct categories via sets; count with dictionaries.

<a id="m7-charts"></a>
**2. Matplotlib categorical charts** — Vertical/horizontal bars, pie percentages, explode, donut.

<a id="m7-vc"></a>
**3. Pandas plotting** — `value_counts` → bar/pie from Series/DataFrame.

<a id="m7-groupby"></a>
**4. GroupBy** — Size, mean, sum, describe; two-level grouping (e.g. release date × platform; day × sex).

<a id="m7-sort"></a>
**5. Sorting** — Single-column and multi-key sorts.

<a id="m7-tips"></a>
**6. Tips + Seaborn** — Stacked/grouped bars; `stripplot` / `swarmplot` with hue.

**Key files:** `cs621_module_7_non_numerical.pdf`, `module7.ipynb`, `module7.html`, `tips.csv`

---

### Module 8 — Time Series Data

**Focus:** Datetime primitives, Pandas time series, rolling windows, and stock prices.

#### Table of Contents

1. [Python `date` / `time` / `datetime`](#m8-dt)
2. [Timedeltas and comparisons](#m8-delta)
3. [Pandas Series time index & plots](#m8-series)
4. [`date_range` and DataFrame time series](#m8-range)
5. [Rolling mean / max / min / std](#m8-roll)
6. [Stock price CSV work](#m8-stock)
7. [Textbook reference](#m8-book)

<a id="m8-dt"></a>
**1. Datetime basics** — Construct dates/times; format strings; ISO weekday/calendar; parse strings.

<a id="m8-delta"></a>
**2. Differences** — Compare dates; `timedelta` arithmetic; timestamps.

<a id="m8-series"></a>
**3. Time-indexed Series** — Line/bar plots of levels over dates.

<a id="m8-range"></a>
**4. `date_range`** — Daily index construction into a DataFrame.

<a id="m8-roll"></a>
**5. Rolling windows** — Moving average, max, min, std; overlay with raw series.

<a id="m8-stock"></a>
**6. Stocks** — Analyze `stock_px.csv` as a real time-series dataset.

<a id="m8-book"></a>
**7. Reference** — McKinney Ch. 11 (*Time Series*).

**Key files:** `cs621_module_8_time_series_data.pdf`, `Module_8_Time_Series_Data.ipynb`, `stock_px.csv`, `Time Series Data Handling.txt`

---

### Module 9 — Spatial Data

**Focus:** Choropleth maps, Folium overlays, and heatmaps.

#### Table of Contents

1. [US population & area choropleths (Plotly)](#m9-us)
2. [COVID-19 world choropleth with ISO join](#m9-covid)
3. [Folium maps (Indianapolis / US)](#m9-folium)
4. [California housing map markers](#m9-housing)
5. [Seaborn heatmaps](#m9-heat)
6. [Homework — alcohol consumption map](#m9-hw)
7. [Supplemental links](#m9-suppl)

<a id="m9-us"></a>
**1. US choropleths** — Population and area from CSV + GeoJSON state boundaries.

<a id="m9-covid"></a>
**2. Global COVID map** — Aggregate cases by country; join ISO codes; Plotly choropleth.

<a id="m9-folium"></a>
**3. Folium** — Centered local map; US choropleth via Folium APIs.

<a id="m9-housing"></a>
**4. Housing points** — Plot California housing lon/lat samples on a map.

<a id="m9-heat"></a>
**5. Heatmaps** — Custom matrices and Seaborn `heatmap` (annotations, grids, colormaps).

<a id="m9-hw"></a>
**6. Homework** — Join `alcohol.csv` with `country_iso.csv`; extremes/averages; choropleth of consumption.

<a id="m9-suppl"></a>
**7. Supplemental** — Choropleth definitions; Plotly / Folium / Seaborn heatmap docs.

**Key files:** `Module_9.ipynb`, `cs621_module_9_spatial_data.pdf`, GeoJSON/CSVs (`usa_states.json`, `indiana_counties.json`, `covid_19_world.csv`, `housing.csv`, `alcohol.csv`, …), `Suppl material.txt`

---

### Module 10 — Web & Social Network Data

**Focus:** Scraping HTML and working with tweet JSON.

#### Table of Contents

1. [HTTP fetch of a web page](#m10-http)
2. [Beautiful Soup parsing](#m10-bs)
3. [Local HTML fallback](#m10-local)
4. [Tweet JSON → dict / DataFrame](#m10-tweets)
5. [Language filter & text extract](#m10-filter)
6. [Supplemental APIs](#m10-suppl)

<a id="m10-http"></a>
**1. Fetch** — Open a URL and download HTML (noting many sites block scraping).

<a id="m10-bs"></a>
**2. Beautiful Soup** — Parse, prettify, collect `<p>` contents.

<a id="m10-local"></a>
**3. Offline HTML** — Load saved page (`bsu_data_science.html`) and repeat parsing.

<a id="m10-tweets"></a>
**4. Tweets** — Load `one_tweet.json` / tweet files into dicts and Pandas; inspect keys/values.

<a id="m10-filter"></a>
**5. Filtering** — Keep English tweets; extract text fields into lists.

<a id="m10-suppl"></a>
**6. Supplemental** — Beautiful Soup docs; X/Twitter API notes (rapidly changing); YouTube Data API.

**Key files:** `cs621_module_10_web_social_data.ipynb`, `cs621_module_10_web_social_network_data.pdf`, `bsu_data_science.html`, `one_tweet.json`, `Suppl materials.txt`

---

### Module 11 — Text Processing

**Focus:** String utilities and classical NLP preprocessing with NLTK.

#### Table of Contents

1. [String constants & case helpers](#m11-str)
2. [Character class checks](#m11-checks)
3. [Sentence & word tokenization](#m11-tok)
4. [Punctuation removal](#m11-punct)
5. [Stop-word filtering](#m11-stop)
6. [Stemming & lemmatization](#m11-stem)
7. [File-based text cleaning](#m11-file)
8. [Supplemental libraries](#m11-suppl)

<a id="m11-str"></a>
**1. Strings** — `string` constants; `lower` / `upper` / `capitalize` / `title`.

<a id="m11-checks"></a>
**2. Predicates** — `isalnum`, `isalpha`, `isdigit`, whitespace detection.

<a id="m11-tok"></a>
**3. Tokenization** — NLTK `sent_tokenize` / `word_tokenize`.

<a id="m11-punct"></a>
**4. Cleaning** — Strip punctuation with `str.translate`.

<a id="m11-stop"></a>
**5. Stop words** — NLTK English stop-word list filtering.

<a id="m11-stem"></a>
**6. Normalization** — Porter & Lancaster stemmers; WordNet lemmatizer.

<a id="m11-file"></a>
**7. Corpus files** — Process local text (e.g. Amazon reviews / Newton corpus exports).

<a id="m11-suppl"></a>
**8. Supplemental** — Project Gutenberg; NLTK, spaCy, Gensim docs.

**Key files:** `module_11_text_processing.ipynb`, `cs621_module_11_text_processing.pdf/.html`, `amazon_reviews.txt`, `bsu_text_1.txt`, `cs621_module_11_newton.txt`, `Suppl Materials.txt`

---

### Module 12 — Text Analytics & Project Planning

**Focus:** Word frequencies, word clouds, POS-tag analytics, and the peer-reviewed project plan assignment.

#### Table of Contents

1. [Word frequency pipelines](#m12-freq)
2. [Pandas Series / DataFrame frequency tables](#m12-pandas)
3. [Word clouds (plain, dict, masked)](#m12-cloud)
4. [POS tagging & tag-frequency charts](#m12-pos)
5. [Homework filters (NN / NNP)](#m12-hw)
6. [Peer-reviewed project plan](#m12-plan)

<a id="m12-freq"></a>
**1. Frequencies** — Read lines, tokenize, distinct words, count with nested loops / dicts.

<a id="m12-pandas"></a>
**2. Tabular freqs** — Series sort; `value_counts`; export `word_freq.csv`.

<a id="m12-cloud"></a>
**3. Word clouds** — From raw text (US Constitution), from frequency dicts, and with custom image masks (`heart.png`).

<a id="m12-pos"></a>
**4. POS analytics** — `pos_tag`; distinct tags; bar chart of top tags.

<a id="m12-hw"></a>
**5. Homework** — Lowercase tokenize; keep nouns tagged `NN` / `NNP`.

<a id="m12-plan"></a>
**6. Project plan** — Domain proposal structured on the pipeline (intro, sources, ingestion, engineering, analytics, visualization, deliverables, hour estimates, markups); peer feedback rubric (`Data Analytics Project Plan.txt`, `cs621_peer_reviewed_project_explanation.pdf`).

**Key files:** `module_12_text_analytics.ipynb`, `cs621_module_12_text_analytics.pdf/.html`, `constitution.txt`, `cs621_text_data_1.txt`, `word_freq.csv`, `heart.png`, project-plan PDFs under `project_plans/`

---

### Module 13 — Sentiment Analysis & Dashboards

**Focus:** Lexicon sentiment scoring, emoji handling, spaCy NER, Amazon review batch scoring, and a Streamlit text dashboard.

#### Table of Contents

1. [Lexicon-based sentiment on sample comments](#m13-lex)
2. [Emoji encode / decode / detect](#m13-emoji)
3. [spaCy named-entity recognition](#m13-ner)
4. [Amazon review preprocessing & scoring](#m13-amazon)
5. [Streamlit Text Analysis Dashboard](#m13-dash)
6. [Supplemental resources](#m13-suppl)

<a id="m13-lex"></a>
**1. Lexicon scoring** — Load Bing Liu–style positive/negative word lists; score short product/car comments.

<a id="m13-emoji"></a>
**2. Emoji** — `emoji.emojize` / `demojize` / `emoji_list` on review text.

<a id="m13-ner"></a>
**3. NER** — `en_core_web_sm` entity extraction.

<a id="m13-amazon"></a>
**4. Reviews at scale** — Lemmatize/tokenize Amazon reviews → `processed_reviews.txt`; count positive vs negative (and neutral) reviews; frequency of selected polarity words.

<a id="m13-dash"></a>
**5. Dashboard** — `streamlit_dashboard_demo.py`: paste or upload text → word cloud, frequency bar chart, POS distribution (`cs621_dashboard.pptx` / `cs621_streamlit_dashboard.pptx`).

<a id="m13-suppl"></a>
**6. Supplemental** — Sentiment lexicon hub; emoji package; spaCy NER docs.

**Key files:** `Module_13_Sentiment_Analysis.ipynb`, `streamlit_dashboard_demo.py`, `cs621_module_13_sentiment.pdf`, `positive_words`, `negative_words`, `amazon_reviews`, `processed_reviews.txt`, `module_13_live_demo.html`

---

### Module 14 — Machine Learning Classification

**Focus:** Supervised classification of handwritten digits with scikit-learn.

#### Table of Contents

1. [Digits dataset exploration](#m14-data)
2. [Train/test split from samples](#m14-split)
3. [Decision Tree training & prediction](#m14-tree)
4. [Custom digit image tests](#m14-custom)
5. [Homework — multi-classifier evaluation](#m14-hw)
6. [References](#m14-ref)

<a id="m14-data"></a>
**1. Data** — `training_digits.csv` / `test_digits.csv`: 28×28 images flattened to 784 pixels + label; class counts.

<a id="m14-split"></a>
**2. Split** — Use a portion of rows for training; hold out labels.

<a id="m14-tree"></a>
**3. Decision Tree** — `sklearn.tree.DecisionTreeClassifier` fit; predict held-out / handcrafted digits.

<a id="m14-custom"></a>
**4. Manual digits** — Predict student-drawn digit vectors; inspect misclassifications.

<a id="m14-hw"></a>
**5. Homework** — Train alternatives (e.g. Random Forest, KNN, Logistic Regression); per-digit recall/accuracy checks.

<a id="m14-ref"></a>
**6. References** — scikit-learn docs; DecisionTreeClassifier API; MNIST source.

**Key files:** `Module_14_Machine_Learning_Classification.ipynb`, `cs621_module_14_machin_learning.pdf`, `mod14.html`, `training_digits.csv`, `test_digits.csv`, `Scikit-learn Documentation.txt`

---

### Module 15 — Linear Regression & MapReduce

**Focus:** Derive and apply linear regression with error metrics; implement a MapReduce-style word count.

#### Table of Contents

1. [Hand-derived regression coefficients](#m15-hand)
2. [Fit line, residuals, MAE / MSE / RMSE](#m15-err)
3. [scikit-learn `LinearRegression`](#m15-sklearn)
4. [Homework — flights regression](#m15-flights)
5. [MapReduce word count](#m15-mr)
6. [MapReduce on cleaned reviews](#m15-mr-reviews)
7. [References](#m15-ref)

<a id="m15-hand"></a>
**1. From scratch** — Implement mean, \(w_1\), \(w_0\) for simple linear regression; scatter + fitted line.

<a id="m15-err"></a>
**2. Errors** — Visual residual segments; mean absolute error, mean squared error, RMSE.

<a id="m15-sklearn"></a>
**3. sklearn API** — Fit `LinearRegression`; inspect `coef_` / `intercept_`; predicted-vs-actual plot.

<a id="m15-flights"></a>
**4. Homework** — Load/clean `flights_1000.csv`; define X/y; train; report parameters and error (`module_15_regression_analysis.ipynb`).

<a id="m15-mr"></a>
**5. MapReduce demo** — Mapper `(word, 1)` → shuffle/group → reducer sum; sort by key/value (`s621_map_reduce.ipynb`).

<a id="m15-mr-reviews"></a>
**6. Applied MapReduce** — Word count over Module 11 cleaned review text (`cs621_module_11_newton.txt`).

<a id="m15-ref"></a>
**7. References** — `LinearRegression` and `mean_absolute_error` docs.

**Key files:** `module_15_regression_analysis.ipynb/.html`, `s621_map_reduce.ipynb/.html`, `cs621_module_15_regression.pdf`, `flights_1000.csv`, `Linear Regression and Mean Absolute Error Guide.txt`

---

## Peer-Reviewed Project Plans

Module 12’s planning assignment and peer reviews live in `project_plans/`:

| Document | Notes |
| --- | --- |
| `CS 621 Final Project.pdf` | Final project materials |
| `CS621_RideWise_Project_Plan.pdf` | RideWise domain plan |
| `Polymarket Whale Consensus & Smart Money Analytics.pdf` | Prediction-market analytics plan |
| `NSullivan Data Analysis Plan.pdf` | Peer plan |
| `CS621 - Module 12 - Peer Reviewed Project Plan - Data Analytics - Henry Thompson.pdf` | Peer plan |
| `Projectplan.pdf` | Additional plan draft |

Plans follow the course pipeline blueprint: introduction, data sample, per-stage work + hour estimates + markup visuals, deliverables, and written peer feedback.

---

## Textbook & References

Primary text:

- Wes McKinney, [*Python for Data Analysis*](https://wesmckinney.com/book/)  
  - Ch. 6 — Data Loading, Storage, and File Formats  
  - Ch. 7 — Data Cleaning and Preparation  
  - Ch. 11 — Time Series  

Other frequently used references appear in each module’s `Suppl*.txt` notes (Plotly, Folium, NLTK, spaCy, scikit-learn, Beautiful Soup, Project Gutenberg, sentiment lexicons, etc.).

---

## Utilities

| File | Purpose |
| --- | --- |
| `html_to_ipynb.py` | Convert Jupyter HTML exports back into `.ipynb` notebooks |
| `pyproject.toml` / `uv.lock` | Reproducible dependency set for the course environment |

---

*CS 621 Data Analytics — Ball State University*
