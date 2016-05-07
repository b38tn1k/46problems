# "99 Bottles of Beer" is a traditional song in
# the United States and Canada. It is popular to
# sing on long trips, as it has a very repetitive
# format which is easy to memorize, and can take a
# long time to sing. The song's simple lyrics are
# as follows:
#
# 99 bottles of beer on the wall, 99 bottles of
# beer.
# Take one down, pass it around, 98 bottles of
# beer on the wall.
#
# The same verse is repeated, each time with one
# fewer bottle. The song is completed when the
# singer or singers reach zero.
#
# Your task here is write a Python program capable
# of generating all the verses of the song.


def bottles(i):
    lyrics = "{} bottles of beer on the wall, {} bottles of beer.\n".format(i, i)
    while i > 0:
        i -= 1
        lyrics += "Take one down, pass it around, {} bottles of beer on the wall.\n".format(i)
        if i == 0: break
        lyrics += "{} bottles of beer on the wall, {} bottles of beer.\n".format(i, i)
    return lyrics

print (bottles(10))