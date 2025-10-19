from django.core.management.base import BaseCommand
from portfolio.models import Experience, Project

class Command(BaseCommand):
    help = 'Populates database with resume data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Experience.objects.all().delete()
        Project.objects.all().delete()

        # Add Experiences
        experiences = [
            {
                'title': 'Associate Backend Developer',
                'company': 'MicroAgility',
                'start_date': 'June 2025',
                'end_date': 'Present',
                'description': '''• Developing NestJS + MongoDB backend for enterprise SaaS with modular architecture spanning HR, LMS, document management, and audit systems.
• Implementing REST APIs with JWT authentication, RBAC, file handling (GCS, Multer), input validation, logging, and centralized error handling.
• Working in Agile environment with cross-team collaboration; receiving hands-on training in GraphQL, multi-tenancy patterns, WebSockets, and microservices architecture (Node.js, Express, S3, Socket.IO).'''
            },
            {
                'title': 'JavaScript Developer',
                'company': 'NxtOf',
                'start_date': 'January 2025',
                'end_date': 'April 2025',
                'description': '''• Built web and mobile features for PropNerd, a real estate tokenization platform handling £500K+ in assets, using React Native and React.
• Developed secure APIs and responsive UIs with NestJS, GraphQL, and PostgreSQL, focusing on performance and scalability.
• Maintained and optimized core applications of NxtOf (a Web3 & AI solutions company) using TypeScript in a full-stack role.'''
            },
            {
                'title': 'Full Stack Developer Intern',
                'company': 'Futurenostics',
                'start_date': 'July 2024',
                'end_date': 'September 2024',
                'description': '''• Completed intensive full-stack development program with weekly technical assessments; built MERN stack applications using React, TypeScript, Chakra UI, and APIs with Axios and React Query.
• Built and managed backend systems with Express.js, MongoDB, and Mongoose, implementing data validation, RESTful APIs, and Git version control.
• Automated CI/CD pipeline using Docker, Kubernetes, Helm, and GitHub Actions for React application deployment.'''
            },
            {
                'title': 'Teaching Assistant & Lab Demonstrator',
                'company': 'FAST-NUCES',
                'start_date': 'May 2023',
                'end_date': 'May 2024',
                'description': '''• Assisted in teaching OOP (C++), Data Structures & Algorithms, and Software Design Analysis (UML, Java, Design Patterns) to 150+ students across multiple sections through lectures, lab sessions, and office hours.
• Guided 100+ students weekly in implementing algorithms, data structures, and OOP concepts, providing debugging and optimization support.
• Evaluated projects and assessments for 50+ students per semester, providing detailed feedback on code quality and software design.'''
            }
        ]

        for exp_data in experiences:
            Experience.objects.create(**exp_data)
            self.stdout.write(self.style.SUCCESS(f'Created: {exp_data["title"]} at {exp_data["company"]}'))

        # Add Projects
        projects = [
            {
                'title': 'Multi-Stage SaaS Backend',
                'tech_stack': 'NestJS, PostgreSQL, TypeORM, GraphQL, Socket.IO, Cloudinary, Winston',
                'description': '''• Developed a production-grade REST API with JWT authentication (access + refresh tokens), role-based access control (RBAC), email verification, and password reset, ensuring secure user management.
• Implemented database migrations, pagination, soft deletes, and file uploads with Cloudinary; added centralized logging with Winston and API documentation with Swagger/OpenAPI.
• Extended the system to GraphQL (Apollo Server) with type-safe queries and schema-driven design for flexible client integrations.
• Integrated real-time features including chat, notifications, and event broadcasting using Socket.IO (WebSockets).
• Architected a multi-tenant SaaS platform, isolating tenant data at the workspace level for scalability and security.
• Deployed on Render with rate limiting, input validation, and 90%+ unit/E2E test coverage.''',
                'github_link': 'https://github.com/saadamir1',
                'live_link': ''
            },
            {
                'title': 'Fashion Recommendation Platform - MeriCloset',
                'tech_stack': 'MERN Stack, TypeScript, Stripe, Google Gemini, BeautifulSoup',
                'description': '''• Built AI-powered platform with collaborative filtering, Gemini chatbot, and BeautifulSoup web scraping for product catalog (500+ products).
• Developed role-based portals (user, brand, admin) with Stripe payments, product comparison, wishlist, and JWT authentication.''',
                'github_link': 'https://github.com/saadamir1',
                'live_link': ''
            }
        ]

        for proj_data in projects:
            Project.objects.create(**proj_data)
            self.stdout.write(self.style.SUCCESS(f'Created: {proj_data["title"]}'))

        self.stdout.write(self.style.SUCCESS('\n✅ All data populated successfully!'))