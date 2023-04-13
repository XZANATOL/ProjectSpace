class String
    def is_upper?
        return self == self.upcase
    end

    def is_lower?
        return self == self.downcase
    end
end


def casear_cipher(string, shift)
    array_lower = Array('a'.ord..'z'.ord)
    array_upper = Array('A'.ord..'Z'.ord)
    cypher = ""

    string.each_char { |char|
        ord = char.ord
        if (char.is_upper?) and (char.is_lower?) # Checks if special char
            cypher += char
        elsif char.is_upper?
            ind = (array_upper.index(ord) + shift) % array_upper.length
            cypher += array_upper[ind].chr
        else
            ind = (array_lower.index(ord) + shift) % array_lower.length
            cypher += array_lower[ind].chr
        end
    }

    return cypher
end


print("Enter string to encode > ")
string = gets.chomp
unless string.ascii_only?
    raise ValueError
end

print("Enter shift number > ")
shift = gets.chomp.to_i
if shift == 0
    raise ValueError
end

puts(casear_cipher(string, shift))