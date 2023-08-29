#Let's create 3 functions, one for guards, one for forwards, and one for centers

from dataCollection import get_player_data



def find_value_in_range(input_num, range_value_map):
    for (lower, upper), value in range_value_map.items():
        if lower <= input_num <= upper:
            return value

def guard_score(data):
    games_played_ranges = {
    (0, 99): 0,
    (100, 199): 1.8,
    (200, 299): 2.6,
    (300, 399): 3.6,
    (400, 499): 4.8,
    (500, 599): 7,
    (600, 699): 9,
    (700, 799): 12,
    (800, 899): 15,
    (900, 999): 18,
    (1001, 1250): 20,
    (1251, float('inf')): 25,
    }
    points_ranges = {
    (0, 5): 1,
    (5, 7): 2,
    (7, 10): 2.5,
    (10,12): 3.5,
    (12, 15): 4.5,
    (15, 17): 6,
    (17, 19): 7,
    (19, 22): 8,
    (22, 25): 9.5,
    (25, float('inf')): 10,
    }
    assists_ranges = {
    (0, 3): 2,
    (3, 4): 3,
    (4, 5): 4.5,
    (5, 6): 6.5,
    (6, 7): 7.5,
    (7, 8): 9,
    (8, 9): 10,
    (9, 10): 11,
    (10, float('inf')): 12,
    }
    rebounds_ranges = {
    (0, 3): 2,
    (3, 5): 4,
    (5, float('inf')): 6,
    }
    steals_ranges = {
    (0, 0.5): 1,
    (0.5, 1): 3,
    (1, 1.2): 4,
    (1.2, 1.4): 5,
    (1.4, 1.6): 6,
    (1.6, 1.8): 7,
    (1.8, float('inf')): 8,
    }
    blocks_ranges = {
    (0, 0.2): 1,
    (0.2, 0.4): 2,
    (0.4, 0.6): 3,
    (0.6, float('inf')): 4,
    }
    ts_percentage_ranges = {
    (0, 50): 0,
    (50, 53): 2.1,
    (53, 56): 4.2,
    (56, 58): 6.3,
    (58, 59): 8,
    (59, float('inf')): 9.6,
    }
    offensive_rating_ranges = {
    (0, 100): 0,
    (100, 103): 2.1,
    (103, 106): 4.2,
    (106, 109): 6.3,
    (109, 112): 7.4,
    (112, float('inf')): 8.4,
    }
    defensive_rating_ranges = {
    (108, float('inf')): 1.5,
    (107, 108): 3,
    (106, 107): 4,
    (105, 106): 5,
    (-float('inf'), 105): 6.1,
    }
    ast_to_ratio_ranges = {
    (-float('inf'), 1.8): 2.1,
    (1.8, 2.5): 4.2,
    (2.5, 3): 6.3,
    (3, 3.5): 8.4,
    (3.5, float('inf')): 9.6,
    }
    plus_minus_ranges = {
    (-float('inf'), 1): 2.1,
    (1, 2): 4.2,
    (2, 3): 6.3,
    (3, 4): 7.4,
    (4, float('inf')): 8.4,
    }   
    games_score = find_value_in_range(data[0][2], games_played_ranges)
    points_score = find_value_in_range(data[0][6], points_ranges)
    assists_score = find_value_in_range(data[0][7], assists_ranges)
    rebounds_score = find_value_in_range(data[0][8], rebounds_ranges)
    steals_score = find_value_in_range(data[0][9], steals_ranges)
    blocks_score = find_value_in_range(data[0][10], blocks_ranges)
    ts_score = find_value_in_range(data[2][3], ts_percentage_ranges)
    off_rating_score = find_value_in_range(data[2][1], offensive_rating_ranges)
    def_rating_score = find_value_in_range(data[2][2], defensive_rating_ranges)
    ast_to_score = find_value_in_range(data[0][12], ast_to_ratio_ranges)
    plus_minus_score = find_value_in_range(data[2][0], plus_minus_ranges)
    total_score = games_score + points_score + assists_score + rebounds_score + steals_score + blocks_score + ts_score + off_rating_score + def_rating_score + ast_to_score + plus_minus_score
    for i in data[1]:
        if i == 'NBA Most Valuable Player':
            total_score+=5
        if i == 'NBA Finals Most Valuable Player':
            total_score+=5
        if i == 'All-Defensive Team':
            total_score+=1
        if i == 'All-NBA':
            total_score+=1
    total_score = total_score + 3 * data[1][len(data[1])-1]
    return total_score


