stocks = [17,3,6,9,15,8,6,1,10]
def stock_picker(prices)
	best_bid = Array.new(3) {0}
	prices.each_with_index.to_a.combination(2) { |buy, sell|
		if sell[0]-buy[0] > best_bid[2]
			best_bid = [buy[1], sell[1], sell[0] - buy[0]]
		end 
	}
	return best_bid
end

print(stock_picker(stocks)) # [buy_day, sell_day, profit]