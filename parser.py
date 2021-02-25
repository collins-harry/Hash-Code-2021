def parse(filename):
    with open(filename) as f:
        out = dict()
        out['streets'] = dict()
        out['car_path'] = list()
        for idx, line in enumerate(f):
            if idx == 0:
                D, I, S, V, F = line.split(" ")
                out['D'] = int(D)
                out['I'] = int(I)
                out['S'] = int(S)
                out['V'] = int(V)
                out['F'] = int(F)
            elif idx <= out['S']:
                B, E, street_name, L = line.split(" ")
                out['streets'][street_name] = {'B': int(B), 'E': int(E), 'L': int(L)}
            else:
                thing = line.split(" ")
                out['car_path'].append({'P': thing[0], 'street_list': thing[1:]})
        return out
