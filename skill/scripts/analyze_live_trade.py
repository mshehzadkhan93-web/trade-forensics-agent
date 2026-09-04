from binance_market import get_market_snapshot
from score_trade import TradeInput, analyze_trade
import json


def analyze_live_trade(symbol, side, entry, stop_loss, take_profit, leverage=1.0, position_size=None):
    trade = TradeInput(
        symbol=symbol,
        side=side,
        entry=entry,
        stop_loss=stop_loss,
        take_profit=take_profit,
        leverage=leverage,
        position_size=position_size,
    )

    structural_analysis = analyze_trade(trade)
    market_data = get_market_snapshot(symbol)

    return {
        "trade_analysis": structural_analysis,
        "live_market_data": market_data,
    }


if __name__ == "__main__":
    result = analyze_live_trade(
        symbol="BTCUSDT",
        side="long",
        entry=79200,
        stop_loss=78000,
        take_profit=82000,
        leverage=5,
        position_size=200,
    )

    print(json.dumps(result, indent=2))
