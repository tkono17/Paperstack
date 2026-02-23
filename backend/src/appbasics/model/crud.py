from dataclasses import dataclass
from typing import Optional, TypeVar, Annotated, Any
from fastapi import Query

@dataclass
class ObjId:
    value: Optional[str|int|float]
    key: Optional[str] = None

QueryC = TypeVar('Query')

TDb = TypeVar('TDb')
TPublic = TypeVar('TPublic')
TCreate = TypeVar('TCreate')
TUpdate = TypeVar('TUpdate')

@dataclass
class ObjCrud:
    def create(self, data: TPublic) -> TPublic:
        return data

    def get(self, where: QueryC = None) -> list[TPublic]:
        return []

    def get(self, oid: ObjId, where: QueryC = None) -> Optional[TPublic]:
        return None
    
    def update(self, oid: ObjId, data: TUpdate) -> TPublic:
        return TPublic()
    
    def delete(self, oid):
        return
    

@dataclass
class DataCrud:
    ClsPublic: TPublic
    ClsCreate: TCreate
    ClsUpdate: TUpdate

    def create(self, data: TPublic) -> TPublic:
        return data

    def get(self, where: QueryC = None) -> list[TPublic]:
        return []

    def get(self, oid: ObjId, where: QueryC = None) -> Optional[TPublic]:
        return None
    
    def update(self, oid: ObjId, data: TUpdate) -> TPublic:
        return TPublic()
    
    def delete(self, oid):
        return


SessionDep = TypeVar('SessionDep')


@dataclass
class DbCrud(ObjCrud):
    ClsDb: TDb
    session: SessionDep

    def create(self, data: TCreate, session: SessionDep) -> TPublic:
        data_db = self.ClsDb.model_validate(data)
        self.session.add(data_db)
        self.session.commit()
        self.session.refresh(data_db)
        return data_db

    def get(self, where: QueryC = None,
            offset: int = 0,
            limit: Annotated[int, Query(le=100)] = 100) -> list[TPublic]:
        v = []
        if where is None:
            statement = select(TDb).offset(offset).limit(limit)
            v = self.session.exec(statement).all()
        else:
            log.warning('DB read with query not supported yet.')
            log.info(where)
            v = []
        return v

    def get(self, oid: ObjId, where: QueryC = None) -> Optional[TPublic]:
        data = self.session.get(TDb, oid.value)
        if data is None:
            raise HTTPException(status_code=404,
                                detail=f'Entry with id={oid} not found')
        return data
    
    def update(self, oid: ObjId, data: TUpdate) -> TPublic:
        data_db = self.session.get(Document, oid.value)
        if data_db is None:
            raise HTTPException(status_code=404,
                                detail=f'Entry with id={oid} not found')
        udata = data.model_dump(exclude_unset=True)
        data_db.sqlmodel_update(udata)
        self.session.add(data_db)
        self.session.commit()
        self.session.refresh(data_db)
        return doc_db
    
    def delete(self, oid: ObjId):
        data_db = self.session.get(Document, oid.value)
        if data_db is None:
            raise HTTPException(status_code=404,
                                detail=f'Entry with oid={oid} not found')
        self.session.delete(data_db)
        self.session.commit()
        return { 'ok': True }

@dataclass
class JsonCrud(ObjCrud):
    document: dict[str, Any]
    collectionPaths: dict[str, str]
    
    def create(self, data: TCreate) -> TPublic:
        return data

    def get(self, where: QueryC = None) -> list[TPublic]:
        return []

    def get(self, oid: ObjId, where: QueryC = None) -> Optional[TPublic]:
        return None
    
    def update(self, oid: ObjId, data: TUpdate) -> TPublic:
        return TPublic()
    
    def delete(self, oid):
        return
