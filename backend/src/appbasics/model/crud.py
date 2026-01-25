from dataclasses import dataclass
from typing import Optional, TypeVar

@dataclass
class ObjId:
    key: Optional[str] = None
    value: Optional[str|int|float] = None

Query = TypeVar('Query')

TDb = TypeVar('TDb')
TPublic = TypeVar('TPublic')
TCreate = TypeVar('TCreate')
TUpdate = TypeVar('TUpdate')

@dataclass
class ObjCrud:
    def create(self, data: TPublic) -> TPublic:
        return data

    def get(self, where: Query = None) -> list[TPublic]:
        return []

    def get(self, oid: ObjId, where: Query = None) -> Optional[TPublic]:
        return None
    
    def update(self, oid: ObjId, data: TUpdate) -> TPublic:
        return TPublic()
    
    def delete(self, oid):
        return
    

@dataclass
class DataCrud:
    document: Any = None
    holderPath: str

    def create(self, data: TPublic) -> TPublic:
        return data

    def get(self, where: Query = None) -> list[TPublic]:
        return []

    def get(self, oid: ObjId, where: Query = None) -> Optional[TPublic]:
        return None
    
    def update(self, oid: ObjId, data: TUpdate) -> TPublic:
        return TPublic()
    
    def delete(self, oid):
        return


SessionDep = TypeVar('SessionDep')


@dataclass
class DbCrud(ObjCrud):
    ClsDb: TDb
    ClsPublic: TPublic
    ClsCreate: TCreate
    ClsUpdate: TUpdate

    def create(self, data: TCreate, session: SessionDep) -> TPublic:
        data_db = self.ClsDb.model_validate(data)
        session.add(data_db)
        session.commit()
        session.refresh(data_db)
        return data_db

    def get(self, where: Query = None) -> list[TPublic]:
        return []

    def get(self, oid: ObjId, where: Query = None) -> Optional[TPublic]:
        return None
    
    def update(self, oid: ObjId, data: TUpdate) -> TPublic:
        return TPublic()
    
    def delete(self, oid):
        return
