import numpy as np
from statsmodels.stats.power import tt_ind_solve_power

#define approximation to Cohen's distance
def cohens_h(p1, p2):
    return abs(2*(np.arcsin(np.power(p1,0.5)) - np.arcsin(np.power(p2,0.5))))



def determine_sample_size(features):
  control_rate = float(features['conversion_rate']) / 100
  test_rate = control_rate + control_rate * float(features['detectable_difference']) / 100
  num_variants = int(features['number_of_variants'])
  power = float(features['power'])
  alpha = float(features['alpha']) / (num_variants - 1)
  proportion_control = float(features['control_proportion'])
  ratio = ((100 - proportion_control) / (num_variants - 1)) / proportion_control
  effect_size = cohens_h(control_rate, test_rate)

  sample_size_control= int(tt_ind_solve_power(effect_size=effect_size, nobs1=None, alpha=alpha, power=power, ratio=ratio))

  try: 
    samples_per_day = float(features['samples_per_day'])
    days_to_run_estimate = round(sample_size_control / samples_per_day)
  except:
    samples_per_day = 'Unknown'
    days_to_run_estimate = 'Unknown'

  
  

  return sample_size_control, days_to_run_estimate



if __name__ == '__main__':
    print(determine_sample_size(example))
