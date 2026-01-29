# from locust import HttpUser, task, between

# class EventsUser(HttpUser):
#     wait_time = between(1, 2)

#     @task
#     def view_events(self):
#         self.client.get("/events?user=locust_user")


# optimised:-

from locust import HttpUser, task, between
import random

class EventsUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def view_events(self):
        # Randomize the user parameter for each simulated user
        user = f"locust_user_{random.randint(1, 1000)}"
        self.client.get(f"/events?user={user}")
