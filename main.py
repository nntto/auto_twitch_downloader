from twitchAPI.twitch import Twitch
from twitchAPI.helper import first
from twitchAPI.object.api import Video
import configparser
import os
from datetime import datetime
import asyncio
import subprocess


def output_file_path(video: Video, output_dir):
    return f"{output_dir}/{video.user_id}/{video.created_at.strftime('%Y%m%d%H%M%S')}_{video.id}_{video.title}.mp4"


def downloaded_video_ids(output_dir, streamer_id):
    # output_dir / streamer_id / 内のファイル名を取得
    file_names = os.listdir(f"{output_dir}/{streamer_id}")
    # ファイル名からvideo_idを取得
    video_ids = [file_name.split("_")[1] for file_name in file_names]
    return video_ids


def download_video(video: Video, quality, output_dir):
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = output_file_path(video, output_dir)

    # TwitchDownloaderCLIコマンドの実行
    subprocess.run(
        [
            "./TwitchDownloaderCLI",
            "videodownload",
            "--id",
            video.id,
            "-q",
            quality,
            "-o",
            output_file,
        ]
    )


# output_dir / streamer_id が存在しない場合は作成
def mkdir_if_not_exists(output_dir, streamer_id):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if not os.path.exists(f"{output_dir}/{streamer_id}"):
        os.makedirs(f"{output_dir}/{streamer_id}")


# 設定ファイルの読み込み
config = configparser.ConfigParser()
config.read("settings.ini")

# 設定値の取得
streamer_ids = config["Settings"]["StreamerIDs"].split(",")
quality = config["Settings"]["Quality"]
output_directory = config["Settings"]["OutputDirectory"]
app_id = config["Twitch"]["AppID"]
app_secret = config["Twitch"]["AppSecret"]


async def main():
    # Twitch APIの初期化
    twitch = await Twitch(app_id, app_secret)

    for streamer_id in streamer_ids:
        mkdir_if_not_exists(output_directory, streamer_id)

        # すでにダウンロード済みのvideo_idを取得
        download_video_ids = downloaded_video_ids(output_directory, streamer_id)

        # streamer_idの最新のvideoを取得
        async for video in twitch.get_videos(user_id=streamer_id):
            if video.id in download_video_ids:
                print(f"ダウンロード済: {video.title}")
                continue

            download_video(video, quality, output_directory)


if __name__ == "__main__":
    asyncio.run(main())
