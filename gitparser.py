import pandas as pd
from git import Repo
import sys

for param in sys.argv:
    param = param.replace('\'', '').replace('"', '')
    if 'output' in param:
        filename = param[param.find('=') + 1:]
    if 'repo' in param:
        repo_path = param[param.find('=') + 1:]
    if 'branch' in param:
        branch = param[param.find('=') + 1:]
def createCSV(repo_path, filename, branch):
    if '\\' in repo_path:
        repo_path = repo_path.replace('\\', '/')
    if '.csv' not in filename:
        filename = str(filename) + '.csv'
    repo = Repo(repo_path)
    hash_list = []
    authors = []
    dates = []
    filenames = []
    commits = list(repo.iter_commits(branch))
    for i in range(len(commits)):
        for changed_file in commits[i].stats.files.keys():
            hash_list.append(commits[i])
            authors.append(commits[i].author)
            dates.append(commits[i].committed_datetime)
            filenames.append(changed_file)
    df = pd.DataFrame()
    df['Hash'] = hash_list
    df['Author'] = authors
    df['Date'] = dates
    df['Filename'] = filenames
    df.to_csv(filename, index=False)
createCSV(repo_path, filename, branch)