from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import StreamingResponse


from app.core.database import get_db
from app.core.security import get_current_user
from app.auth.models import User
from app.notes import schema
from app.notes.services.notes import NoteSerivce
from app.notes.services.ai_service import AIService

router = APIRouter(prefix="/notes", tags=["Notes"])

db_dependency = Annotated[AsyncSession, Depends(get_db)]
user_dependency = Annotated[User, Depends(get_current_user)]

@router.get("/", response_model=schema.ListNoteResponse, status_code=status.HTTP_200_OK)
async def get_notes(db: db_dependency, current_user: user_dependency):
    notes = await NoteSerivce.read_notes(db, current_user)
    if not notes:
        return {
            "message": "No notes found.",
            "notes": []
                }
    return {
        "message": "Notes retrieved successfully",
        "notes": notes
    }


@router.post("/create", response_model=schema.CreateNoteResponse, status_code=status.HTTP_201_CREATED)
async def create_note(note_in: schema.CreateNoteRequest,db: db_dependency, currrent_user: user_dependency):
    new_note = await NoteSerivce.create_note(note_in, db, currrent_user)
    return {
        "message": "Note created successfully",
        "note": new_note   
    }


# @router.post("/summarize", status_code=status.HTTP_200_OK)
# async def summarize_no(current_user: user_dependency, db: db_dependency, ):
#     return StreamingResponse(AIService.summarize_notes(), media_type="text/event-stream")
