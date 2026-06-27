"""Migration for 1.0.11: publish OTA live-user detection fixes."""

from __future__ import annotations

from caramos_ota_update.context import MigrationContext

FROM_VERSION = "1.0.10"
TO_VERSION = "1.0.11"
DESCRIPTION = "Fix OTA migrations for systems without the default caram user"


def run(context: MigrationContext) -> None:
    """No-op migration; package payload contains fixes for earlier migration code."""

    context.log("installed OTA migration fixes for systems using custom usernames")
