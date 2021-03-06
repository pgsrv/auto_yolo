import numpy as np
from dps.utils import Config

from auto_yolo import envs

readme = "xo simple 2stage experiment"

config = Config()
distributions = dict(n_train=100 * 2 ** np.arange(8))

durations = dict(
    long=dict(
        max_hosts=1, ppn=6, cpp=2, gpu_set="0,1", wall_time="24hours",
        project="rpp-bengioy", cleanup_time="10mins",
        slack_time="10mins", n_repeats=6, step_time_limit="24hours"),
    med=dict(
        max_hosts=1, ppn=1, cpp=2, gpu_set="0", wall_time="2hours",
        project="rpp-bengioy", cleanup_time="2mins",
        slack_time="2mins", n_repeats=1),
    short=dict(
        max_hosts=1, ppn=3, cpp=2, gpu_set="0", wall_time="30mins",
        project="rpp-bengioy", cleanup_time="1min",
        slack_time="1min", n_repeats=3)
)

envs.run_experiment(
    "simple_xo_2stage", config, readme, alg="simple_xo_2stage", task="xo",
    name_variables="decoder_kind", durations=durations, distributions=distributions
)
