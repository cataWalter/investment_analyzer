interest_rate = 10  # value in %
set_aside_per_month = 1000
set_aside_per_year = 12 * set_aside_per_month
years = 10
final_capital = 0
gain = 0

for i in range(years):
    print("year =", i)
    print("gain =", int(gain))
    print("capital =", int(final_capital))
    print()
    gain = final_capital * interest_rate / 100
    final_capital = final_capital + gain + set_aside_per_year
