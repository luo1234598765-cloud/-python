import statistics


def calculate_return(start_price, end_price):
    return (end_price - start_price) / start_price


def calculate_max_drawdown(prices):
    peak = prices[0]
    max_drawdown = 0

    for price in prices:
        if price > peak:
            peak = price

        drawdown = (price - peak) / peak

        if drawdown < max_drawdown:
            max_drawdown = drawdown

    return max_drawdown


prices = [200, 202, 198, 205]

start_price = prices[0]
end_price = prices[-1]

print(f"开始价格：{start_price}")
print(f"结束价格：{end_price}")

total_return = calculate_return(start_price, end_price)
print(f"总收益率：{total_return:.2%}")

daily_returns = []

for i in range(len(prices) - 1):
    daily_return = calculate_return(prices[i], prices[i + 1])
    daily_returns.append(daily_return)
    print(f"第{i + 1}天到第{i + 2}天的收益率：{daily_return:.2%}")

print(f"每日收益率列表：{daily_returns}")

average_return = sum(daily_returns) / len(daily_returns)
best_return = max(daily_returns)
worst_return = min(daily_returns)

print(f"平均每日收益率：{average_return:.2%}")
print(f"最大单日涨幅：{best_return:.2%}")
print(f"最大单日跌幅：{worst_return:.2%}")

daily_volatility = statistics.stdev(daily_returns)
annual_volatility = daily_volatility * (252 ** 0.5)

print(f"每日波动率：{daily_volatility:.2%}")
print(f"年化波动率：{annual_volatility:.2%}")

max_drawdown = calculate_max_drawdown(prices)
print(f"最大回撤：{max_drawdown:.2%}")

daily_risk_free_rate = 0
sharpe_ratio = (
    (average_return - daily_risk_free_rate)
    / daily_volatility
    * (252 ** 0.5)
)

print(f"夏普比率：{sharpe_ratio:.2f}")
