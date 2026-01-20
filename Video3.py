from openai import OpenAI

client = OpenAI()

# video = client.videos.create(
#   model = "sora-2",
#   prompt = "A futuristic city in the style of cyberpunk with neon lights.", # A calico cat playing a piano on stage
#   size = "1280x720", # Optional: 720x1280, 1280x720, 1024x1792, 1792x1024
#   seconds = "8"      # Optional: 4, 8, or 12 seconds
# )
# 
# print(video.id)

completed_video = client.videos.retrieve("video_696f8389a29081919155b7ed743224480323d770f1dc212e") # video.id
print(completed_video)
if completed_video.status == "completed":
  response = client.videos.download_content(video_id = "video_696f8389a29081919155b7ed743224480323d770f1dc212e")
  with open("video2.mp4", "wb") as f:
    f.write(response.content)
  # video_content = client.videos.content.retrieve(video.id)
  # print(f"Watch your video here: {video_content.url}")
else:
  print("A videó még nincs kész.")


# video_696f83186d8081918eaaa290e816e1f60f6546425ad962af
# video_696f8389a29081919155b7ed743224480323d770f1dc212e