def forward_score(data):
    games_played_ranges = {
    (0, 99): 0,
    (100, 199): 1.8,
    (200, 299): 2.6,
    (300, 399): 3.6,
    (400, 499): 4.8,
    (500, 599): 7,
    (600, 699): 9,
    (700, 799): 12,
    (800, 899): 15,
    (900, 999): 18,
    (1001, 1250): 20,
    (1251, float('inf')): 25,
    }
    points_ranges = {
    (0, 5): 1,
    (5, 7): 2,
    (7, 10): 3.5,
    (10,12): 4.5,
    (12, 15): 5.5,
    (15, 17): 7,
    (17, 19): 9,
    (19, 22): 11,
    (22, 25): 12.5,
    (25, float('inf')): 14,
    }
    rebounds_ranges = {
    (0, 3): 2,
    (3, 4): 3,
    (4, 5): 4.5,
    (5, 6): 6.5,
    (6, 7): 7.5,
    (7, 8): 9,
    (7, 8): 11,
    (8, float('inf')): 12,
    }
    assists_ranges = {
    (0, 3): 2,
    (3, 5): 4,
    (5, float('inf')): 6,
    }
    steals_ranges = {
    (0, 0.5): 1,
    (0.5, 0.8): 1.5,
    (0.8, 1): 2.5,
    (1.0, 1.4): 3.5,
    (1.4, 1.8): 5,
    (1.8, float('inf')): 6,
    }
    blocks_ranges = {
    (0, 0.2): 0,
    (0.2, 0.5): 2,
    (0.5, 1): 3,
    (1, 1.4): 4,
    (1.2, 1,4): 5,
    (1.4, float('inf')): 6,
    }
    ts_percentage_ranges = {
    (0, 50): 0,
    (50, 53): 2.1,
    (53, 56): 4.2,
    (56, 58): 6.3,
    (58, 59): 8,
    (59, float('inf')): 9.6,
    }
    offensive_rating_ranges = {
    (0, 100): 0,
    (100, 103): 2.1,
    (103, 106): 4.2,
    (106, 109): 6.3,
    (109, 112): 7.4,
    (112, float('inf')): 7.2,
    }
    defensive_rating_ranges = {
    (108, float('inf')): 1.5,
    (107, 108): 3,
    (106, 107): 4,
    (105, 106): 5,
    (-float('inf'), 105): 7.3,
    }
    ast_to_ratio_ranges = {
    (-float('inf'), 1.8): 0,
    (1.8, 2.5): 1,
    (2.5, 3): 1.5,
    (3, 3.5): 2.5,
    (3.5, float('inf')): 3.5,
    }
    plus_minus_ranges = {
    (-float('inf'), 1): 2.1,
    (1, 2): 4.2,
    (2, 3): 6.3,
    (3, 4): 7.4,
    (4, float('inf')): 8.4,
    }   
    games_score = find_value_in_range(data[0][2], games_played_ranges)
    points_score = find_value_in_range(data[0][6], points_ranges)
    assists_score = find_value_in_range(data[0][7], assists_ranges)
    rebounds_score = find_value_in_range(data[0][8], rebounds_ranges)
    steals_score = find_value_in_range(data[0][9], steals_ranges)
    blocks_score = find_value_in_range(data[0][10], blocks_ranges)
    ts_score = find_value_in_range(data[2][3], ts_percentage_ranges)
    off_rating_score = find_value_in_range(data[2][1], offensive_rating_ranges)
    def_rating_score = find_value_in_range(data[2][2], defensive_rating_ranges)
    ast_to_score = find_value_in_range(data[0][12], ast_to_ratio_ranges)
    plus_minus_score = find_value_in_range(data[2][0], plus_minus_ranges)
    total_score = games_score + points_score + assists_score + rebounds_score + steals_score + blocks_score + ts_score + off_rating_score + def_rating_score + ast_to_score + plus_minus_score
    for i in data[1]:
        if i == 'NBA Most Valuable Player':
            total_score+=5
        if i == 'NBA Finals Most Valuable Player':
            total_score+=5
        if i == 'All-Defensive Team':
            total_score+=1
        if i == 'All-NBA':
            total_score+=1
    total_score = total_score + 3 * data[1][len(data[1])-1]
    return total_score




