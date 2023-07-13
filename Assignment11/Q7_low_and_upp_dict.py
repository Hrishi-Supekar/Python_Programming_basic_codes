# 7. create lower and upper dictionary for ex. l=["ReD","GreEen","BLue"]
# upper_lower_dict={'red':'RED','blue':'BLUE'....} using Dictionary comprehension

l = ['ReD', 'BlUe', 'GrEeN', 'YeLlOw', 'PiNk', 'PuRpLe', 'CyAn']
up_low_dict = {x.lower(): x.upper() for x in l}
print(up_low_dict)

