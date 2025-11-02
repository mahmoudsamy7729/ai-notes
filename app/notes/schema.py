from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field, ConfigDict


class NoteOut(BaseModel):
    id: UUID
    title: str
    content: str
    summary: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CreateNoteRequest(BaseModel):
    title: str = Field(..., max_length=255, examples=["Note Title Example"])
    content: str = Field(..., examples=["This is the content of the note."])


class CreateNoteResponse(BaseModel):
    message: str
    note: NoteOut


class ListNoteResponse(BaseModel):
    message: str
    notes: list[NoteOut]





