# Personal Assistant (CLI) — JSON Storage

Консольное приложение на Python для управления:
- **книгой контактов** (имя, телефоны, e-mail, адрес, день рождения);
- **заметками** (текст + теги вида `#tag`).

## Требования

- Python **3.10+**
- Рекомендуется виртуальное окружение.

## Установка

```bash
git clone <repo_url> personal_assistant_bot
cd personal_assistant_bot

python -m venv .venv            # Windows: python
source .venv/bin/activate       # Windows PowerShell: .\.venv\Scripts\Activate.ps1

pip install -r requirements.txt   