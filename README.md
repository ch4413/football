# Introduction 
MLS season modelling

# Getting Started

0. Clone repo and download supporting data into `data`

1. Create `env` and install requirements 

```
pip install -r requirements.txt
```

2. Install `footballanalysis` package

```{python}
cd football

pip install -e .

```

3. Run Notebooks for analysis:

#### EXPLORING THE FIRST SEASON
* Q1, 2, 3: notebooks\S1_123_season_1_analysis.ipynb
* Extra analysis of key players and XG: notebooks/S1_X_additional_analysis.ipynb

#### PREDICTING THE SECOND SEASON
* Q1: notebooks/S2_1_season_2_bayes_predictions.ipynb (simple Bayes), notebooks/S2_1_season_2_bayes_lm_prediction.ipynb (improved LM)

* Q2: notebooks/S2_2_season_2_plot_predictions.ipynb



# Build and Test
Not build or test scripts added

# Contribute

christopher.hughes@bath.edu