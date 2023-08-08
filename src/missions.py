```python
class Mission:
    def __init__(self, mission_id, mission_name, mission_description, mission_objectives):
        self.mission_id = mission_id
        self.mission_name = mission_name
        self.mission_description = mission_description
        self.mission_objectives = mission_objectives
        self.mission_status = "Not Started"

    def start_mission(self):
        self.mission_status = "In Progress"

    def complete_mission(self):
        self.mission_status = "Completed"

    def get_mission_status(self):
        return self.mission_status

    def get_mission_details(self):
        return {
            "mission_id": self.mission_id,
            "mission_name": self.mission_name,
            "mission_description": self.mission_description,
            "mission_objectives": self.mission_objectives,
            "mission_status": self.mission_status
        }


class Missions:
    def __init__(self):
        self.missions = []

    def add_mission(self, mission):
        self.missions.append(mission)

    def get_mission(self, mission_id):
        for mission in self.missions:
            if mission.mission_id == mission_id:
                return mission
        return None

    def start_mission(self, mission_id):
        mission = self.get_mission(mission_id)
        if mission:
            mission.start_mission()

    def complete_mission(self, mission_id):
        mission = self.get_mission(mission_id)
        if mission:
            mission.complete_mission()

    def get_all_missions(self):
        return [mission.get_mission_details() for mission in self.missions]
```