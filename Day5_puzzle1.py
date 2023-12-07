import re
with open('input.txt') as fr:
   seeds = fr.readline()
   seeds = [int(i) for i in seeds.split(': ')[-1].split()]
   soils = [0 for _ in range(len(seeds))]
   ferts = [0 for _ in range(len(seeds))]
   waters = [0 for _ in range(len(seeds))]
   lights = [0 for _ in range(len(seeds))]
   temps = [0 for _ in range(len(seeds))]
   humids = [0 for _ in range(len(seeds))]
   locs = [0 for _ in range(len(seeds))]
   for l in fr:
    if 'map' in l:
        map_key = l.split()[0]
    if re.match('\d+\s+\d+\s+\d+',l):
        des,src,n = (int(c) for c in l.split())
        # for i in range(n): mapping[map_key][s + i] = d + i
        if map_key == 'seed-to-soil':
            for i,seed in enumerate(seeds):
                if soils[i] != 0 and soils[i] != seed: continue
                if seed >= src and seed <= src + n: soils[i]= seed + des - src
                else: soils[i] = seed
        if map_key == 'soil-to-fertilizer':
            for i,soil in enumerate(soils):
                if ferts[i] != 0 and ferts[i] != soil: continue
                if soil >= src and soil <= src + n: ferts[i]= soil + des - src
                else: ferts[i] = soil
        if map_key == 'fertilizer-to-water':
            for i,fert in enumerate(ferts):
                if waters[i] != 0 and waters[i] != fert: continue
                if fert >= src and fert <= src + n: waters[i]= fert + des - src
                else: waters[i] = fert
        if map_key == 'water-to-light':
            for i,water in enumerate(waters):
                if lights[i] != 0 and lights[i] != water: continue
                if water >= src and water <= src + n: lights[i]= water + des - src
                else: lights[i] = water
        if map_key == 'light-to-temperature':
            for i,light in enumerate(lights):
                if temps[i] != 0 and temps[i] != light: continue
                if light >= src and light <= src + n: temps[i]= light + des - src
                else: temps[i] = light
        if map_key == 'temperature-to-humidity':
            for i,temp in enumerate(temps):
                if humids[i] != 0 and humids[i] != temp: continue
                if temp >= src and temp <= src + n: humids[i]= temp + des - src
                else: humids[i] = temp
        if map_key == 'humidity-to-location':
            for i,humid in enumerate(humids):
                if locs[i] != 0 and locs[i] != humid: continue
                if humid >= src and humid <= src + n: locs[i]= humid + des - src
                else: locs[i] = humid



# for i in range(len(seeds)):
#     print(f'{seeds[i]} -> {soils[i]} -> {ferts[i]} -> {waters[i]} -> {lights[i]} -> {temps[i]} -> {humids[i]} -> {locs[i]}')

print(min(locs))