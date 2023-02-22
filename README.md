# League of counter

Find your lol stats easily and quickly

## Requirements

- Account League Of Legends for api key ([create](https://signup.leagueoflegends.com/fr-fr/signup/index))
- Python 3.11.2 or hight ([dowload](https://www.python.org/downloads/))

## Installation

#### Clone repository

```bash
    git clone https://github.com/Guyguy25/league-of-counter
```

#### Install all necessary packages

tkinter: `pip install tk`
pillow: `pip install pillow`

## Configuration

#### Edit the api key in `json/config.json` file

Change `YOUR_API_KEY` for [your_api_key](https://developer.riotgames.com/)

```json
{
  "api": {
    "key": "YOUR_API_KEY"
  }
}
```

_This key expires every 24 hours so remember to change it every 24 hours_

## Run script

```bash
    python index.py
```

**or**

```bash
    python3 index.py
```

## Tutorial

Enter a league of legends nickname with the right region
![App Screenshot](https://imgur.com/N0JJjm0)

## Author

- [@Guyguy25](https://github.com/Guyguy25)
