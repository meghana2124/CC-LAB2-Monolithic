# from locust import HttpUser, task, between

# class MyEventsUser(HttpUser):
#     wait_time = between(1, 2)

#     @task
#     def view_my_events(self):
#         self.client.get("/my-events?user=locust_user")


# optimised:-
from locust import HttpUser, task, between
import random

class MyEventsUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def view_my_events(self):
        # Randomize the user parameter to simulate different users
        user = f"locust_user_{random.randint(1, 1000)}"
        self.client.get(f"/my-events?user={user}")
