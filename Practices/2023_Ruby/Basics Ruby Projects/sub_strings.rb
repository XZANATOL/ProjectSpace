dictionary = ["below","down","go","going","horn","how","howdy","it","i","low","own","part","partner","sit"]
def sub_strings(string, dictionary)
	counter = Hash.new(0)
	string.downcase!

	dictionary.each { |word|
		matches = string.scan(word).length
		counter[word] = matches unless matches == 0
	}

	return counter
end

print("> ")
string = gets.strip
puts sub_strings(string, dictionary)