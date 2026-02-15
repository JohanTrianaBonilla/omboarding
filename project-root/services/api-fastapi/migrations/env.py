from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# Importa tu Base (declarative_base)
from app.core.database import Base
from app.models import candidate  # importa tus modelos para que Alembic los detecte

# Configuración del archivo alembic.ini
config = context.config

# Setup logs
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadatos de SQLAlchemy para autogenerar migraciones
target_metadata = Base.metadata

def run_migrations_offline():
    """Ejecuta migraciones sin conexión."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Ejecuta migraciones con conexión."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
