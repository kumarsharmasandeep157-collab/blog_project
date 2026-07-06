# DevBlog - Full Stack Django Blog Platform

A fully functional, modern blog application built using the Django web framework, custom relational database models, an interactive admin panel, user authentication systems, and a responsive frontend stylized with Bootstrap 5 templates.

This project was developed as part of the Python Web Development Internship at **Main Flow Services and Technologies Private Limited**.

---

## 🚀 Completed Milestones & Architecture

### Task 1: Environment, Database Schema & Admin Panel
- **Virtual Environment Setup:** Configured an isolated development workspace using `venv`.
- **Relational Models:** Built structured relational schemas for `Category`, `Post`, and `Comment` tables inside `models.py` with foreign key relations, status tags, slugs, and automated timestamp hooks.
- **Database Migrations:** Formulated and executed schema structures into an operational SQLite3 data store.
- **Custom Admin Interface:** Customized `admin.py` with column list filters, search fields, automated slug prepopulation, and status selectors. Prepared the initial application environment with production-ready posts and categories.

### Task 2: Web Views, User Authentication & CRUD Comment System
- **Routing Controllers:** Implemented robust Class-Based Views (`PostListView`, `PostDetailView`, `PostCreateView`, `PostUpdateView`, `PostDeleteView`) and functional handlers (`register_view`, `add_comment`).
- **Secure URL Routing:** Mapped all 7 required core endpoints including system auth paths (`django.contrib.auth.urls`) to process platform workflows seamlessly.
- **Authentication Security:** Applied view layer validation mixins (`LoginRequiredMixin`, `UserPassesTestMixin`) and wrappers (`@login_required`) to restrict access to administrative actions and commenting features.
- **Dynamic Frontend Templates:** Created structural HTML block templates (`base.html`, `home.html`, `post_detail.html`, `register.html`, `post_form.html`, `post_confirm_delete.html`) featuring customized Bootstrap 5 input layouts, responsive widgets, status badges, flash alert messages, and comments tracking pipelines.

---

##  Repository Directory Structure

```text
blog_project/
│
├── blog/
│   ├── migrations/      # Database evolution scripts
│   ├── templates/
│   │   └── blog/        # Responsive HTML frontends
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── post_detail.html
│   │       ├── post_form.html
│   │       ├── post_confirm_delete.html
│   │       └── register.html
│   ├── admin.py         # Dash custom filters and search hooks
│   ├── forms.py         # User accounts and post forms config
│   ├── models.py        # Database relational schemas
│   ├── urls.py          # App level path mappings
│   └── views.py         # Core business logic processing unit
│
├── blog_project/
│   ├── settings.py      # Core global configurations
│   └── urls.py          # Main project namespace root router
│
├── db.sqlite3           # Relational file data store
├── manage.py            # Command line operational manager
└── requirements.txt     # Complete environment package layout lock
