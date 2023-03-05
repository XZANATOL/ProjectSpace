import pynecone as pc

config = pc.Config(
    app_name="pc_explore",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
    telemetry_enabled=False,
)
