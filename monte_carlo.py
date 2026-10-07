import statistics
from scenarios.runner import run_scenario

errors = []
heater_duties = []

for seed in range(100):
    log = run_scenario(
        "scenarios/cold_morning.yaml",
        seed=seed,
        save_outputs=False,
    )

    setpoint = log["setpoint"][0]
    errors.append(
        statistics.mean(abs(t - setpoint) for t in log["T_true"])
    )
    heater_duties.append(statistics.mean(log["heater"]))

print("Average temperature error:", statistics.mean(errors))
print("Error standard deviation:", statistics.stdev(errors))
print("Average heater duty:", statistics.mean(heater_duties))