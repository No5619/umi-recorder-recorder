- 取自 https://github.com/jim60105/twitch-stream-recorder/tree/987dfdad69436b819bf0ea919285b7b325bb0a29

- 去 https://dev.twitch.tv/console/apps 跟twitch申請client_id、client_secret

- 請先新建config檔，程式才能順利執行:

```python
# path to a folder where you want your VODs to be saved to
root_path = r"recorder/umi_videos"
# name of the streamer you want to record by default
username = "umimiowo"

# register clieint_id, client_secret from twitch-developers:
# link: https://dev.twitch.tv/console/apps
client_id = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
client_secret = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"

quality = "best"
```

- 執行` pip install -r ./requirements.txt`，安裝所需的package

- 執行twitch-recorder.py，就會開始進行監控、錄製