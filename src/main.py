

job_log="./data/longhorn-v100.log"
slurm_config="./test/test_data/slurm_config.json"
backfill_config="./test/test_data/backfill_config.json"

import sys
# print(sys.path)
import json

# from sim.simparser import *

def load_slurm_config(config_file):
    with open(config_file) as f:
        return json.load(f)


def load_backfill_config(config_file):
    with open(config_file) as f:
        return json.load(f)

slurm_config = load_slurm_config(slurm_config)
backfill_config = load_backfill_config(backfill_config)


simulator_tmp = simulator.Simulator()
# load_jobs is optional and it depends on whether you want to use the job from the initial logs
simulator_tmp.load_jobs(job_log)
# Time should be datetime.datetime
start_time = datetime.strptime("2020-06-26T08:40:53", "%Y-%m-%dT%H:%M:%S")
# Every new simulator instance must initialize the scheduler
simulator_tmp.init_scheduler(88, slurm_config, start_time, backfill_config)


