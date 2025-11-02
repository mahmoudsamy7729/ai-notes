# 🧠 AI Notes App

AI Notes App is a simple yet powerful tool that helps you **take notes effortlessly** and **summarize them using AI**.  
Whether you’re in a meeting, brainstorming session, or lecture — just write your note and let the app handle the summarization for you.

---

## ✨ Features

- 📝 **Create Notes:**  
  Add a note with a **title** and **content** easily through the interface.

- 🤖 **AI Summarization:**  
  Each note is automatically summarized using AI — perfect for quick review later.

- 📚 **View All Notes:**  
  Access all your notes and their AI-generated summaries in one place.

- 💼 **Use Case:**  
  Ideal for meetings, research sessions, lectures, or personal journaling.

---

## 🧩 How It Works

1. The user enters:
   - A **title**
   - The **content** of the note  
2. The app sends the content to the AI summarizer.  
3. The AI generates a short summary.  
4. The summarized note is saved and displayed in the notes list.

---

## 🛠️ Tech Stack

- **Backend:** FastAPI  
- **Frontend:** (Optional — e.g., HTML, React, or any UI framework)  
- **AI:** HuggingFace 
- **Database:** PostgreSQL / Any preferred DB

---

## 🚀 Running the App

```bash
# 1. Clone the repository
git clone https://github.com/mahmoudsamy7729/ai-notes.git

# 2. Navigate to the project directory
cd ai-notes

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the FastAPI app
uvicorn main:app --reload
