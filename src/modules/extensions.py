import pickle

list_images = [
    ".jpeg",".jpg",".png",".gif",".webp",".tiff",".psd",".raw",".bmp",".heif",".indd",".svg",".ico"
    ]
list_documents = [
    ".doc",".txt",".pdf",".xlsx",".docx",".xls",".rtf",".md",".ods",".ppt",".pptx"
    ]
list_videos = [
    ".mp4",".mkv"
    ]
list_audio = [
    ".mp3",".wav",".m4a"
    ]
list_applications = [
    ".exe",".lnk"
    ]
list_codes = [
    ".c",".py",".java",".cpp",".js",".html",".css",".php"
    ]

extensions = {
    "Images" : list_images, 
    "Documents" : list_documents, 
    "Videos" : list_videos,
    "Audio" : list_audio,
    "Applications" : list_applications,
    "Code" : list_codes,
    }