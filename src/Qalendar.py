from Week import Week
from dimod import DiscreteQuadraticModel


# TODO: Make functions like get_sampler, or sample_dqm i.e. standard dwave ocean functions that will be useful
class Qalendar:
    def __init__(self, time_step: int = 15) -> None:
        self.week = Week(time_step)
        self.dqm = DiscreteQuadraticModel()
        self.time_step = time_step
        self.activities = (
            []
        )  # NOTE: This probably will become a dictionary, prepare to adaapt code if needed

    def __repr__(self) -> str:
        return str(self.week)

    def __getitem__(self, key):
        return self.week[key]

    def add_time_constraint(self, activity: str, total_time: int) -> None:
        """
        Adds a user specified time constraint to the DQM for a given activity
        """
        assert activity in self.activities, "Activity not found in activities"
        terms = []
        activity_index = self.activities.index(activity) + 1

        for day_id in range(7):
            for time in self.week[day_id].get_available_timeslots():
                terms.append((f"{day_id}_{time}", activity_index, 1))

        self.dqm.add_linear_equality_constraint(
            terms=terms,
            lagrange_multiplier=5,
            constant=-total_time * int(60 // self.time_step),
        )

        return None

    def add_time_preference(self, activity: str, preference: str) -> None:
        """
        Adds a preference for morning/afternoon/evening for a given activity
        """
        assert activity in self.activities, "Activity not found in activities"
        activity_index = self.activities.index(activity) + 1
        time_ranges = {
            "Morning": range(0, 1200),
            "Afternoon": range(1200, 1800),
            "Evening": range(1800, 2400),
        }

        if preference not in time_ranges:
            raise ValueError("Invalid preference")

        for day_id in range(7):
            for time in self.week[day_id].get_available_timeslots():
                v_label = f"{day_id}_{time}"
                if time in time_ranges[preference]:
                    self.dqm.set_linear_case(v_label, activity_index, -1)

        return None

    def prepare_dqm(self):
        for day in range(7):
            for time in self[day].get_available_timeslots():
                self.dqm.add_variable(len(self.activities) + 1, label=f"{day}_{time}")
