#dag is how we define the pipeline
#tasks in pipeline
#pendulum is build on top of datetime for start and end times
from airflow.decorators import dag, task
import pendulum
import requests
import xmltodict

@dag(
    dag_id = 'podcast_summary',
    schedule_interval = '@daily',
    start_date = pendulum.datetime(2023,5,8),
    catchup = False
)
def podcast_summary():
    #method goes here
    pass

    @task()
    def get_episodes():
        data = requests.get("https://www.marketplace.org/feed/podcast/marketplace/")
        feed = xmltodict.parse(data.text)
        episodes = feed["rss"]["channel"]["item"]
        print("Found {len(episodes)} episodes")
        return episodes
    podcast_episodes = get_episodes()

summary = podcast_summary()
