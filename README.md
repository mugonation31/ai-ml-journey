# AI/ML Learning Tracker — GitHub-Linked

This repo links your **daily learning progress** to an Excel tracker.

## 🧩 How it works
- You commit work with a tag in your commit message like **`[W1D3]`** (Week 1, Day 3).
- A GitHub Action reads the last commit message and updates `progress/12-week-progress-tracker.xlsx`, marking that day as **✅ Done**.
- The Action then commits the updated tracker back to the repo automatically.

## ✅ Commit message convention
Use **one** of the following tags at the **start** of your commit message:
- `[W1D1]`, `[W1D2]`, ..., `[W1D7]`
- `[W2D1]` … `[W12D7]`

**Examples**
- `[W3D2] add pandas groupby notebook and charts`
- `[W5D4] tuned logistic regression C parameter + README`

> Tip: Keep one tag per commit to make updates unambiguous.

## 📦 Files
- `progress/12-week-progress-tracker.xlsx` — your master tracker (edit status manually if needed).
- `scripts/update_tracker.py` — updates the tracker from a commit tag.
- `.github/workflows/update-tracker.yml` — automation that runs on every push.

## 🔧 Local use (optional)
You can run the updater locally too:

```bash
python3 -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/update_tracker.py "[W1D3] any message"
```

## 📝 Requirements
Create a `requirements.txt` with:
```
pandas
openpyxl
```

## 🛡️ Notes
- The GitHub Action uses the built-in `GITHUB_TOKEN` to commit the updated Excel file.
- If you push multiple commits, the **latest** commit message tag wins for that push event.
- If the tag is missing or malformed, the Action does nothing.
