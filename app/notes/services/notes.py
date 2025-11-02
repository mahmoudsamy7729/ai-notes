from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession



from app.notes.models import Note
from app.auth.models import User
from app.notes import schema
from app.notes.services.ai_service import AIService


class NoteSerivce:
    @staticmethod
    async def read_notes(db: AsyncSession, current_user: User):
        notes = current_user.notes
        return notes
    

    @staticmethod
    async def create_note(note: schema.CreateNoteRequest, db: AsyncSession, current_user: User):

        # Get AI summary (not streaming, just a normal OpenAI call)
        note_summary = await AIService.summarize_notes(note.content)

        #Create new note
        new_note = Note(
            title=note.title,
            content=note.content,
            user_id=current_user.id,
            summary = note_summary
        )

        #Save to DB
        db.add(new_note)
        await db.commit()
        await db.refresh(new_note)
        return new_note