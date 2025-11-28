# Session 1: Hello-LLM Starter Kit

This is the starter kit for Session 1: "BOOT-CAMP & HELLO-LLM".

Your goal for this session is to complete the files in the `app/` directory to create a simple FastAPI application that uses Groq to answer a question.

## Project Structure

The final project structure should look like this:

```
chatbot-mini/
├── .venv/                       (ignored in git)
├── .env                         (created by student)
├── requirements.txt             (given by teacher)
├── app/
│   ├── __init__.py
│   ├── main.py                  (only 20 lines today)
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py            (given skeleton)
│   ├── api/
│   │   └── v1/
│   │       ├── __init__.py
│   │       └── endpoints/
│   │           ├── __init__.py
│   │           └── chat.py      (only 1 route today)
│   ├── services/
│   │   ├── __init__.py
│   │   └── llm_service.py       (given skeleton)
│   └── models/
│       ├── __init__.py
│       └── schemas.py           (given skeleton)
└── README.md                    (check-list inside)
```

## Wrap-up Checklist (Must be completed before Session 2)

Please check off all items below:

- [ ] `docker ps` works (Docker daemon running)
- [ ] `venv` activated, requirements installed (`pip install -r requirements.txt`)
- [ ] `.env` contains a real Groq key (`GROQ_API_KEY=gsk_...`)
- [ ] `uvicorn app.main:app --reload --port 8000` starts without error
- [ ] `/api/v1/chat` returns a JSON response when tested with Postman/Thunder Client/curl
- [ ] Screenshot of a successful API test (e.g., Thunder Client or curl) is saved

**Red-flag items – if any student still has these, do NOT proceed to Session 2:**
- "pip install" errors
- 401 / 403 from Groq (key issue)
- Port 8000 already in use
