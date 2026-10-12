from app.domain.data import Data
from app.repositories.storage.models.data import Data as DataModel


def map_to_domain(data: DataModel) -> Data:
    return Data(
        id=data.id,
        created_at=data.created_at,
        ip=data.ip,
        method=data.method,
        uri=data.uri,
        status_code=data.status_code,
    )

def map_to_model(data: Data) -> DataModel:
    return DataModel(
        id=data.id,
        ip=data.ip,
        method=data.method,
        uri=data.uri,
        status_code=data.status_code,
        created_at=data.created_at,
    )
