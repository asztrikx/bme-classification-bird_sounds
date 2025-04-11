# For windows runs
Its best to switch into wsl for faster runs (23->3min/epoch, 0.05->0.5it/s).
- Sanity check hanged,
- when disabled epoch bar never showed, it just loaded infinitely.
- Commenting out num_workers helped: https://stackoverflow.com/a/70949425/4404911)
- but made runs much slower

Running in windows may still be possible by commenting lines with `num_workers=num_workers,` and `persistent_workers=True` but no guarantees.

See instructions for WSL:

`wsl --install -d Ubuntu-24.04`

[Get WSL compatible driver:](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local)

`wsl -d Ubuntu-24.04`
- `sudo apt install python3.12-venv python3-pip ffmpeg`
- Copy data folder
- Symlink main, .env, requirements

# To run the project
Download dataset from [BirdCLEF 2024](https://www.kaggle.com/competitions/birdclef-2024/data), unzip it and place the files into `./data`

Copy `.env.template` and rename it to `.env` and fill out the values for your wandb account

First run `data_exploration.ipynb` to
- view data analysis
- trim dataset based on data analysis

Then run `main.ipynb` to
- create spectrograms (and view them) from the remaining audios
- train on them
- run evaluations
- see application
