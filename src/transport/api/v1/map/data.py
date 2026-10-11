from app.transport.api.v1.schemas.data import CreateData, OutData, Log
from app.domain.data import Data

def map_to_domain(data: CreateData) -> Data:
    return Data(
        ip=str(data.log.ip),
        method=data.log.method.value,
        uri=data.log.uri,
        status_code=data.log.status_code,
    )

def map_to_dto(data: Data) -> OutData:
    return OutData(
        id = data.id,
        created = data.created_at,
        log = Log(
            ip=data.ip,
            method=data.method,
            uri=data.uri,
            status_code=data.status_code,
        ),
    )
