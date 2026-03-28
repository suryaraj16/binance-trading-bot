# Binance Futures Trading Bot

## Setup

1. Install dependencies:
   pip install -r requirements.txt

2. Create `.env` file:
   API_KEY=your_key
   API_SECRET=your_secret

## Run

### Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 65000

## Features
- Market & Limit orders
- CLI validation
- Logging
- Error handling
