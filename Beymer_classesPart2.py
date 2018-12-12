"""
Hello and welcome to the series of code that resulted in the loss of
at least 0.2333333321% of my brain cells. Have fun making your playlist to make
up for the true tragedy of the creaton process. :(((( xoxo - Amber Beymer
"""



class Song:
    def __init__(self, title, artist, trackNumber, length):
        self.title = title
        self.artist = artist
        self.trackNumber = trackNumber
        self.length = length

    def track_info(self):
        print("Song name: " + self.title)
        print("Artist:" + self.artist)
        print("Track number: " + str(self.trackNumber))
        print("Song length: " + str(self.length))
        print("") #break

class playList:

    def __init__(self, name):
        self.name = name
        self.playlist = []    #playlist = roster (from example)


    def addSong(self,song):
        self.playlist.append(song)    #append is used to add song
        print(self.name + " currently has " +str(len(self.playlist)) + " songs")
        playLen = 0 #accumulator
        for i in range(len(self.playlist)):
            playLen += self.playlist[i].length
        print("The accumulative length of " + self.name + " is " +str(playLen))

    def addOwnSong(self, title, artist, trackNumber, length):
        ownSong = Song(title, artist, trackNumber, length)
        self.addSong(ownSong)

    def remove_songIndex(self, index):
        self.playlist.pop(index)  #The pop() method removes and returns the element at the given index (passed as an argument) from the list. (Google)
        print(self.name + " currently has " + str(len(self.playlist)) + " songs")
        playLen = 0 #works same as addSong function
        for i in range(len(self.playlist)):
            playLen += self.playlist[i].length
        print("The accumulative length of " + self.name + " is" +str(playLen))


    def remove_songTitle(self, name):
        for i in range(len(self.playlist)):      #if user enters song title existing in playlist, that song is removed
            if self.playlist[i].title == name:
                self.playlist.pop(i)
        print("")
        print(self.name + " now has " + str(len(self.playlist)) + " songs")
        playLen = 0
        for i in range(len(self.playlist)):
            playLen += self.playlist[i].length
        print("The accumulative length of " + self.name + " is now " + str(playLen))

"""
        s1 = Song("Darude Sandstorm", "Darude", 1, 3.52)
        s2 = Song("Never Gonna Give You Up", "Rick Astley", 2, 3.35)  #song selection
        s3 = Song("The X-Files", "The Illuminati", 3, 5.24)
        s4 = Song("Big Green Tractor", "Jason Aldean", 5, 3.47)
        s5 = Song("The Duck Song", "I don't know", 6, 2.12)
"""

pn = input("What would you like to name your playlist?: ")
print("") #unecessary line of code, but it adds extra break adding to the aesthetic appeal if you will
playlistName = playList(pn)
addS1 = input("Add 'Darude Sandstorm' to your playlist? ('Yes' or 'No'): ")
if (addS1 == "Yes" or "yes"):
    print("")
    s1 = Song("Darude Sandstorm", "Darude", 1, 3.52)
    playlistName.addSong(s1)
    print("")
elif (addS1 == "No" or "no"):
    print("Your taste in music is trash!!!!!!1111!!!!!!!")
    exit()
addS2 = input("Add 'Never Gonna Give You Up' to your playlist? ('Yes' or 'No'): ")
if (addS2 == "Yes" or "yes"):
    print("")
    s2 = Song("Never Gonna Give You Up", "Rick Astley", 2, 3.35)
    playlistName.addSong(s2)
    print("")
elif (addS2 == "No" or "no"):
    print("Your taste in music is trash!!!!!!1111!!!!!!!")
    exit()
addS3 = input("Add 'The X-Files' to your playlist? ('Yes' or 'No'): ")
if (addS3 == "Yes" or "yes"):
    print("")
    s3 = Song("The X-Files", "The Illuminati", 3, 5.24)
    playlistName.addSong(s3)
    print("")
elif (addS3 == "No" or "no"):
    print("Your taste in music is trash!!!!!!1111!!!!!!!")
    exit()
addS4 = input("Add 'Big Green Tractor' to your playlist? ('Yes' or 'No'): ")
if (addS4 == "Yes" or "yes"):
    print("")
    s4 = Song("Big Green Tractor", "Jason Aldean", 5, 3.47)
    playlistName.addSong(s4)
    print("")
elif (addS4 == "No" or "no"):
    print("Your taste in music is trash!!!!!!1111!!!!!!!")
    exit()
addS5 = input("Add 'The Duck Song' to your playlist? ('Yes' or 'No'): ")
if (addS5 == "Yes" or "yes"):
    print("")
    s5 = Song("The Duck Song", "I don't know", 6, 2.12)
    playlistName.addSong(s5)
    print("")
elif (addS5 == "No" or "no"):
    print("Your taste in music is trash!!!!!!1111!!!!!!!")
    exit()



addElse = input("Add custom song to playlist?: ")
print("")
while addElse == "Yes" or "yes":    #sets condition variable 
    title = input("Song title: ")
    artist = input("Song artist: ")
    trackNumber = int(input("Song track number: "))
    length = float(input("Song length: "))
    print("")
    playlistName.addOwnSong(title, artist, trackNumber, length)
    print("")

removeSong = input("Remove a song from your playlist?: ")
while removeSong == "Yes" or "yes":
    print("")
    title = input("Which song would you like to remove by title?: ")
    print("")
    playlistName.remove_songTitle(title)
    print("")
    removeSong = input("Remove another song from your playlist?: ")
    print("")

print(pn + " has the following songs: ")
print("")
for i in range(len(playlistName.playlist)):
    playlistName.playlist[i].track_info()
    
    


                      
    









