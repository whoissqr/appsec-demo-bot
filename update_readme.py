# shichao 2020.07.24:12:17
from python_graphql_client import GraphqlClient
import feedparser
import httpx
import json
import pathlib
import re
import os
import datetime

root = pathlib.Path(__file__).parent.resolve()
client = GraphqlClient(endpoint="https://api.github.com/graphql")


TOKEN = os.environ.get("GH_TOKEN", "")


def replace_chunk(content, marker, chunk, inline=False):
    r = re.compile(
        r"<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->".format(marker, marker),
        re.DOTALL,
    )
    if not inline:
        chunk = "\n{}\n".format(chunk)
    chunk = "<!-- {} starts -->{}<!-- {} ends -->".format(marker, chunk, marker)
    return r.sub(chunk, content)

def formatGMTime(timestamp):
    GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
    dateStr = datetime.datetime.strptime(timestamp, GMT_FORMAT) + datetime.timedelta(hours=8)
    return dateStr.date()

def make_query(after_cursor=None):
    return """
query {
  viewer {
    repositories(first: 100, privacy: PUBLIC, after:AFTER) {
      pageInfo {
        hasNextPage
        endCursor
      }
      nodes {
        name
        description
        url
        releases(last:1) {
          totalCount
          nodes {
            name
            publishedAt
            url
          }
        }
      }
    }
  }
}
""".replace(
        "AFTER", '"{}"'.format(after_cursor) if after_cursor else "null"
    )


def fetch_releases(oauth_token):
    repos = []
    releases = []
    repo_names = set()
    has_next_page = True
    after_cursor = None

    while has_next_page:
        data = client.execute(
            query=make_query(after_cursor),
            headers={"Authorization": "Bearer {}".format(oauth_token)},
        )
        print()
        print(json.dumps(data, indent=4))
        print()
        for repo in data["data"]["viewer"]["repositories"]["nodes"]:
            if repo["releases"]["totalCount"] and repo["name"] not in repo_names:
                repos.append(repo)
                repo_names.add(repo["name"])
                releases.append(
                    {
                        "repo": repo["name"],
                        "repo_url": repo["url"],
                        "description": repo["description"],
                        "release": repo["releases"]["nodes"][0]["name"]
                        .replace(repo["name"], "")
                        .strip(),
                        "published_at": repo["releases"]["nodes"][0][
                            "publishedAt"
                        ].split("T")[0],
                        "url": repo["releases"]["nodes"][0]["url"],
                    }
                )
        has_next_page = data["data"]["viewer"]["repositories"]["pageInfo"][
            "hasNextPage"
        ]
        after_cursor = data["data"]["viewer"]["repositories"]["pageInfo"]["endCursor"]
    return releases

def fetch_code_time():
    return httpx.get(
        "https://gist.githubusercontent.com/whoissqr/45929d16ece946e3d25fb40c4878e112/raw/"
    )

def fetch_douban():
    entries = feedparser.parse("https://www.douban.com/feed/people/kkshichao/interests")["entries"]
    return [
        {
            "title": item["title"],
            "url": item["link"].split("#")[0],
            "published": formatGMTime(item["published"])
        }
        for item in entries
    ]


def fetch_blog_entries():
    entries = feedparser.parse("http://kkshichao.blogspot.com/feed.xml")["entries"]
    return [
        {
            "title": entry["title"],
            "url": entry["link"].split("#")[0],
            "published": entry["published"].split("T")[0],
        }
        for entry in entries
    ]


if __name__ == "__main__":
    
    # === Write out to releases.md file ===
    project_releases = root / "releases.md"
    releases = fetch_releases(TOKEN)
    releases.sort(key=lambda r: r["published_at"], reverse=True)
    md = "\n".join(
        [
            "* <a href='{url}' target='_blank'>{repo} {release}</a> - {published_at}".format(**release)
            for release in releases[:8]
        ]
    )

    
    project_releases_md = "\n".join(
        [
            (
                "* **[{repo}]({repo_url})**: [{release}]({url}) - {published_at}\n"
                "<br>{description}"
            ).format(**release)
            for release in releases
        ]
    )
    project_releases_content = project_releases.open().read()
    project_releases_content = replace_chunk(
        project_releases_content, "recent_releases", project_releases_md
    )
    project_releases_content = replace_chunk(
        project_releases_content, "release_count", str(len(releases)), inline=True
    )
    project_releases.open("w").write(project_releases_content)
    
    print("project_releases_content === " + project_releases_content)
  
    # === write out to file README.md ===
    readme = root / "README.md"
    readme_contents = readme.open().read()
    rewritten = replace_chunk(readme_contents, "recent_releases", md)
    
    # update wakatime stats from my gist
    code_time_text = "\n```text\n"+fetch_code_time().text+"\n```\n"
    rewritten = replace_chunk(rewritten, "code_time", code_time_text)

    # update from my douban blog: want to read, etc.
    doubans = fetch_douban()[:5]
    doubans_md = "\n".join(
        ["* <a href='{url}' target='_blank'>{title}</a> - {published}".format(**item) for item in doubans]
    )

    rewritten = replace_chunk(rewritten, "douban", doubans_md)
    print("doubans_md === " + doubans_md)

    # update from my blogspot:
    entries = fetch_blog_entries()[:5]
    entries_md = "\n".join(
        ["* <a href='{url}' target='_blank'>{title}</a> - {published}".format(**entry) for entry in entries]
    )
    rewritten = replace_chunk(rewritten, "blog", entries_md)
    print("entries_md === " + entries_md)

    readme.open("w").write(rewritten)
    print("rewritten === " + rewritten)
    
