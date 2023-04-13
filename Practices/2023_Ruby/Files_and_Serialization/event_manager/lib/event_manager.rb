require 'google/apis/civicinfo_v2'
require "csv"
require "erb"

civic_info = Google::Apis::CivicinfoV2::CivicInfoService.new
civic_info.key = 'AIzaSyClRzDqDh5MsXwnCWi0kOiiBivP6JsSyBw'
file_name = "event_attendees_s.csv"

puts("EventManager Initialized!")

=begin # Iteration 0: Loading a File
file = File.exist?("event_attendees_s.csv") ? File.open("event_attendees_s.csv", "r") : nil
file.readline
until file.eof?
	line = file.readline
	line = line.split(",")
	name = line[2]
	puts name
end
=end

table = File.exist?(file_name) ? CSV.open(file_name,
										headers: true,
										header_converters: :symbol
									) : nil
template_letter = File.read('form_letter.html')
erb_template = ERB.new template_letter
Dir.mkdir('output') unless Dir.exist?('output')
hour_counter = Hash.new(0)

table.each { |row|
	id = row[0]
	person_name = row[:first_name]
	zip_code = row[:zipcode].to_s.rjust(5, '0')[0..4]
	legislators = civic_info.representative_info_by_address(
		address: 80202,
		levels: 'country',
		roles: ['legislatorUpperBody', 'legislatorLowerBody']
		).officials

	form_letter = erb_template.result(binding)
  	#puts form_letter

  	form_filename = "output/thanks_#{id}.html"
  	File.open(form_filename, "w"){ |file|
  		file.puts(form_letter)
  	}
  	puts "[+] #{id} done"

  	wrangled_date = []
  	wrangled_time = []
  	reg_date = row[:regdate].split(" ")
  	reg_date[0].split("/").each{ |date|
  		wrangled_date.push(date.rjust(2, '0'))
  	}
  	reg_date[1].split(":").each{ |time|
  		wrangled_time.push(time.rjust(2, '0'))
  	}
  	reg_hour = DateTime.strptime("#{wrangled_date.join("/")} #{wrangled_time.join(":")}", "%m/%d/%y %H:%M").hour
  	hour_counter[reg_hour] += 1
}

puts "Registration Dates:"
puts hour_counter