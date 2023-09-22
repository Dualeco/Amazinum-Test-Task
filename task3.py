import numpy as np
prob = np.array([0.1, 0.2, 0.4, 0.8, 0.9])

# One coin out of 5 is selected randomly. Find a probability of each time Heads fall in row:

# 1st way of thinking:
# P(H / before 1st experiment) = 0.48 (avg of each probability)
# P(H / before 2nd experiment) - ?

# H - event of 1 Heads with any preselected coin
# HH - event of 2 Heads in a row with any preselected coin
# P(HH) = sum of P(H/Ci) * P(Ci)
# P(HH) also equals P(H / before 1st experiment) * P(H / before 2nd experiment),
# Hence P(H / 2nd experiment) = P(HH) / P(H / 1st experiment) = 1.66 / 2.4 = 0.69
# ^ apply for all experiments up to 8th.

# 2nd way of thinking:
# Bayes theorem: P(HH/H) = (P(H/HH) * P(HH)) / P(H),
# H - event of 1 Heads with any preselected coin
# HH - event of 2 Heads in a row with any preselected coin
# P(HH / H) - prob of HH under condition that H happened
# P(H / HH) - prob of H under condition that HH happened. Clearly, P(H / HH) = 1,
# so this term cancels out.
# Hence, P(HH/H) = (P(H/HH) * P(HH)) / P(H) = P(HH) / P(H) = 1.66 / 2.4 = 0.69
# ^ apply for all experiments up to 8th

# Summing up, the solution equals:
# (common probability of N heads in a row) / (common probability of N - 1 heads in a row)


def calculate_for_n_trials(coin_probs, n_trials=8):
    # Init = before 1st experiment
    common_prob_before_each_experiment = [np.mean(coin_probs)]
    # 1 heads in row
    heads_in_row_probs = coin_probs

    # 2 and more heads in row
    for i in range(n_trials):
        heads_in_row_probs = heads_in_row_probs * coin_probs
        # Common probability for next heads in a row
        heads_in_row_common_prob = np.mean(heads_in_row_probs)

        prob_before_this_experiment = round(heads_in_row_common_prob / common_prob_before_each_experiment[-1], 2)

        common_prob_before_each_experiment.append(prob_before_this_experiment)

    return common_prob_before_each_experiment[1:]

print(calculate_for_n_trials(prob, 8))
