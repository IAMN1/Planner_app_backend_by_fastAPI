from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from beanie import PydanticObjectId
from models.events import Event, EventUpdate
from database.connection import Database
from auth.authenticate import authenticate

event_router = APIRouter(tags=["Events"])

event_database = Database(Event)

@event_router.get('/', response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    events = await event_database.get_all()
    return events

@event_router.get('/{id}', response_model=Event)
async def retrieve_event(id: PydanticObjectId) -> Event:
    event = await event_database.get(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied does not exist!"
        )
    return event

@event_router.post('/new')
async def create_event(new_event: Event, user: str = Depends(authenticate)) -> dict:
    new_event.creator = user
    await event_database.save(new_event)
    return {"message": "Event created successfully"}

@event_router.put('/{id}', response_model=Event)
async def update_event(id: PydanticObjectId, body: EventUpdate, user: str = Depends(authenticate)) -> Event:
    event = await event_database.get(id)
    if event.creator != user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Operation not allowed"
        )
    
    updated_event = await event_database.update(id, body)
    if not updated_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID doesn't exist"
        )
    return updated_event

@event_router.delete('/delete/{id}')
async def delete_event(id: PydanticObjectId, user: str = Depends(authenticate)) -> dict:
    
    event = await event_database.get(id)
    
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied id does not exist"
        )
    
    if event.creator != user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not allowed"
        )
    
    event = await event_database.delete(id)

    return{"message": "Event deleted successfully!"}

