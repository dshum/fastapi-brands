from sqlalchemy import select, cast
from sqlalchemy.dialects.postgresql import JSONB

from models.brands import Brand
from repositories.abstract.brands import SQLAlchemyRepository


class BrandRepository(SQLAlchemyRepository):
    model = Brand
