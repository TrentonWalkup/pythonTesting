from locust import HttpLocust, TaskSet, task, between

class UserBehaviour(TaskSet):
    def on_start(self):
        self.login()

    def on_stop(self):
        self.logout()

    def login(self):
        self.client.post("http://the-internet.herokuapp.com/login", {"username":"tomsmith", "password":"SuperSecretPassword!"})

    def logout(self):
        self.client.post("http://the-internet.herokuapp.com/login", {"username":"tomsmith", "password":"SuperSecretPassword!"})

    @task(1)
    def index(self):
        self.client.get("http://the-internet.herokuapp.com/secure")


class WebsiteUser(HttpLocust):
    task_set = UserBehaviour
    wait_time = between(5, 9)
