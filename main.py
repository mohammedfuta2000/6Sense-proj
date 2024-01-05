redisClient = redis.StrictRedis.from_url(redis_endpoint)
        try:
            redisClient.set('foo', 'bar')
            value = redisClient.get('foo')
            print("test Value: ", value)
        except Exception as e:
            print("\n\nredis error: ", e)
            print("\n\n\n")
            if "MOVED" in e:
                 new_endpoint = e.split()[2]
                 redisClient = redis.StrictRedis.from_url('redis://{}'.format(new_endpoint))

        key = "connected_chargepoints"
        keyExist = redisClient.exists(key)

sentence = "the dog blue"
print(sentence.split()[2])