# 🔬 Trade Forensics Agent

An AI-powered crypto trade investigation skill designed to work with Binance market data and Agent OS.

Instead of generating another generic BUY/SELL signal, Trade Forensics investigates a trade **before or after execution** and identifies where the real risk is hiding.

## 🎯 What It Does

### Pre-Trade Forensics

Give the agent a proposed trade such as:

```text
Analyze my planned SOLUSDT long.
Entry: 140
Position: $200
Leverage: 10x
Stop Loss: 136
Take Profit: 150
```

The agent evaluates available data including:

- Market price
- Position size
- Leverage
- Stop-loss distance
- Risk/reward
- Bid/ask spread
- Liquidity
- Volatility
- Funding rate
- Open interest
- Liquidation exposure

It then produces a **Trade Integrity Score from 0–100** and identifies the biggest weakness in the setup.

### Post-Trade Forensics

Ask:

```text
Why did this trade lose?
```

The agent investigates possible causes such as:

- Bad entry
- Excessive leverage
- Oversized position
- Poor risk/reward
- Stop-loss placement
- Volatility
- Thin liquidity
- Spread/slippage
- Funding pressure
- Market timing
- Execution error

## 🧪 Example Output

```text
Trade Integrity Score: 38/100
Risk Level: Critical Risk

Key Findings
- Leverage is aggressive relative to the stop distance.
- Current volatility increases liquidation exposure.
- Risk/reward does not adequately compensate for setup risk.

Primary Failure Risk
Excessive leverage.

Risk Improvement
Reduce leverage and position exposure before execution.
```

## 🧠 Design Principle

Most trading assistants answer:

> Should I buy or sell?

Trade Forensics asks:

> What exactly can break this trade?

The goal is not hype or prediction. The goal is **trade diagnosis and risk intelligence**.

## 🛡️ Data Integrity

The skill must:

- Use live Binance data when available through connected tools.
- Never fabricate market prices or metrics.
- Clearly distinguish facts from estimates.
- Mark unavailable metrics instead of inventing values.
- Never claim certainty about future price movement.

## 📁 Repository Structure

```text
trade-forensics-agent/
├── skill/
│   └── SKILL.md
├── docs/
├── examples/
├── LICENSE
└── README.md
```

## 🚧 Status

Under active development.

Planned next steps include Binance market-data integration, forensic scoring logic, test cases, and richer post-trade diagnostics.

## 📜 License

MIT License