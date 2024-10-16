import requests
import plotly.graph_objs as go
from plotly import offline

languages = ["javascript", "ruby", "c", "java", "perl", "haskell", "go"]
for language in languages:
    url = f"https://api.github.com/search/repositories?q=language:{language}&sort=stars"
    headers = {'Accept': 'application/vnd.github.v3+json'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        response_dict = response.json()
        repo_dicts = response_dict['items']
        names, stars = [], []
        
        for repo_dict in repo_dicts[:10]:  # Top 10 repositories
            names.append(repo_dict['name'])
            stars.append(repo_dict['stargazers_count'])
        
        # Create Bar Chart
        data = [go.Bar(x=names, y=stars)]
        layout = go.Layout(
            title=f"Most Popular {language.capitalize()} Projects on GitHub",
            xaxis_title="Repository",
            yaxis_title="Stars",
        )
        fig = go.Figure(data=data, layout=layout)
        offline.plot(fig, filename=f'{language}_repos.html')
        fig.write_image(f'images/{language}_repos.png')
    else:
        print(f"Failed to retrieve {language} repositories.")
