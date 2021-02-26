import sys

N = int(sys.stdin.readline().strip())

S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
team = []
member = []
score = []
peo2_team_list = []
peo2_team = []
check = [False for _ in range(N)]


def dfs(depth):
    if depth == N // 2:
        team.append(tuple(member))
        return

    for i in range(N):
        if i > 0 and len(member) == 0:
            return
        if not check[i]:
            check[i] = True
            if len(member) == 0 or member[-1] < i:
                member.append(i)
                dfs(depth + 1)
                check[i] = False
                member.pop()
            else:
                check[i] = False

def dfs_team(depth, team_para):
    global peo2_team_list

    if depth == 2:  # # peo2_team_list = [((0, 1), (0, 2), (1, 2))...]
        peo2_team_list.append(tuple(peo2_team))
        return
    for i in range(N // 2):
        if not check_second[i]:
            check_second[i] = True
            if len(peo2_team) == 0 or peo2_team[-1] < team_para[i]:
                peo2_team.append(team_para[i])
                dfs_team(depth + 1, team_para)
                check_second[i] = False
                peo2_team.pop()
            else:
                check_second[i] = False

    if depth == 0:
        tmp = peo2_team_list
        peo2_team_list = []
        return tmp



def oppteam(team):
    opp_member = []
    # 상대편도 넣기.
    for member in team:
        tmp = []
        for i in range(N):
            if not i in member:
                tmp.append(i)
        opp_member.append(tuple(tmp))
    return opp_member


def cal_team_power(team, opp_team):

    for i in range(len(team)):
        team_score = 0
        opp_team_score = 0
        for j in dfs_team(0, team[i]):
            team_score += S[j[0]][j[1]] + S[j[1]][j[0]]
        for k in dfs_team(0, opp_team[i]):
            opp_team_score += S[k[0]][k[1]] + S[k[1]][k[0]]

        score.append(abs(team_score - opp_team_score))


    return min(score)


dfs(0)
check_second = [False for _ in range(N // 2)]
opp_team = oppteam(team)

print(cal_team_power(team, opp_team))
