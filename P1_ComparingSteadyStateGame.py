import Parameters as P
import Problem1 as Cls
import SupportSteadyState as Support

# create a cohort of patients for when the drug is not available
cohortFairCoin = Cls.Cohort(
    id=1,
    pop_size=P.SIM_POP_SIZE,
    mortality_prob=P.MORTALITY_PROB)
# simulate the cohort
FairCoinOutcome = cohortFairCoin.simulate(P.TIME_STEPS)

# create a cohort of patients for when the drug is available
cohortUnfairCoin = Cls.Cohort(
    id=2,
    pop_size=P.SIM_POP_SIZE,
    mortality_prob=P.MORTALITY_PROB*P.DRUG_EFFECT_RATIO)
# simulate the cohort
UnfairCoinOutcome = cohortUnfairCoin.simulate(P.TIME_STEPS)

# print outcomes of each cohort
Support.print_outcomes(FairCoinOutcome, 'When coin is fair:')
Support.print_outcomes(UnfairCoinOutcome, 'When coin is unfair:')

# draw survival curves and histograms
Support.draw_survival_curves_and_histograms(FairCoinOutcome, UnfairCoinOutcome)

# print comparative outcomes
Support.print_comparative_outcomes(FairCoinOutcome, UnfairCoinOutcome)
