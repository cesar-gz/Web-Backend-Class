import redis

r = redis.Redis(db=0)

topFivePlayers = r.zrevrange("players", 0, 4, withscores=True)

format = {
        0 : "1st Place" ,
        1 : "2nd Place" ,
        2 : "3rd Place" ,
        3 : "4th Place" ,
        4 : "5th Place"    }

for i, (player, score) in enumerate(topFivePlayers):
    print(f"{format.get(i)}: {player.decode('utf-8')} with {int(score)} points")
