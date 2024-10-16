import requests
import plotly.graph_objs as go
from plotly import offline

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
response = requests.get(url)
submission_ids = response.json()[:30]

submission_titles, submission_links, submission_comments = [], [], []

for submission_id in submission_ids:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    response = requests.get(url)
    if response.status_code == 200:
        submission_data = response.json()
        title = submission_data.get('title', 'N/A')
        comments = submission_data.get('descendants', 0)
        link = f"https://news.ycombinator.com/item?id={submission_id}"
        
        submission_titles.append(f"<a href='{link}'>{title}</a>")
        submission_comments.append(comments)

# Create bar chart
data = [go.Bar(x=submission_titles, y=submission_comments)]
layout = go.Layout(
    title="Most Active Discussions on Hacker News",
    xaxis_title="Submissions",
    yaxis_title="Number of Comments",
)
fig = go.Figure(data=data, layout=layout)
offline.plot(fig, filename='hn_discussions.html')
fig.write_image('images/hn_discussions.png')
