from dotenv import dotenv_values
from pathlib import Path

DATA_DIR = Path("/root/data/prod")

config = dotenv_values()
config["DISCORD_DATA_DIR"] = DATA_DIR / "raw_discord_export"
config["SQLITE_FP"] = DATA_DIR / "database/discord_server.sqlite"
config["FILE_DUMPS_DIR"] = DATA_DIR / "file_dumps"
