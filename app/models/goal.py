from app import db

# "One" side
# one Goal has many Tasks
# tasks looks at the class Task and finds the value for attribute/column "goal"
# tasks attribute is pluralized bc a singular goal HAS MANY tasks
# db.relationship creates the join table
class Goal(db.Model):
    goal_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    tasks = db.relationship("Task", back_populates="goal")
    

    # powerful takeaway: you can call a function on a value in a dict!
    def to_dict(self):
        return {
            "id": self.goal_id,
            "title": self.title
        }
    

    @classmethod
    def from_dict(cls, goal_data):
        new_goal = Goal(
            title=goal_data["title"]
        )
        return new_goal