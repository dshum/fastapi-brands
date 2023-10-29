import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration

from lib import settings

__all__ = ["configure"]


def configure() -> None:
    sentry_sdk.init(
        dsn=settings.sentry.DSN,
        environment=settings.app.ENVIRONMENT,
        release=settings.app.BUILD_NUMBER,
        integrations=[FastApiIntegration()],
        traces_sample_rate=settings.sentry.TRACES_SAMPLE_RATE,
        enable_tracing=settings.sentry.ENABLE,
    )
