#   =====================BEGINING OF THE EXAM PROJECT REQUIREMENTS====================== 
from fastapi import FastAPI
from routes import users, courses, enrollments
from fastapi.responses import Response

# --------- for fullstack -----------
from fastapi.middleware.cors import CORSMiddleware
# -----------------------------------


app = FastAPI(title="EduTrack Lite API")

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(courses.router, prefix="/courses", tags=["courses"])
app.include_router(enrollments.router, prefix="/enrollments", tags=["enrollments"])

@app.get("/")
def root():
    return {"msg": "EduTrack Lite API running"}

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return Response(status_code=204)
    
  # ===============THE END OF PROJECT REQUIREMENTS=====================  
  
  
# ==============FULLSTACK================ 
#   Allow frontend origins (localhost & GitHub Pages)
origins = [
    "http://127.0.0.1:5501",          # Local testing (VSCode Live Server)
    "http://localhost:5501",          # Local alternate
    "https://njorodev.github.io",     # Your GitHub Pages domain
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],   # Allow all HTTP methods
    allow_headers=["*"],   # Allow all headers
)
 
 

 

