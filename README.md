# To run the project
Download dataset from [BirdCLEF 2024](https://www.kaggle.com/competitions/birdclef-2024/data), unzip it and place the files into `./data`

Copy `.env.template` and rename it to `.env` and fill out the values for your wandb account

Run `data_exploration.ipynb` to
- view data analysis
- trim dataset based on data analysis

Run `main.ipynb` to
- create spectrograms (and view them) from the remaining audios
- train on them
- run evaluations
- see application