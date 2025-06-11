# Jovis

*A lightweight JupyterHub setup for small‑team collaboration.*

---

## 1. Before You Start

1. **Clone the repository**
2. **Edit `.env`**  
   - At minimum, set  
     ```bash
     NOTEBOOK_DIR_PATH=<absolute_path_to_repo>/notebooks
     ```
   - Adjust any other settings as required for your environment.

---

## 2. Launching Jovis

```bash
docker compose up -d --build   # first launch (builds images)
docker compose up -d           # subsequent launches
```

> **Tip:** `docker compose logs -f` shows real‑time logs if you need to debug the start‑up sequence.

---

## 3. First Login

Jovis uses **FirstUseAuthenticator**:

- The very first login to the **admin account** sets its password.
- Additional users can be created later from **“Hub Control Panel → Admin”**.
- Each user sets their own password on their first login.

---

## 4. Collaborative Editing

For quick, friction‑free collaboration:

1. Create—or reuse—**one shared “project” account**.
2. Distribute its credentials to team members.
3. When two or more people are logged in under the same account,  
   `jupyter-collaboration-extension` automatically switches notebooks into real‑time co‑editing mode.

---

## 5. Pre‑installed Python Packages

| Package        |
|----------------|
| NumPy          |
| SciPy          |
| pandas         |
| Matplotlib     |
| scikit‑learn   |

You can add more libraries in `requirements.txt` or install them on‑the‑fly inside a running notebook.

---

## 6. Enabling HTTPS

For production deployments, place Jovis **behind a reverse proxy** such as Nginx or Traefik and terminate TLS there.

---

### Happy collaborating! 🚀