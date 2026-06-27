"""baseline (empty)

Establishes the migration history. No schema yet — domain tables arrive with the
first bounded context (Identity, Release 2). Applying this creates Alembic's
``alembic_version`` tracking table and proves the migration pipeline end-to-end.

Revision ID: 0001_baseline
Revises:
Create Date: 2026-06-27
"""

from collections.abc import Sequence

revision: str = "0001_baseline"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
