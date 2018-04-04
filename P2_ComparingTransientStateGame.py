import Parameters as P
import Problem2 as Cls
import SupportTransientState as Support

# create multiple cohorts for when the drug is not available
multiCohortFairCoin = Cls.MultiCohort(
    ids=range(P.NUM_SIM_COHORTS),   # [0, 1, 2 ..., NUM_SIM_COHORTS-1]
    pop_sizes=[P.REAL_POP_SIZE] * P.NUM_SIM_COHORTS,  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
    coin_probs=[P.FAIR_PROB]*P.NUM_SIM_COHORTS  # [p, p, ...]
)
# simulate all cohorts
multiCohortFairCoin.simulate(P.TIME_STEPS)

# create multiple cohorts for when the drug is available
multiCohortUnfairCoin = Cls.MultiCohort(
    ids=range(P.NUM_SIM_COHORTS, 2*P.NUM_SIM_COHORTS),   # [NUM_SIM_COHORTS, NUM_SIM_COHORTS+1, NUM_SIM_COHORTS+2, ...]
    pop_sizes=[P.REAL_POP_SIZE] * P.NUM_SIM_COHORTS,  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
    mortality_probs=[P.FAIR_PROB*P.UNFAIR_PROB]*P.NUM_SIM_COHORTS
)
# simulate all cohorts
multiCohortUnfairCoin.simulate(P.TIME_STEPS)

# print outcomes of each cohort
Support.print_outcomes(multiCohortFairCoin, 'When coin is fair:')
Support.print_outcomes(multiCohortUnfairCoin, 'When coin is unfair:')

# draw histograms of average survival time
Support.draw_histograms(multiCohortFairCoin, multiCohortUnfairCoin)

# print comparative outcomes
Support.print_comparative_outcomes(multiCohortFairCoin, multiCohortUnfairCoin)
