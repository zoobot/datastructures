
def  electionWinner(votes):
  max = ''

  for i in votes:
    if votes.count(i) > votes.count(max):
      print('inif', votes.count(i))
      max = i
    elif votes.count(i) == votes.count(max):
      myascii = ord(i)
      print('inelse',myascii)
      if myascii > ord(max):
        max = myascii
    return max


votes = {'alex', "Micael"}