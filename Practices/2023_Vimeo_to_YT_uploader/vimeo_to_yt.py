from datetime import datetime
import requests
import socket
import json
import time
import re
import os
import sys

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from googleapiclient.http import MediaFileUpload

scopes = ["https://www.googleapis.com/auth/youtube.upload"]
VIMEO_CONFIG_URL = "https://player.vimeo.com/video/{vid_id}/config"
socket.setdefaulttimeout(30000)

def get_vimeo_data(url) -> dict:
	"""
	Scraps Vimeo video config and wrangles data to return
	complete video filename + best resolution url to download
	the video from.
	"""
	vid_id = re.search(r"^https://vimeo.com/(\d+)", vimeo_vid_url)[1]
	vimeo_request_url = VIMEO_CONFIG_URL.format(vid_id=vid_id)
	vimeo_request = requests.get(vimeo_request_url)
	vimeo_request = json.loads(vimeo_request.content)

	video_title = vimeo_request["video"]["title"]
	vimeo_request = vimeo_request["request"]["files"]["progressive"]

	download_url: str
	codec: str
	vid_width: int = 0 
	for vid in vimeo_request:
		if vid["width"] > vid_width:
			download_url = vid["url"]
			vid_width = vid["width"]
			codec = vid["mime"].replace("video/", "")

	return {
		"title": f"{video_title}.{codec}",
		"url": download_url,
		"codec": codec
	}


def get_yt_instance() -> googleapiclient:
	# Disable OAuthlib's HTTPS verification when running locally.
	# *DO NOT* leave this option enabled in production.
	os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

	api_service_name = "youtube"
	api_version = "v3"
	client_secrets_file = "client_secrets.json"

	# Get credentials and create an API client
	flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
		client_secrets_file, scopes)
	credentials = flow.run_console()
	youtube = googleapiclient.discovery.build(
		api_service_name, api_version, credentials=credentials)

	return youtube


def yt_upload(youtube, vimeo_data) -> None:
	request = youtube.videos().insert(
		part = "snippet",
		body={
			"snippet": {
				"title": vimeo_data["title"].replace(".{}".format(vimeo_data["codec"]), "")
			}
		},
		media_body=MediaFileUpload(vimeo_data["title"])
	)
	response = request.execute()

	print(response)
	print("Video URL: https://www.youtube.com/watch?v={vid_id}&feature=youtu.be".format(vid_id=response["id"]))


if __name__ == "__main__":
	youtube = get_yt_instance()

	with open("vimeo_urls.txt", "r") as file:
		vimeo_vid_urls = file.readlines()

	for vimeo_vid_url in vimeo_vid_urls:
		try:
			vimeo_data = get_vimeo_data(vimeo_vid_url)

			print("[+] Downloading: {}".format(vimeo_data["title"]))
			video = requests.get(vimeo_data["url"])
			with open(vimeo_data["title"], "wb") as file:
				file.write(video.content)

			print("[+] Uploading: {}".format(vimeo_data["title"]))
			yt_upload(youtube, vimeo_data)

			print("[+] Done!")
			print("=============================================")

			os.remove(vimeo_data["title"])
		except Exception as err:
			print("[-] Failed to process: {url}".format(url="vimeo_vid_url"))
			print("=============================================")

			log_data = [
				datetime.now().strftime("%d %b %Y %I:%M %p"),
				vimeo_vid_url,
				err,
				"============================================="
			]

			with open("errors.txt", "a") as file:
				for l in log_data:
					file.write(str(l))
					file.write("\n")

			time.sleep(5)