def big_score(data):
    games_played_ranges = {
    (0, 99): 0,
    (100, 199): 1.8,
    (200, 299): 2.6,
    (300, 399): 3.6,
    (400, 499): 4.8,
    (500, 599): 7,
    (600, 699): 9,
    (700, 799): 12,
    (800, 899): 15,
    (900, 999): 18,
    (1001, 1250): 20,
    (1251, float('inf')): 25,
    }
    points_ranges = {
    (0, 5): 1,
    (5, 7): 2,
    (7, 10): 3.5,
    (10,12): 4.5,
    (12, 15): 5.5,
    (15, 17): 7,
    (17, 19): 9,
    (19, 22): 11,
    (22, 25): 12.5,
    (25, float('inf')): 12,
    }
    rebounds_ranges = {
    (0, 3): 0.5,
    (3, 5): 3,
    (5, 6): 5,
    (6, 7): 7,
    (7, 8): 9,
    (8, 9.5): 11.5,
    (9.5, 10.5): 13,
    (10.5, float('inf')): 14, 
    }
    assists_ranges = {
    (0, 3): 2,
    (3, 5): 4,
    (5, float('inf')): 6,
    }
    steals_ranges = {
    (0, 0.2): 0,
    (0.2, 0.7): 1,
    (0.7, 1): 3.5,
    (1, 1.3): 3.5,
    (1.3, float('inf')): 4,
    }
    blocks_ranges = {
    (0, 0.5): 0,
    (0.5, 1): 1.5,
    (1, 1.4): 3,
    (1.4, 1.8): 4.5,
    (1.8, 2.4): 6,
    (2.4, float('inf')): 8,
    }
    ts_percentage_ranges = {
    (0, 50): 0,
    (50, 53): 0.75,
    (53, 56): 2.5,
    (56, 58): 4.5,
    (58, 59): 6,
    (59, float('inf')): 7.3,
    }
    offensive_rating_ranges = {
    (0, 100): 0,
    (100, 103): 2.1,
    (103, 106): 4.2,
    (106, 109): 6.3,
    (109, 112): 7.4,
    (112, float('inf')): 7.2,
    }
    defensive_rating_ranges = {
    (108, float('inf')): 1,
    (107, 108): 3,
    (106, 107): 5,
    (105, 106): 7,
    (-float('inf'), 105): 9.6,
    }
    ast_to_ratio_ranges = {
    (-float('inf'), 1.8): 0,
    (1.8, 2.5): 1,
    (2.5, 3): 1.5,
    (3, 3.5): 2.5,
    (3.5, float('inf')): 3.5,
    }
    plus_minus_ranges = {
    (-float('inf'), 1): 2.1,
    (1, 2): 4.2,
    (2, 3): 6.3,
    (3, 4): 7.4,
    (4, float('inf')): 8.4,
    }   
    games_score = find_value_in_range(data[0][2], games_played_ranges)
    points_score = find_value_in_range(data[0][6], points_ranges)
    assists_score = find_value_in_range(data[0][7], assists_ranges)
    rebounds_score = find_value_in_range(data[0][8], rebounds_ranges)
    steals_score = find_value_in_range(data[0][9], steals_ranges)
    blocks_score = find_value_in_range(data[0][10], blocks_ranges)
    ts_score = find_value_in_range(data[2][3], ts_percentage_ranges)
    off_rating_score = find_value_in_range(data[2][1], offensive_rating_ranges)
    def_rating_score = find_value_in_range(data[2][2], defensive_rating_ranges)
    ast_to_score = find_value_in_range(data[0][12], ast_to_ratio_ranges)
    plus_minus_score = find_value_in_range(data[2][0], plus_minus_ranges)
    total_score = games_score + points_score + assists_score + rebounds_score + steals_score + blocks_score + ts_score + off_rating_score + def_rating_score + ast_to_score + plus_minus_score
    for i in data[1]:
        if i == 'NBA Most Valuable Player':
            total_score+=5
        if i == 'NBA Finals Most Valuable Player':
            total_score+=5
        if i == 'All-Defensive Team':
            total_score+=2
        if i == 'All-NBA':
            total_score+=2
    total_score = total_score + 3 * data[1][-1]
    return total_score


def get_final_score(player_nme):
    score = 0
    score_data = get_player_data(player_nme)
    position = score_data[0][1]
    if 'f' in position:
        score = forward_score(score_data)
    elif 'g' in position:
        score = guard_score(score_data)
    else:
        score = big_score(score_data)
    return score




