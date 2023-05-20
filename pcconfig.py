import pynecone as pc

class StockleConfig(pc.Config):
    pass

config = StockleConfig(
    app_name="stockle",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
    bun_path="$HOME/.bun/bin/bun",
)
