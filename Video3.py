from openai import OpenAI

client = OpenAI()

video = client.videos.create(
  model = "sora-2",
  prompt = "As a cartoon from the 1950th: A young woman on the beach. She says Hi! I'm sunbathing, while she waves.", # A futuristic city in the style of cyberpunk with neon lights. # A calico cat playing a piano on stage
  size = "1280x720", # Optional: 720x1280, 1280x720, 1024x1792, 1792x1024
  seconds = "4"      # Optional: 4, 8, or 12 seconds
)

print(video.id)

completed_video = client.videos.retrieve(video.id) # 
print(completed_video)
if completed_video.status == "completed":
  response = client.videos.download_content(video_id = video.id)
  with open("video2.mp4", "wb") as f:
    f.write(response.content)
else:
  print("A videó még nincs kész.")
  while completed_video.status != "completed":
    completed_video = client.videos.retrieve(video.id)
    print(completed_video)
    if completed_video.status == "failed":
      print(f"A videó megbukott.") # : {completed_video.message}
      break
  
  if completed_video.status == "completed":
    response = client.videos.download_content(video_id = video.id)
    with open("video4.mp4", "wb") as f:
      f.write(response.content)


# video_696f83186d8081918eaaa290e816e1f60f6546425ad962af
# video_696f8389a29081919155b7ed743224480323d770f1dc212e
# video_6970704d35948191b38579615ce117a3011c65b27c3aa15e
