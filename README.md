# Portfolio Website

A clean, professional portfolio website built with Django to showcase my work experience, projects, and skills.

## Features

- 🏠 **Multi-page architecture** - Home, About, Experience, Projects, Skills, Contact
- 📊 **Admin Panel** - Easy content management through Django admin
- 📝 **Contact Form** - Functional contact form with message storage
- 📄 **Resume Download** - Downloadable PDF resume
- 🎨 **Responsive Design** - Clean, professional UI
- ⚡ **Auto-populate Script** - Management command to load resume data

## Tech Stack

- **Backend:** Django 5.2, Python 3.13
- **Database:** SQLite
- **Frontend:** HTML5, CSS3
- **Styling:** Custom CSS with modern design patterns

## Project Structure

```
portfolio-django/
├── portfolio/                 # Main app
│   ├── management/           # Custom management commands
│   ├── migrations/           # Database migrations
│   ├── static/              # CSS and static files
│   ├── templates/           # HTML templates
│   ├── admin.py            # Admin configuration
│   ├── models.py           # Database models
│   ├── urls.py             # URL routing
│   └── views.py            # View functions
├── portfolio_django_app/    # Project settings
├── db.sqlite3              # Database
└── manage.py              # Django management script
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/saadamir1/portfolio-django.git
   cd portfolio-django
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Mac/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Load sample data (optional)**
   ```bash
   python manage.py populate_data
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

8. **Visit the site**
   - Portfolio: `http://127.0.0.1:8000/`
   - Admin Panel: `http://127.0.0.1:8000/admin/`

## Usage

### Adding Content

1. Access admin panel at `/admin`
2. Add/edit Experience entries
3. Add/edit Project entries
4. View contact messages

### Custom Management Commands

**Populate resume data:**
```bash
python manage.py populate_data
```

This command automatically populates the database with experience and project data.

## Models

### Experience
- Title, Company, Start Date, End Date, Description

### Project
- Title, Description, Tech Stack, GitHub Link, Live Link

### ContactMessage
- Name, Email, Message, Created At

## Deployment

For production deployment:

1. Update `ALLOWED_HOSTS` in settings.py
2. Set `DEBUG = False`
3. Configure static files collection
4. Use a production database (PostgreSQL recommended)
5. Set up environment variables for sensitive data

## Contributing

This is a personal portfolio project, but suggestions and feedback are welcome!

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

- **Email:** Saadamir070@gmail.com
- **LinkedIn:** [linkedin.com/in/saadamir1](https://linkedin.com/in/saadamir1)
- **GitHub:** [github.com/saadamir1](https://github.com/saadamir1)

---

Built with ❤️ using Django
