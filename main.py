from fastapi import FastAPI

from src.frameworks_challenges.app import app

main = FastAPI()

main.include_router(app)
