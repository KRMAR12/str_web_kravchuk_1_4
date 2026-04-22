from locust import HttpUser, task, between

class CryptoPerformanceUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def search_scenario(self):
        
        self.client.get("/")
        
        self.client.get("/search?q=Ukraine", name="/search")

    @task
    def view_map(self):
        
        self.client.get("/map")