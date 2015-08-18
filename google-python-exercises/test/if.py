import random

def main():
    speeds = [50,60,70,80,90,100]
    moods = ['good','bad','terrible']
    speed = speeds[random.randint(0,len(speeds)-1)]
    mood = moods[random.randint(0,len(moods)-1)]

    print "Speed: " + str(speed)
    print "Officers mood: " + mood
    
    if speed >=80:
        print "License and registration please"
        if mood == 'terrible' or speed >= 100:
            print 'STEP OUT OF THE VEHICAL'
        elif mood == 'bad' or speed >= 90:
            print "I'm going to have to write you a ticket"
        else:
            print "Slow it down bub"
    else:
        print "Have a good day"
    
def write_ticket():
    print "Sorry, I'm going to have to write you a ticket"

if __name__ == "__main__":
    main()
