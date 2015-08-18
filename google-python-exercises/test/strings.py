def main():
    raw = r'test\nraw\nstring'
    print "raw " + raw
    multi =  """this goes 
on lots of lines"""

    print multi

    print "LOWER".lower()
    print "upper".upper()
    print "   no white space".strip()
    print "a is alpha: "+str("a".isalpha())
    print "2 is digit: "+str("2".isdigit())
    print " is space: "+ str(" ".isspace())
    longString = "this string is used for testing things"
    print "\n" + longString
    print "does is start with this?"
    print str(longString.startswith("this"))
    print "does it wend with things?"
    print str(longString.endswith("things"))
    print "where is the word used in it"
    print str(longString.find("used"))
    print longString.replace("string","stringy bit")
    print longString    
    print "test"
    orderdList1 = "Nate,Alyson,Cole,Colin"
    orderdList2 = "Thompson,Durham,Gibbs,McCarthy"
    splitList1 = orderdList1.split(',')
    splitList2 = orderdList2.split(',')
    joinedNames = []
    for i in range(len(splitList1)):
        joinedNames.append(splitList1[i] + " " + splitList2[i])
    print ",".join(joinedNames)
    test = "hello"
    newTest = test
    print test
    print newTest
    test = "by"
    print test
    print newTest
    print newTest[3:-1]

    print "%d is the number of times that I said %s %x" % (1,"test",8)
    print u"unicode! \u018e"
if __name__ == '__main__':
    main()
