
from locust import Locust, TaskSet, task

class IgeonoteTasks(TaskSet):
    def on_start(self):
       pass

    @task
    def aagtekerke(self):
	    self.client.get('/city/map/1144829/aagtekerke-zeeland-netherlands')

    @task
    def index(self):
        self.client.get("/")

    @task
    def about(self):
        self.client.get("/city/map/651585/aach-baden-wurttemberg-germany")

    @task
    def api(self):
        self.client.get("/api/geoip/country/66.249.66.20")

    @task
    def city(self):
        self.client.get("/city")

    @task
    def country(self):
        self.client.get("/country/china")

    @task
    def geoname1(self):
        self.client.get("/api/zipcode/us/90210")

    @task
    def geoname2(self):
        self.client.get("/api/zipcode/za/9974")

    @task
    def geoname3(self):
        self.client.get("/api/zipcode/za/9958")

    @task
    def geoname4(self):
        self.client.get("/api/zipcode/za/9966")


class IgeonoteUser(Locust):
    host = 'http://igeonote.com'
    task_set = IgeonoteTasks

class SiboxTasks(TaskSet):
    def on_start(self):
        pass
    @task
    def index(self):
        self.client.get('/')

class SiboxUser(Locust):
    host = 'http://sibox.isgoodness.com'
    task_set = SiboxTasks

class ShrtiTasks(TaskSet):

    @task
    def index(self):
        self.client.get('/create')

class ShrtiUser(Locust):
    host = 'http://shrti.isgoodness.com'
    task_set = ShrtiTasks


class ErrorJsTasks(TaskSet):

    @task
    def index(self):
        self.client.get('/list')

class ErrorJsUser(Locust):
    host = 'http://jserrorpixel.com'
    task_set = ErrorJsTasks

class WebperfTasks(TaskSet):

    @task
    def index(self):
        self.client.get('/report/timing/igeonote.com')

class WebperfUser(Locust):
    host = 'http://webperf.isgoodness.com'
    task_set = WebperfTasks


class CurrebasTasks(TaskSet):

    @task
    def index(self):
        self.client.get('/')

class CurrebasUser(Locust):
    host = 'http://currebas.isgoodness.com'
    task_set = CurrebasTasks
