# Environment Setup Guide

This guide explains how to use the `env.example` template to configure your FastAPI application.

## 🎯 **Quick Setup**

### **1. Copy the Template**
```bash
cp env.example .env
```

### **2. Generate Secure Secret Key**
```bash
# Generate a secure secret key for JWT tokens
openssl rand -hex 32
```

### **3. Edit Your .env File**
Open `.env` in your editor and customize the values below.

## 📋 **Required Configuration**

### **🔐 Security Settings (CRITICAL)**
```env
# Replace with generated secret key from step 2
SECRET_KEY="your-generated-secret-key-here"

# Leave these as default unless you know what you're doing
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### **👤 Superuser Account**
```env
# Change these to your preferred admin credentials
FIRST_SUPERUSER="admin@yourdomain.com"
FIRST_SUPERUSER_PASSWORD="your-secure-password"
```

### **🌐 CORS Configuration**
```env
# For development - allows frontend connections
BACKEND_CORS_ORIGINS="http://localhost:3000,http://localhost:8000,http://127.0.0.1:3000,http://127.0.0.1:8000"

# For production - specify your actual domains
# BACKEND_CORS_ORIGINS="https://yourdomain.com,https://api.yourdomain.com"
```

## 🔧 **Optional Configuration**

### **💾 Database Settings**
```env
# Default SQLite (good for development)
DATABASE_URL="sqlite:///./app.db"

# PostgreSQL for production
# DATABASE_URL="postgresql://username:password@localhost:5432/database_name"
```

### **📧 Email Configuration**
```env
# Disable emails in development
EMAILS_ENABLED=false

# Enable for production with real SMTP settings
# EMAILS_ENABLED=true
# SMTP_HOST="smtp.gmail.com"
# SMTP_PORT=587
# SMTP_USER="your-email@gmail.com"
# SMTP_PASSWORD="your-app-password"
```

### **🐛 Development Settings**
```env
# Keep true for development
DEBUG=true
LOG_LEVEL="INFO"
```

## 🚀 **Environment-Specific Examples**

### **Development .env**
```env
SECRET_KEY="fa6e138f80c5055940129a70c4b1654d69fd2f31d7b4f967c205cef3995edf4e"
DATABASE_URL="sqlite:///./app.db"
FIRST_SUPERUSER="dev@example.com"
FIRST_SUPERUSER_PASSWORD="devpassword123"
BACKEND_CORS_ORIGINS="http://localhost:3000,http://localhost:8000"
DEBUG=true
EMAILS_ENABLED=false
```

### **Production .env**
```env
SECRET_KEY="your-production-secret-generated-with-openssl"
DATABASE_URL="postgresql://user:password@db:5432/fastapi_prod"
FIRST_SUPERUSER="admin@yourcompany.com"
FIRST_SUPERUSER_PASSWORD="very-secure-production-password"
BACKEND_CORS_ORIGINS="https://yourapp.com,https://api.yourapp.com"
DEBUG=false
EMAILS_ENABLED=true
SMTP_HOST="smtp.sendgrid.net"
SMTP_PORT=587
SMTP_USER="apikey"
SMTP_PASSWORD="your-sendgrid-api-key"
```

## ✅ **Verification Steps**

### **1. Test Configuration Loading**
```bash
# This should run without configuration errors
make lint
```

### **2. Start the Application**
```bash
# Start development server
make dev
```

### **3. Check API Documentation**
```bash
# Open in browser or test with curl
curl http://localhost:8000/docs
```

### **4. Test Database Connection**
```bash
# Run database migrations
poetry run alembic upgrade head
```

## 🔒 **Security Best Practices**

### **✅ DO:**
- Always generate unique SECRET_KEY for each environment
- Use strong passwords for FIRST_SUPERUSER_PASSWORD
- Keep .env files out of version control (already in .gitignore)
- Use environment-specific configurations
- Regularly rotate secrets in production

### **❌ DON'T:**
- Never commit .env files to git
- Don't use default passwords in production
- Don't share SECRET_KEY between environments
- Don't use DEBUG=true in production
- Don't hardcode secrets in code

## 🔍 **Troubleshooting**

### **Common Issues:**

**1. "Settings has no attribute X" errors**
- Make sure all variables in `env.example` are in your `.env`
- Check for typos in variable names

**2. Database connection errors**
- Verify DATABASE_URL format
- Ensure database exists (SQLite auto-creates)
- Check PostgreSQL credentials and connectivity

**3. CORS errors**
- Add your frontend URL to BACKEND_CORS_ORIGINS
- Include both localhost and 127.0.0.1 variants
- Check port numbers match your frontend

**4. JWT token errors**
- Ensure SECRET_KEY is properly set
- Verify ALGORITHM is "HS256"
- Check ACCESS_TOKEN_EXPIRE_MINUTES is a number

## 📚 **Configuration Reference**

| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| `SECRET_KEY` | string | Yes | JWT signing key (generate with openssl) |
| `DATABASE_URL` | string | Yes | Database connection string |
| `FIRST_SUPERUSER` | email | Yes | Initial admin user email |
| `FIRST_SUPERUSER_PASSWORD` | string | Yes | Initial admin password |
| `BACKEND_CORS_ORIGINS` | csv | No | Allowed CORS origins |
| `DEBUG` | boolean | No | Development mode flag |
| `EMAILS_ENABLED` | boolean | No | Enable email functionality |

For complete list, see `env.example` file comments.

## 🎯 **Next Steps**

After setting up your environment:

1. **Create superuser**: `poetry run python -m app.db.init_db`
2. **Run tests**: `make test`
3. **Start coding**: Follow the patterns in `.cursorrules`
4. **Deploy**: Use production .env configuration

Need help? Check `PROJECT_CONTEXT.md` for architecture guidance!
