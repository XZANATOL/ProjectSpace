### Vimeo to YT Uploader

script that scraps provided video links from Vimeo in `vimeo_urls.txt`, downloads them, and re-upload them to Youtube one by one. The script is equipped with error logs and it Youtube Data API V3 for connecting with Google platform.

### Usage

> I will consider that you can deal with Google Cloud Platform and can enable Youtube Data API V3 and created an API key for connecting.

1) Edit the `<client_id>` & `<client_secret>` in `client_secrets.json` file.
2) run `pip install -r requirements.txt`
3) Put Vimeo links in `vimeo_urls.txt` file.
3) run the script `python vimeo_to_yt.py`
4) You'll get a link that authenticates your account for the script to use in YT.
5) Done! :)