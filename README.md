# Automated Web App Deployment - Flask To-Do Application

A simple Flask-based To-Do application with automated CI/CD deployment using Jenkins and Docker.

## 🚀 Features

- **Simple To-Do Management**: Add and delete tasks with a clean, dark-themed UI
- **SQLite Database**: Lightweight database for task persistence
- **Automated CI/CD**: Jenkins pipeline for continuous integration and deployment
- **Containerized**: Docker and Docker Compose for consistent deployment
- **Production Ready**: Optimized Docker image with proper environment configuration

## 📋 Prerequisites

- Python 3.11+
- Docker and Docker Compose
- Jenkins (for automated deployment)
- Git

## 🛠️ Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/rakshitmalik136/Automated-Web-App-Deployment.git
   cd Automated-Web-App-Deployment
   ```

2. **Set up virtual environment** (recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   # Using the provided script
   chmod +x run.sh
   ./run.sh
   
   # Or manually
   export FLASK_APP=app.py
   export FLASK_ENV=development
   flask run
   ```

5. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

### Docker Deployment

1. **Build and run with Docker Compose**
   ```bash
   docker-compose up -d --build
   ```

2. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

3. **Stop the application**
   ```bash
   docker-compose down
   ```

## 🏗️ Architecture

```
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker image configuration
├── docker-compose.yml    # Docker Compose setup
├── Jenkinsfile           # Jenkins CI/CD pipeline
├── run.sh               # Local development script
└── templates/           # HTML templates
    ├── layout.html      # Base template with styling
    └── index.html       # Main page template
```

## 🔄 CI/CD Pipeline

The Jenkins pipeline includes the following stages:

1. **Code Clone**: Pulls the latest code from the GitHub repository
2. **Build & Test**: Builds the Docker image
3. **Push to DockerHub**: Tags and pushes the image to DockerHub
4. **Deploy**: Deploys the application using Docker Compose

### Setting up Jenkins

1. **Configure Jenkins Credentials**
   - Add DockerHub credentials with ID: `dockerHubCreds`
   - Username and password should match your DockerHub account

2. **Create a Jenkins Pipeline Job**
   - Point to this repository
   - Use the provided `Jenkinsfile`

3. **Environment Variables**
   The pipeline uses the following environment variables:
   - `dockerHubUser`: Your DockerHub username
   - `dockerHubPass`: Your DockerHub password

## 🐳 Docker Configuration

### Dockerfile
- Uses Python 3.11 slim base image
- Optimized for production with proper dependency caching
- Runs on port 5000

### Docker Compose
- Development-friendly configuration
- Volume mounting for live code changes
- Environment variable configuration

## 🗄️ Database

The application uses SQLite for simplicity:
- Database file: `todo.db`
- Single table: `tasks` with columns `id` and `content`
- Automatic initialization on first run

## 🎨 Frontend

- Clean, dark-themed UI using Simple.css
- Responsive design
- Centered layout with modern styling
- Task management with add/delete functionality

## 📝 API Endpoints

- `GET /`: Display all tasks
- `POST /add`: Add a new task
- `GET /delete/<task_id>`: Delete a specific task

## 🔧 Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `FLASK_APP` | Flask application entry point | `app.py` |
| `FLASK_ENV` | Flask environment | `production` (Docker), `development` (local) |
| `FLASK_RUN_HOST` | Host to bind the server | `0.0.0.0` |
| `FLASK_RUN_PORT` | Port to run the server | `5000` |

## 🚀 Deployment Options

### Manual Docker Build
```bash
# Build image
docker build -t flask-app .

# Run container
docker run -p 5000:5000 flask-app
```

### Production Deployment
For production deployment, consider:
- Using a production WSGI server (Gunicorn, uWSGI)
- Setting up reverse proxy (Nginx)
- Configuring proper logging
- Using environment-specific configurations
- Setting up database backups

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🔗 Links

- **Repository**: [https://github.com/rakshitmalik136/Automated-Web-App-Deployment](https://github.com/rakshitmalik136/Automated-Web-App-Deployment)
- **Issues**: Report bugs and request features via GitHub Issues

## 📞 Support

If you encounter any issues or have questions, please open an issue in the GitHub repository.

---

**Made with ❤️ using Flask, Docker, and Jenkins**
