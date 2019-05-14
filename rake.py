$ git clone https://github.com/zelandiya/RAKE-tutorial
import rake
import operator
stoppath = "data/stoplists/SmartStoplist.txt"
rake_object = rake.Rake("SmartStoplist.txt", 5, 3, 4)
sample_file = open("desktop/LendingHomeLien.txt", 'r')
text = sample_file.read()
keywords = rake_object.run(text)
print "Keywords:", keywords
