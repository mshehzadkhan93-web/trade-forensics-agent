# Trade Forensics Agent

A forensic risk-analysis tool for cryptocurrency trades that evaluates a proposed or completed setup using live Binance market data and structured trade scoring.

This project is designed to answer a more useful question than “Should I buy or sell?” It asks: “What can realistically break this trade, how exposed is it to risk, and how strong is the setup before execution?”

## What It Does

Trade Forensics Agent analyzes a trade using:

- trading pair and direction
- entry, stop-loss, and take-profit levels
- leverage
- position size
- live spot and futures market conditions
- risk/reward ratio
- spread, volatility, funding, and basis data

It produces a structured forensic assessment that helps users understand whether a trade is strong, acceptable, high risk, or critical risk.

## Key Features

- Pre-trade trade integrity scoring
- Post-trade failure diagnosis
- Live Binance market-data integration
- Risk/reward evaluation
- Stop-distance and leverage analysis
- Market context checks including spread, funding, and futures/spot basis
- CLI-based execution for trade review
- Agent/skill packaging for Claude-style workflows

## Live Binance Market-Data Integration

The project connects to Binance REST endpoints for live market context, including:

- spot bid/ask book ticker
- 24-hour ticker data
- futures mark price and premium index data
- funding rate
- open interest

This data is used to adjust the trade assessment based on real-time market conditions rather than relying on static assumptions.

## Trade Integrity Score

Each trade is assigned a score from 0 to 100.

Score bands:

- 80–100: Strong
- 60–79: Acceptable
- 40–59: High Risk
- 0–39: Critical Risk

The score is based on the trade’s structure and then adjusted by live conditions when available, such as:

- large entry deviation from live price
- elevated spread
- funding pressure
- abnormal futures/spot basis

## Risk Analysis

The agent evaluates several risk dimensions, including:

- risk/reward ratio
- leverage appropriateness
- stop-loss placement relative to entry
- leveraged stop exposure
- live market alignment
- execution quality indicators such as spread
- broader market pressure from funding or basis shifts

This makes the tool useful for trade review, decision support, and risk awareness rather than signal generation.

## Installation

Clone the repository:

```bash
git clone https://github.com/mshehzadkhan93-web/trade-forensics-agent.git
cd trade-forensics-agent
```

The project does not require a package manager install to run the basic CLI workflow. Python 3 is used for the scripts.

## CLI Usage Example

From the scripts directory:

```bash
cd skill/scripts
python3 trade_cli.py BTCUSDT long 79400 78800 81000 --leverage 5 --position-size 200
```

This produces a structured analysis for a BTCUSDT long trade with the given parameters.

You can also call the analysis module directly if needed.

## Claude Skill Installation Using the ZIP

To install this project as a Claude-compatible skill package:

1. Create the ZIP archive for the skill folder from the repository root:

```bash
zip -r trade-forensics-skill.zip skill -x "skill/scripts/*.backup" "*/__pycache__/*" "*.pyc"
```

2. Import or add the generated archive to your Claude skill environment or skill manager.
3. Ensure the skill files are preserved as packaged content.
4. Use the included instructions and scripts as a local forensic trade analysis skill.

The repository includes the packaged skill content under the skill directory and the exact skill instructions are defined in skill/SKILL.md.

## Example Output

```json
{
  "trade_analysis": {
    "symbol": "BTCUSDT",
    "side": "LONG",
    "trade_integrity_score": 100,
    "risk_level": "Strong",
    "risk_reward_ratio": 2.67,
    "stop_distance_pct": 0.76,
    "target_distance_pct": 2.02,
    "leveraged_stop_exposure": 3.78,
    "leverage": 5.0,
    "position_size": 200.0,
    "findings": [
      "Risk/reward is strong.",
      "Leverage is controlled."
    ],
    "entry_vs_live_pct": 0.113,
    "futures_spot_basis_pct": -0.0391,
    "live_score_adjustment": 0,
    "live_findings": [],
    "live_context": {
      "spot_price": 79310.02,
      "mark_price": 79279.0,
      "funding_rate": 4.915e-05,
      "spread_pct": 1.2608748099862577e-05,
      "open_interest": 109179.361
    },
    "final_live_adjusted_score": 100
  }
}
```

This output illustrates the project’s methodology: a structural trade review, then a live-market adjustment layer using Binance data.

## Project Structure

```text
trade-forensics-agent/
├── skill/
│   ├── SKILL.md
│   └── scripts/
│       ├── analyze_live_trade.py
│       ├── binance_market.py
│       ├── score_trade.py
│       ├── trade_cli.py
│       └── score_trade.py.backup
├── docs/
├── examples/
├── LICENSE
├── README.md
└── trade-forensics-skill.zip   # generated archive for skill packaging
```

## Limitations

This project is a risk-analysis and forensic diagnosis tool, not a trade-execution engine or guaranteed predictive system.

Important limitations:

- Binance market data is live but may be delayed or temporarily unavailable.
- Network or API issues can affect live retrieval.
- The tool does not guarantee that a trade will succeed or fail.
- Trade scoring is based on risk structure and market context, not future price certainty.
- It cannot assess every macro or off-exchange variable that may affect execution.

## Disclaimer

This project is for research, analysis, and educational use only.

It does not guarantee profitable trades, does not provide financial advice, and does not execute trades automatically. Users remain fully responsible for their own trading decisions, risk management, and market behavior.

The Trade Forensics Agent is designed to improve risk awareness and decision quality, not to promise outcomes or automate trading.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
