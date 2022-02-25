from pushbullet import Pushbullet

accesToken = 'o.ZKJxDw19XXv0pYvYhR61H5blyPuDF8Tk'

pb = Pushbullet(accesToken)
push = pb.push_note('Rewards', 'data')
