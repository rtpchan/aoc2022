import pulp

# ore robot ore cost
# clay robot ore cost
# obsidian robot ore cost
# obsidian robot clay cost
# geode robot ore cost
# geode robot obsidian cost
# time available
def problem(o, c, oo, oc, go, gc, time):

    gem_prob = pulp.LpProblem('gem_stone_problem', pulp.LpMaximize)

    time_series = list(range(time))
    time_series_to_calculate = list(range(time - 1))

    ore = pulp.LpVariable.dicts("ore", time_series, lowBound=0, cat=pulp.LpInteger)
    clay = pulp.LpVariable.dicts("clay", time_series, lowBound=0, cat=pulp.LpInteger)
    obsidian = pulp.LpVariable.dicts("obsidian", time_series, lowBound=0, cat=pulp.LpInteger)
    geode = pulp.LpVariable.dicts("geode", time_series, lowBound=0, cat=pulp.LpInteger)

    ore_robots = pulp.LpVariable.dicts("ore_robots", time_series, lowBound=0, cat=pulp.LpInteger)
    clay_robots = pulp.LpVariable.dicts("clay_robots", time_series, lowBound=0, cat=pulp.LpInteger)
    obsidian_robots = pulp.LpVariable.dicts("obsidian_robots", time_series, lowBound=0, cat=pulp.LpInteger)
    geode_robots = pulp.LpVariable.dicts("geode_robots", time_series, lowBound=0, cat=pulp.LpInteger)

    ore[0] = 0
    clay[0] = 0
    obsidian[0] = 0
    geode[0] = 0

    ore_robots[0] = 1
    clay_robots[0] = 0
    obsidian_robots[0] = 0
    geode_robots[0] = 0

    # maximize extracted geodes
    gem_prob += pulp.lpSum(geode)

    for x in time_series_to_calculate:
        # calculate how the resources will change
        gem_prob += ore[x + 1] == ore[x] + ore_robots[x] \
                    - (ore_robots[x + 1] - ore_robots[x]) * o \
                    - (clay_robots[x + 1] - clay_robots[x]) * c \
                    - (obsidian_robots[x + 1] - obsidian_robots[x]) * oo \
                    - (geode_robots[x + 1] - geode_robots[x]) * go 
        gem_prob += clay[x + 1] == clay[x] + clay_robots[x] \
                    - (obsidian_robots[x + 1] - obsidian_robots[x]) * oc 
        gem_prob += obsidian[x + 1] == obsidian[x] + obsidian_robots[x] \
                    - (geode_robots[x + 1] - geode_robots[x]) * gc
        gem_prob += geode[x + 1] == geode[x] + geode_robots[x]

        # constraint for having required resources amount to construct new robot
        gem_prob += ore[x] >= (ore_robots[x + 1] - ore_robots[x]) * o \
                    + (clay_robots[x + 1] - clay_robots[x]) * c \
                    + (obsidian_robots[x + 1] - obsidian_robots[x]) * oo \
                    + (geode_robots[x + 1] - geode_robots[x]) * go
        gem_prob += clay[x] >= (obsidian_robots[x + 1] - obsidian_robots[x]) * oc 
        gem_prob += obsidian[x] >= (geode_robots[x + 1] - geode_robots[x]) * gc

        # only one robot can be built
        gem_prob += ore_robots[x + 1] + obsidian_robots[x + 1] + clay_robots[x + 1] + geode_robots[x + 1] <=\
                    ore_robots[x] + obsidian_robots[x] + clay_robots[x] + geode_robots[x] + 1
        gem_prob += ore_robots[x + 1] >= ore_robots[x]
        gem_prob += clay_robots[x + 1] >= clay_robots[x]
        gem_prob += obsidian_robots[x + 1] >= obsidian_robots[x]
        gem_prob += geode_robots[x + 1] >= geode_robots[x]

    gem_prob.solve()

    return geode[time - 1].value()

    pass
